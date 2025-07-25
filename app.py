"""
API Flask para el sistema de detección de ciberacoso.
Conecta el frontend con los algoritmos de backend.
"""

from flask import Flask, request, jsonify, render_template, send_from_directory
from flask_cors import CORS
import os
import csv
import sys
import time
from werkzeug.utils import secure_filename
# Agregar el directorio actual al path
sys.path.append(os.path.dirname(os.path.abspath(__file__)))

from algorithms.analyzer import CyberbullyingAnalyzer
from algorithms.selector import AlgorithmSelector
from recommendations_engine import get_recommendations_for_analysis
##Comentario Harry

UPLOAD_FOLDER = os.path.join(os.getcwd(), 'uploads')
BASE_FILE = 'patrones.csv'
ALLOWED_EXTENSIONS = {'csv', 'txt'}
MAX_FILES = 5
TIEMPO_MAXIMO = 86400

# Crear la instancia de Flask
app = Flask(__name__)
CORS(app)  # habilitar CORS si lo necesitas

if not os.path.exists(UPLOAD_FOLDER):
    os.makedirs(UPLOAD_FOLDER)
COMBINED_FILE = 'patrones_combinado.csv'

def generar_archivo_combinado():
    """
    Combina patrones.csv (base) + todos los CSV de uploads en un solo archivo temporal.
    """
    patrones = cargar_todos_los_patrones()
    if not patrones:
        return

    fieldnames = ['id', 'frase', 'categorias', 'nivel_gravedad', 'descripcion']
    severity_map = {
        'Muy Alto': 90,
        'Alto': 70,
        'Medio': 50,
        'Bajo': 20
    }

    with open(COMBINED_FILE, 'w', newline='', encoding='utf-8') as f:
        writer = csv.DictWriter(f, fieldnames=fieldnames)
        writer.writeheader()
        for p in patrones:
            sev_text = p.get('severity', '')
            sev_num = severity_map.get(sev_text, 50)
            writer.writerow({
                'id': p.get('id', ''),
                'frase': p.get('pattern', ''),
                'categorias': p.get('category', ''),
                'nivel_gravedad': sev_num,
                'descripcion': p.get('description', '')
            })
    print(f"[INFO] Archivo combinado generado con {len(patrones)} patrones.")

def map_severity(value):
    try:
        val = int(value)
    except:
        return value  # ya viene como texto
    if val >= 85:
        return 'Muy Alto'
    elif val >= 70:
        return 'Alto'
    elif val >= 50:
        return 'Medio'
    else:
        return 'Bajo'
    
REQUIRED_COLUMNS_1 = {'id', 'frase', 'categorias', 'nivel_gravedad', 'descripcion'}
REQUIRED_COLUMNS_2 = {'id', 'mensaje', 'gravedad', 'categoria', 'etiqueta'}

def validar_columnas(filepath):
    with open(filepath, newline='', encoding='utf-8') as f:
        reader = csv.reader(f)
        headers = next(reader, None)
        if headers is None:
            return False
        headers_lower = set(h.strip().lower() for h in headers)
        return (REQUIRED_COLUMNS_1 <= headers_lower) or (REQUIRED_COLUMNS_2 <= headers_lower)


def allowed_file(filename):
    return '.' in filename and filename.rsplit('.', 1)[1].lower() in ALLOWED_EXTENSIONS


# Patrones básicos de respaldo en caso de que el CSV no se cargue
PATRONES_RESPALDO = [
    {'id': '1', 'pattern': 'eres un inútil', 'category': 'insulto directo', 'severity': 'Muy Alto', 'description': 'Insulto directo'},
    {'id': '2', 'pattern': 'no sirves para nada', 'category': 'humillación', 'severity': 'Muy Alto', 'description': 'Humillación'},
    {'id': '3', 'pattern': 'cállate de una vez', 'category': 'agresión verbal', 'severity': 'Alto', 'description': 'Orden agresiva'},
    {'id': '4', 'pattern': 'idiota', 'category': 'insulto directo', 'severity': 'Alto', 'description': 'Insulto común'},
    {'id': '5', 'pattern': 'estúpido', 'category': 'insulto cognitivo', 'severity': 'Alto', 'description': 'Ataque a inteligencia'},
    {'id': '6', 'pattern': 'tonto', 'category': 'insulto leve', 'severity': 'Medio', 'description': 'Insulto menor'},
    {'id': '7', 'pattern': 'feo', 'category': 'insulto físico', 'severity': 'Medio', 'description': 'Ataque apariencia'},
    {'id': '8', 'pattern': 'gordo', 'category': 'insulto físico', 'severity': 'Medio', 'description': 'Comentario peso'},
    {'id': '9', 'pattern': 'nadie te quiere', 'category': 'exclusión social', 'severity': 'Alto', 'description': 'Exclusión social'},
    {'id': '10', 'pattern': 'eres un perdedor', 'category': 'desprecio', 'severity': 'Alto', 'description': 'Desprecio general'}
]

