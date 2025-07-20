"""
API Flask para el sistema de detección de ciberacoso.
Conecta el frontend con los algoritmos de backend.
"""

from flask import Flask, request, jsonify, render_template, send_from_directory
from flask_cors import CORS
import os
import sys

# Agregar el directorio actual al path
sys.path.append(os.path.dirname(os.path.abspath(__file__)))

from algorithms.analyzer import CyberbullyingAnalyzer
from algorithms.selector import AlgorithmSelector

app = Flask(__name__)
CORS(app)  # Permitir solicitudes desde el frontend

# Configuración
app.config['SECRET_KEY'] = 'safetext-cyberbullying-detection-2025'

# Inicializar el analizador
analyzer = CyberbullyingAnalyzer()
selector = AlgorithmSelector()

@app.route('/')
def index():
    """Redirige a la página principal del frontend."""
    return send_from_directory('templates', 'index.html')

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
    
    Request JSON:
    {
        "text": "Texto a analizar"
    }
    
    Response JSON:
    {
        "success": true,
        "result": { ... análisis completo ... }
    }
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
        
        # Realizar el análisis
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

@app.route('/api/patterns', methods=['GET'])
def get_patterns():
    """
    Obtiene todos los patrones cargados.
    
    Response JSON:
    {
        "success": true,
        "patterns": [ ... lista de patrones ... ],
        "statistics": { ... estadísticas ... }
    }
    """
    try:
        patterns = analyzer.patterns
        statistics = analyzer.get_pattern_statistics()
        
        return jsonify({
            'success': True,
            'patterns': patterns,
            'statistics': statistics
        })
        
    except Exception as e:
        return jsonify({
            'success': False,
            'error': f'Error al obtener patrones: {str(e)}'
        }), 500

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
