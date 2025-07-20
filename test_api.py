"""
Script de prueba para verificar el funcionamiento de la API sin iniciar el servidor web.
"""

import sys
import os
import json

# Agregar el directorio actual al path
sys.path.append(os.path.dirname(os.path.abspath(__file__)))

from algorithms.analyzer import CyberbullyingAnalyzer
from algorithms.selector import AlgorithmSelector

def test_api_functions():
    """
    Prueba las funciones principales que usa la API.
    """
    print("=" * 60)
    print("PRUEBA DE FUNCIONES DE LA API")
    print("=" * 60)
    
    # Inicializar componentes
    analyzer = CyberbullyingAnalyzer()
    selector = AlgorithmSelector()
    
    # Prueba 1: Análisis de texto completo
    print("\n1. ANÁLISIS DE TEXTO COMPLETO")
    print("-" * 40)
    text = "Eres un idiota y muy tonto. No sirves para nada."
    result = analyzer.analyze_text(text)
    
    print(f"Texto: {text}")
    print(f"¿Es ciberacoso?: {result['is_cyberbullying']}")
    print(f"Nivel de riesgo: {result['risk_level']}")
    print(f"Patrones encontrados: {result['total_patterns_found']}")
    print(f"Total coincidencias: {result['total_matches']}")
    
    # Prueba 2: Análisis de patrón específico
    print("\n2. ANÁLISIS DE PATRÓN ESPECÍFICO")
    print("-" * 40)
    pattern = "jajajajaja"
    analysis = selector.analyze_pattern(pattern)
    
    print(f"Patrón: {pattern}")
    print(f"Algoritmo recomendado: {analysis['recommended_algorithm']}")
    print(f"Razón: {analysis['reason']}")
    print(f"Longitud: {analysis['length']}")
    print(f"Ratio repetición: {analysis['repetition_ratio']:.2f}")
    
    # Prueba 3: Búsqueda de patrón específico
    print("\n3. BÚSQUEDA DE PATRÓN ESPECÍFICO")
    print("-" * 40)
    search_text = "Este idiota no sabe nada, es muy tonto"
    search_pattern = "idiota"
    search_result = selector.search_pattern(search_text, search_pattern)
    
    print(f"Texto: {search_text}")
    print(f"Patrón: {search_pattern}")
    print(f"Algoritmo usado: {search_result['algorithm_used']}")
    print(f"Encontrado: {search_result['found']}")
    print(f"Coincidencias: {search_result['total_matches']}")
    print(f"Posiciones: {search_result['positions']}")
    
    # Prueba 4: Estadísticas de patrones
    print("\n4. ESTADÍSTICAS DE PATRONES")
    print("-" * 40)
    stats = analyzer.get_pattern_statistics()
    
    print(f"Total patrones: {stats['total_patterns']}")
    print(f"Por severidad: {stats['by_severity']}")
    print(f"Por longitud: {stats['by_length']}")
    
    # Prueba 5: Formato JSON (simulando respuesta de API)
    print("\n5. FORMATO JSON DE RESPUESTA")
    print("-" * 40)
    api_response = {
        'success': True,
        'result': result
    }
    
    # Mostrar solo las primeras líneas del JSON para no saturar
    json_str = json.dumps(api_response, indent=2, ensure_ascii=False)
    lines = json_str.split('\n')
    for i, line in enumerate(lines[:15]):  # Mostrar solo las primeras 15 líneas
        print(line)
    if len(lines) > 15:
        print("... (JSON truncado)")
    
    print("\n" + "=" * 60)
    print("TODAS LAS PRUEBAS DE API COMPLETADAS")
    print("=" * 60)

def test_algorithm_performance():
    """
    Prueba el rendimiento de los algoritmos con diferentes tipos de patrones.
    """
    print("\n" + "=" * 60)
    print("PRUEBA DE RENDIMIENTO DE ALGORITMOS")
    print("=" * 60)
    
    selector = AlgorithmSelector()
    
    # Texto largo para pruebas
    long_text = "Este es un texto muy largo que contiene múltiples patrones. " * 50
    long_text += "Algunos pueden decir que eres idiota o tonto. "
    long_text += "Jajajaja qué divertido es esto. "
    long_text += "No sirves para nada en absoluto. "
    long_text += "Texto adicional para hacer la búsqueda más compleja. " * 20
    
    test_patterns = [
        ("idiota", "Patrón corto"),
        ("jajajaja", "Patrón repetitivo"),
        ("no sirves para nada", "Patrón largo"),
        ("este es un patrón muy largo sin muchas repeticiones", "Patrón muy largo"),
        ("aaaaaaaaaa", "Patrón muy repetitivo")
    ]
    
    print(f"Texto de prueba: {len(long_text)} caracteres")
    print("-" * 60)
    
    for pattern, description in test_patterns:
        analysis = selector.analyze_pattern(pattern)
        result = selector.search_pattern(long_text, pattern)
        
        print(f"\nPatrón: '{pattern}' ({description})")
        print(f"Algoritmo seleccionado: {analysis['recommended_algorithm']}")
        print(f"Razón de selección: {analysis['reason']}")
        print(f"Coincidencias encontradas: {result['total_matches']}")
        if result['found']:
            print(f"Posiciones: {result['positions']}")

if __name__ == "__main__":
    print("SISTEMA DE DETECCIÓN DE CIBERACOSO")
    print("Prueba de Funciones de API")
    print("Desarrollado por Harry Guajan y Joel Tinitana")
    print("EPN - Estructura de Datos y Algoritmos II")
    
    try:
        test_api_functions()
        test_algorithm_performance()
        
        print("\n🎉 TODAS LAS PRUEBAS COMPLETADAS EXITOSAMENTE 🎉")
        print("\nEl backend está listo para:")
        print("✓ Detectar patrones de ciberacoso")
        print("✓ Seleccionar automáticamente entre KMP y Boyer-Moore")
        print("✓ Proporcionar análisis detallados")
        print("✓ Servir respuestas JSON para el frontend")
        
    except Exception as e:
        print(f"\n❌ Error durante las pruebas: {e}")
        import traceback
        traceback.print_exc()