def cargar_todos_los_patrones():
    patrones_dict = {}  # clave: texto normalizado, valor: patrón con más gravedad
    
    print(f"[DEBUG] Intentando cargar patrones...")
    print(f"[DEBUG] BASE_FILE: {BASE_FILE}")
    print(f"[DEBUG] Directorio actual: {os.getcwd()}")
    print(f"[DEBUG] BASE_FILE existe: {os.path.exists(BASE_FILE)}")

    def procesar_row(row):
        mensaje = (row.get('frase') or row.get('mensaje') or '').strip().lower()
        if not mensaje:
            return
        gravedad_valor = row.get('nivel_gravedad') or row.get('gravedad') or '0'
        try:
            gravedad_num = int(gravedad_valor)
        except:
            gravedad_num = 0

        nuevo_patron = {
            'id': row.get('id', ''),
            'pattern': row.get('frase') or row.get('mensaje', ''),
            'category': row.get('categorias') or row.get('categoria', ''),
            'severity': map_severity(gravedad_valor),
            'severity_num': gravedad_num,  # campo auxiliar para comparar
            'description': row.get('descripcion') or row.get('etiqueta', '')
        }

        # Mantener solo el de mayor gravedad
        if mensaje not in patrones_dict or gravedad_num > patrones_dict[mensaje]['severity_num']:
            patrones_dict[mensaje] = nuevo_patron

    # --- Procesar archivo base ---
    if os.path.exists(BASE_FILE):
        print(f"[DEBUG] Cargando archivo base: {BASE_FILE}")
        try:
            with open(BASE_FILE, 'r', encoding='utf-8') as f:
                reader = csv.DictReader(f)
                count = 0
                for row in reader:
                    procesar_row(row)
                    count += 1
                print(f"[DEBUG] Procesadas {count} líneas del archivo base")
        except Exception as e:
            print(f"[ERROR] Error leyendo archivo base: {e}")
    else:
        print(f"[WARNING] Archivo base {BASE_FILE} no encontrado")

    # --- Procesar archivos subidos ---
    if os.path.exists(UPLOAD_FOLDER):
        print(f"[DEBUG] Revisando archivos en {UPLOAD_FOLDER}")
        for archivo in os.listdir(UPLOAD_FOLDER):
            ruta = os.path.join(UPLOAD_FOLDER, archivo)
            if os.path.isfile(ruta) and allowed_file(archivo):
                try:
                    with open(ruta, 'r', encoding='utf-8') as f:
                        reader = csv.DictReader(f)
                        count = 0
                        for row in reader:
                            procesar_row(row)
                            count += 1
                        print(f"[DEBUG] Procesadas {count} líneas de {archivo}")
                except Exception as e:
                    print(f"[ERROR] Error leyendo {archivo}: {e}")

    # Convertir dict a lista y eliminar campo auxiliar
    patrones_final = []
    for pat in patrones_dict.values():
        pat.pop('severity_num', None)
        patrones_final.append(pat)

    print(f"[DEBUG] Total patrones finales: {len(patrones_final)}")
    
    # Si no se cargaron patrones, usar los de respaldo
    if len(patrones_final) == 0:
        print("[WARNING] No se cargaron patrones desde archivos, usando patrones de respaldo")
        patrones_final = PATRONES_RESPALDO.copy()
        print(f"[DEBUG] Usando {len(patrones_final)} patrones de respaldo")
    
    return patrones_final


