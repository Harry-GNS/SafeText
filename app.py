"""
API Flask para el sistema de detección de ciberacoso.
Conecta el frontend con los algoritmos de backend.
"""

from flask import Flask, request, jsonify, send_from_directory
from flask_cors import CORS
import os
import sys
import time
from werkzeug.utils import secure_filename
import csv

# Agregar el directorio actual al path
sys.path.append(os.path.dirname(os.path.abspath(__file__)))

from algorithms.analyzer import CyberbullyingAnalyzer
from algorithms.selector import AlgorithmSelector

app = Flask(__name__)
CORS(app)

# ---------------- CONFIG ----------------
app.config['SECRET_KEY'] = 'safetext-cyberbullying-detection-2025'
UPLOAD_FOLDER = os.path.join(os.getcwd(), 'uploads')
os.makedirs(UPLOAD_FOLDER, exist_ok=True)

ALLOWED_EXTENSIONS = {'csv', 'txt'}
TIEMPO_MAXIMO = 86400  # 24h
MAX_FILES = 5          # máximo de archivos en uploads
BASE_FILE = 'patrones.csv'

# ---------------- FUNCIONES AUXILIARES ----------------
def allowed_file(filename):
    return '.' in filename and filename.rsplit('.', 1)[1].lower() in ALLOWED_EXTENSIONS

def limpiar_archivos():
    ahora = time.time()
    for archivo in os.listdir(UPLOAD_FOLDER):
        ruta = os.path.join(UPLOAD_FOLDER, archivo)
        if os.path.isfile(ruta):
            edad = ahora - os.path.getctime(ruta)
            if edad > TIEMPO_MAXIMO:
                os.remove(ruta)
                print(f"[Limpieza] Archivo eliminado por antigüedad: {archivo}")

def cargar_todos_los_patrones():
    patrones_totales = []
    # base
    base_path = os.path.join(os.getcwd(), BASE_FILE)
    if os.path.exists(base_path):
        with open(base_path, 'r', encoding='utf-8') as f:
            reader = csv.DictReader(f)
            for row in reader:
                patrones_totales.append({
                    'id': row.get('id', ''),
                    'pattern': row.get('frase', ''),
                    'category': row.get('categorias', ''),
                    'severity': row.get('nivel_gravedad', ''),
                    'description': row.get('descripcion', '')
                })
    # uploads
    for archivo in os.listdir(UPLOAD_FOLDER):
        ruta = os.path.join(UPLOAD_FOLDER, archivo)
        if os.path.isfile(ruta) and allowed_file(archivo):
            try:
                with open(ruta, 'r', encoding='utf-8') as f:
                    reader = csv.DictReader(f)
                    for row in reader:
                        patrones_totales.append({
                            'id': row.get('id', ''),
                            'pattern': row.get('frase', ''),
                            'category': row.get('categorias', ''),
                            'severity': row.get('nivel_gravedad', ''),
                            'description': row.get('descripcion', '')
                        })
            except Exception as e:
                print(f"[Error leyendo {archivo}] {e}")
    return patrones_totales

# ---------------- INICIALIZAR ----------------
analyzer = CyberbullyingAnalyzer()
selector = AlgorithmSelector()

# ---------------- RUTAS PÁGINAS ----------------
@app.route('/')
def index():
    return send_from_directory('templates', 'index.html')

@app.route('/index.html')
def index_page():
    return send_from_directory('templates', 'index.html')

@app.route('/config.html')
def config_page():
    return send_from_directory('templates', 'config.html')

@app.route('/resultados.html')
def results_page():
    return send_from_directory('templates', 'resultados.html')

@app.route('/templates/<path:filename>')
def serve_templates(filename):
    return send_from_directory('templates', filename)

@app.route('/static/<path:filename>')
def serve_static(filename):
    return send_from_directory('static', filename)

# ---------------- API PRINCIPAL ----------------
@app.route('/api/patterns', methods=['GET'])
def get_patterns():
    try:
        patterns = cargar_todos_los_patrones()
        return jsonify({'success': True, 'patterns': patterns})
    except Exception as e:
        return jsonify({'success': False, 'error': f'Error al obtener patrones: {str(e)}'}), 500

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

            return jsonify({'success': True, 'message': f'{filename} subido correctamente.'})
        else:
            return jsonify({'success': False, 'error': 'Formato no permitido (solo .csv o .txt)'}), 400
    except Exception as e:
        return jsonify({'success': False, 'error': f'Error al subir archivo: {str(e)}'}), 500

@app.route('/api/list-files', methods=['GET'])
def list_files():
    try:
        files = []
        # base
        base_path = os.path.join(os.getcwd(), BASE_FILE)
        if os.path.exists(base_path):
            size = os.path.getsize(base_path) // 1024
            files.append({'name': BASE_FILE, 'size': size, 'protected': True})
        # uploads
        for archivo in os.listdir(UPLOAD_FOLDER):
            ruta = os.path.join(UPLOAD_FOLDER, archivo)
            if os.path.isfile(ruta):
                size = os.path.getsize(ruta) // 1024
                files.append({'name': archivo, 'size': size, 'protected': False})
        return jsonify({'success': True, 'files': files})
    except Exception as e:
        return jsonify({'success': False, 'error': f'No se pudieron listar los archivos: {str(e)}'}), 500

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
            return jsonify({'success': True, 'message': f'{filename} eliminado correctamente'})
        else:
            return jsonify({'success': False, 'error': 'El archivo no existe'}), 400
    except Exception as e:
        return jsonify({'success': False, 'error': f'Error al eliminar archivo: {str(e)}'}), 500

# ---------------- MAIN ----------------
if __name__ == '__main__':
    print("=" * 60)
    print("SafeText - Sistema de Detección de Ciberacoso")
    print("API Backend con algoritmos KMP y Boyer-Moore")
    print("Desarrollado por Harry Guajan y Joel Tinitana")
    print("EPN - Estructura de Datos y Algoritmos II")
    print("=" * 60)
    print(f"Patrones cargados: {len(analyzer.patterns)}")
    limpiar_archivos()
    print("Iniciando servidor en http://localhost:5000")
    app.run(debug=True, host='0.0.0.0', port=5000)