def limpiar_archivos():
    ahora = time.time()
    for archivo in os.listdir(UPLOAD_FOLDER):
        ruta = os.path.join(UPLOAD_FOLDER, archivo)
        if os.path.isfile(ruta):
            edad = ahora - os.path.getctime(ruta)
            if edad > TIEMPO_MAXIMO:
                os.remove(ruta)

# --- API para listar archivos ---
@app.route('/api/list-files', methods=['GET'])
def list_files():
    try:
        files = []
        # Incluir el archivo base como protegido
        base_path = os.path.join(os.getcwd(), BASE_FILE)
        if os.path.exists(base_path):
            size = os.path.getsize(base_path) // 1024
            files.append({'name': BASE_FILE, 'size': size, 'protected': True})
        # Incluir archivos de uploads
        for archivo in os.listdir(UPLOAD_FOLDER):
            ruta = os.path.join(UPLOAD_FOLDER, archivo)
            if os.path.isfile(ruta):
                size = os.path.getsize(ruta) // 1024
                files.append({'name': archivo, 'size': size, 'protected': False})
        return jsonify({'success': True, 'files': files})
    except Exception as e:
        return jsonify({'success': False, 'error': f'No se pudieron listar los archivos: {str(e)}'}), 500

# --- API para subir archivos ---
@app.route('/api/upload-patterns', methods=['POST'])
def upload_patterns():
    try:
        limpiar_archivos()
        # validar cantidad
        archivos_existentes = os.listdir(UPLOAD_FOLDER)
        if len(archivos_existentes) >= MAX_FILES:
            return jsonify({'success': False, 'error': 'Se alcanzó el máximo de archivos permitidos.'}), 400

        if 'file' not in request.files:
            return jsonify({'success': False, 'error': 'No se envió ningún archivo'}), 400

        file = request.files['file']
        if file.filename == '':
            return jsonify({'success': False, 'error': 'Nombre de archivo vacío'}), 400

        # proteger nombre base
        if file.filename.lower() == BASE_FILE.lower():
            return jsonify({'success': False, 'error': 'No se puede subir un archivo con el nombre reservado patrones.csv'}), 400

        if file and allowed_file(file.filename):
            filename = secure_filename(file.filename)
            filepath = os.path.join(UPLOAD_FOLDER, filename)

            if os.path.exists(filepath):
                return jsonify({'success': False, 'error': 'El archivo ya existe en el servidor.'}), 400

            # guardar provisional
            file.save(filepath)

            # validar encabezados
            try:
                with open(filepath, 'r', encoding='utf-8') as f:
                    header = f.readline().strip().lower().split(',')
                    columnas = ['id', 'frase', 'categorias', 'nivel_gravedad', 'descripcion']
                    for col in columnas:
                        if col not in [h.strip() for h in header]:
                            os.remove(filepath)
                            return jsonify({'success': False, 'error': f'Falta columna requerida: {col}'}), 400
            except Exception as e:
                os.remove(filepath)
                return jsonify({'success': False, 'error': f'Archivo inválido: {str(e)}'}), 400
            # validar columnasgenerar_archivo_combinado()
            generar_archivo_combinado()
            analyzer.load_patterns()

            return jsonify({'success': True, 'message': f'{filename} subido correctamente.'})
        else:
            return jsonify({'success': False, 'error': 'Formato no permitido (solo .csv o .txt)'}), 400
    except Exception as e:
        return jsonify({'success': False, 'error': f'Error al subir archivo: {str(e)}'}), 500


# --- API para eliminar archivo ---
@app.route('/api/delete-file', methods=['POST'])
def delete_file():
    try:
        data = request.get_json()
        if not data or 'filename' not in data:
            return jsonify({'success': False, 'error': 'Archivo no especificado'}), 400
        filename = data['filename']
        if filename.lower() == BASE_FILE.lower():
            return jsonify({'success': False, 'error': 'No se puede eliminar el archivo base'}), 400
        filepath = os.path.join(UPLOAD_FOLDER, filename)
        if os.path.exists(filepath):
            os.remove(filepath)
            generar_archivo_combinado()
            analyzer.load_patterns()

            return jsonify({'success': True, 'message': f'{filename} eliminado correctamente'})
        else:
            return jsonify({'success': False, 'error': 'El archivo no existe'}), 400
    except Exception as e:
        return jsonify({'success': False, 'error': f'Error al eliminar archivo: {str(e)}'}), 500
@app.route('/api/delete-pattern', methods=['POST'])
def delete_pattern():
    try:
        data = request.get_json()
        if not data or 'id' not in data:
            return jsonify({'success': False, 'error': 'ID no especificado'}), 400

        pattern_id = str(data['id'])

        # proteger los datos primarios
        if pattern_id.isdigit() and int(pattern_id) <= 115:
            return jsonify({'success': False, 'error': 'Este patrón está protegido y no se puede eliminar.'}), 403

        # leer y filtrar el CSV
        nuevos_registros = []
        eliminado = False
        headers = ['id','frase','categorias','nivel_gravedad','descripcion']

        if os.path.exists(BASE_FILE):
            with open(BASE_FILE, 'r', encoding='utf-8') as f:
                reader = csv.DictReader(f)
                headers = reader.fieldnames
                for row in reader:
                    if row['id'] != pattern_id:
                        nuevos_registros.append(row)
                    else:
                        eliminado = True

        if eliminado:
            with open(BASE_FILE, 'w', newline='', encoding='utf-8') as f:
                writer = csv.DictWriter(f, fieldnames=headers)
                writer.writeheader()
                writer.writerows(nuevos_registros)

            generar_archivo_combinado()
            analyzer.load_patterns()

            return jsonify({'success': True, 'message': f'Patrón con ID {pattern_id} eliminado correctamente'})
        else:
            return jsonify({'success': False, 'error': 'No se encontró el patrón a eliminar'}), 404

    except Exception as e:
        return jsonify({'success': False, 'error': f'Error al eliminar patrón: {str(e)}'}), 500


# Configuración
app.config['SECRET_KEY'] = 'safetext-cyberbullying-detection-2025'

# Inicializar el analizador
print("[INIT] Inicializando aplicación...")
print(f"[INIT] Directorio de trabajo: {os.getcwd()}")
print(f"[INIT] Archivos en directorio: {os.listdir('.')}")

selector = AlgorithmSelector()
print("[INIT] Generando archivo combinado...")
generar_archivo_combinado()
print("[INIT] Inicializando analizador...")
analyzer = CyberbullyingAnalyzer(patterns_file=COMBINED_FILE)
print("[INIT] Cargando patrones...")
analyzer.load_patterns()
print(f"[INIT] Patrones cargados en analyzer: {len(analyzer.patterns) if hasattr(analyzer, 'patterns') else 'No disponible'}")
print("[INIT] Inicialización completada.")
  
            # Cargar patrones desde el archivo combinado
@app.route('/')
def index():
    """Redirige a la página principal del frontend."""
    return send_from_directory('templates', 'index.html')

@app.route('/index.html')
def index_page():
    """Sirve la página principal."""
    return send_from_directory('templates', 'index.html')

@app.route('/config.html')
def config_page():
    """Sirve la página de configuración."""
    return send_from_directory('templates', 'config.html')
#Comentario XD
@app.route('/resultados.html')
def results_page():
    """Sirve la página de resultados."""
    return send_from_directory('templates', 'resultados.html')

@app.route('/templates/<path:filename>')
def serve_templates(filename):
    """Sirve archivos de templates."""
    return send_from_directory('templates', filename)

@app.route('/static/<path:filename>')
def serve_static(filename):
    """Sirve archivos estáticos."""
    return send_from_directory('static', filename)

@app.route('/api/analyze', methods=['POST'])
def analyze_text():
    """
    Analiza un texto para detectar ciberacoso.
    """
    try:
        data = request.get_json()

        if not data or 'text' not in data:
            return jsonify({
                'success': False,
                'error': 'Texto no proporcionado'
            }), 400

        text = data['text']

        if not text.strip():
            return jsonify({
                'success': False,
                'error': 'El texto no puede estar vacío'
            }), 400

        # ✅ Usar directamente el analizador sin recargar patrones
        result = analyzer.analyze_text(text)

        return jsonify({
            'success': True,
            'result': result
        })

    except Exception as e:
        return jsonify({
            'success': False,
            'error': f'Error en el análisis: {str(e)}'
        }), 500


@app.route('/api/analyze-pattern', methods=['POST'])

def analyze_pattern():
    """
    Analiza las características de un patrón específico.
    
    Request JSON:
    {
        "pattern": "patrón a analizar"
    }
    
    Response JSON:
    {
        "success": true,
        "analysis": { ... análisis del patrón ... }
    }
    """
    try:
        data = request.get_json()
        
        if not data or 'pattern' not in data:
            return jsonify({
                'success': False,
                'error': 'Patrón no proporcionado'
            }), 400
        
        pattern = data['pattern']
        
        # Analizar el patrón
        analysis = selector.analyze_pattern(pattern)
        
        return jsonify({
            'success': True,
            'analysis': analysis
        })
        
    except Exception as e:
        return jsonify({
            'success': False,
            'error': f'Error en el análisis del patrón: {str(e)}'
        }), 500

@app.route('/api/search-pattern', methods=['POST'])
def search_pattern():
    """
    Busca un patrón específico en un texto.
    
    Request JSON:
    {
        "text": "Texto donde buscar",
        "pattern": "Patrón a buscar"
    }
    
    Response JSON:
    {
        "success": true,
        "result": { ... resultado de la búsqueda ... }
    }
    """
    try:
        data = request.get_json()
        
        if not data or 'text' not in data or 'pattern' not in data:
            return jsonify({
                'success': False,
                'error': 'Texto y patrón son requeridos'
            }), 400
        
        text = data['text']
        pattern = data['pattern']
        
        if not text.strip() or not pattern.strip():
            return jsonify({
                'success': False,
                'error': 'El texto y el patrón no pueden estar vacíos'
            }), 400
        
        # Buscar el patrón
        result = selector.search_pattern(text, pattern)
        
        return jsonify({
            'success': True,
            'result': result
        })
        
    except Exception as e:
        return jsonify({
            'success': False,
            'error': f'Error en la búsqueda: {str(e)}'
        }), 500

@app.route('/api/debug', methods=['GET'])
def debug_info():
    """Endpoint de debugging para ver el estado del sistema"""
    try:
        import os
        debug_data = {
            'working_directory': os.getcwd(),
            'files_in_directory': os.listdir('.'),
            'base_file_exists': os.path.exists(BASE_FILE),
            'base_file_path': BASE_FILE,
            'upload_folder_exists': os.path.exists(UPLOAD_FOLDER),
            'combined_file_exists': os.path.exists(COMBINED_FILE),
            'patterns_count': len(cargar_todos_los_patrones()),
            'analyzer_patterns_count': len(analyzer.patterns) if hasattr(analyzer, 'patterns') else 'No disponible'
        }
        
        # Intentar leer las primeras líneas del archivo base
        if os.path.exists(BASE_FILE):
            try:
                with open(BASE_FILE, 'r', encoding='utf-8') as f:
                    debug_data['base_file_first_lines'] = f.readlines()[:3]
            except Exception as e:
                debug_data['base_file_read_error'] = str(e)
        
        return jsonify({'success': True, 'debug': debug_data})
    except Exception as e:
        return jsonify({'success': False, 'error': str(e)}), 500

@app.route('/api/patterns', methods=['GET'])
def get_patterns():
    try:
        patterns = cargar_todos_los_patrones()
        return jsonify({'success': True, 'patterns': patterns})
    except Exception as e:
        return jsonify({'success': False, 'error': f'Error al obtener patrones: {str(e)}'}), 500


@app.route('/api/patterns/reload', methods=['POST'])
def reload_patterns():
    """
    Recarga los patrones desde el archivo CSV.
    
    Response JSON:
    {
        "success": true,
        "message": "Patrones recargados exitosamente",
        "total_patterns": número_de_patrones
    }
    """
    try:
        generar_archivo_combinado()        
        analyzer.load_patterns()
        
        return jsonify({
            'success': True,
            'message': 'Patrones recargados exitosamente',
            'total_patterns': len(analyzer.patterns)
        })
        
    except Exception as e:
        return jsonify({
            'success': False,
            'error': f'Error al recargar patrones: {str(e)}'
        }), 500

@app.route('/api/test', methods=['GET'])
def test_api():
    """
    Endpoint de prueba para verificar que la API funciona.
    """
    return jsonify({
        'success': True,
        'message': 'API de SafeText funcionando correctamente',
        'version': '1.0.0',
        'algorithms': ['KMP', 'Boyer-Moore'],
        'total_patterns': len(analyzer.patterns)
    })

@app.route('/api/recommendations', methods=['POST'])
def get_recommendations():
    """
    Endpoint para obtener recomendaciones personalizadas basadas en el análisis
    """
    try:
        data = request.get_json()
        
        if not data:
            return jsonify({
                'success': False,
                'error': 'No se proporcionaron datos de análisis'
            }), 400
        
        # Validar que tenga la estructura básica del análisis
        if 'is_cyberbullying' not in data:
            return jsonify({
                'success': False,
                'error': 'Datos de análisis incompletos'
            }), 400
        
        # Generar recomendaciones usando el motor de recomendaciones
        recommendations_result = get_recommendations_for_analysis(data)
        
        if recommendations_result['success']:
            return jsonify({
                'success': True,
                'recommendation': recommendations_result['recommendation'],
                'generated_at': analyzer._get_timestamp()
            })
        else:
            return jsonify({
                'success': False,
                'error': recommendations_result.get('error', 'Error generando recomendaciones'),
                'fallback_recommendation': recommendations_result.get('recommendation')
            }), 500
            
    except Exception as e:
        print(f"Error en /api/recommendations: {e}")
        return jsonify({
            'success': False,
            'error': f'Error del servidor: {str(e)}'
        }), 500

@app.errorhandler(404)
def not_found(error):
    """Maneja errores 404."""
    return jsonify({
        'success': False,
        'error': 'Endpoint no encontrado'
    }), 404

@app.errorhandler(500)
def internal_error(error):
    """Maneja errores 500."""
    return jsonify({
        'success': False,
        'error': 'Error interno del servidor'
    }), 500

@app.route('/api/add-pattern', methods=['POST'])
def add_pattern():
    """
    Añade un nuevo patrón al archivo base y recarga los patrones en memoria.
    Espera un JSON con:
    {
        "id": "11",
        "frase": "nuevo patrón",
        "categorias": "Insulto",
        "nivel_gravedad": 50,
        "descripcion": "Descripción del patrón"
    }
    """
    try:
        data = request.get_json()

        # Validar campos requeridos
        required = ['id', 'frase', 'categorias', 'nivel_gravedad', 'descripcion']
        for campo in required:
            if campo not in data or data[campo] == '':
                return jsonify({'success': False, 'error': f'Campo faltante o vacío: {campo}'}), 400

        # Añadir al archivo base
        with open(BASE_FILE, 'a', newline='', encoding='utf-8') as f:
            writer = csv.writer(f)
            writer.writerow([
                data['id'],
                data['frase'],
                data['categorias'],
                data['nivel_gravedad'],
                data['descripcion']
            ])

        # Recargar en memoria       
        generar_archivo_combinado()
        analyzer.load_patterns()  # actualizar archivo combinado
        return jsonify({'success': True, 'message': 'Patrón añadido correctamente', 'total_patterns': len(analyzer.patterns)})

    except Exception as e:
        return jsonify({'success': False, 'error': f'Error al añadir patrón: {str(e)}'}), 500
if __name__ == '__main__':
    print("=" * 60)
    print("SafeText - Sistema de Detección de Ciberacoso")
    print("API Backend con algoritmos KMP y Boyer-Moore")
    print("Desarrollado por Harry Guajan y Joel Tinitana")
    print("EPN - Estructura de Datos y Algoritmos II")
    print("=" * 60)
    
    # Cargar patrones al iniciar
    print(f"Patrones cargados: {len(analyzer.patterns)}")
    
    # Iniciar servidor
    print("Iniciando servidor en http://localhost:5000")
    app.run(debug=True, host='0.0.0.0', port=5000)