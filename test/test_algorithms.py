"""
Script de prueba para los algoritmos de detección de ciberacoso.
Demuestra el funcionamiento de KMP, Boyer-Moore y el selector automático.
"""

import sys
import os

# Agregar el directorio padre al path para importar los módulos
sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

from algorithms.analyzer import CyberbullyingAnalyzer
from algorithms.selector import AlgorithmSelector
from algorithms.kmp import KMPAlgorithm
from algorithms.boyer_moore import BoyerMooreAlgorithm

def test_individual_algorithms():
    """
    Prueba los algoritmos KMP y Boyer-Moore individualmente.
    """
    print("=" * 60)
    print("PRUEBA DE ALGORITMOS INDIVIDUALES")
    print("=" * 60)
    
    # Texto de prueba
    text = "Hola idiota, eres muy tonto y estúpido. Jajajaja qué loser eres. Cállate mejor."
    
    # Patrones de prueba
    patterns = ["idiota", "jajajaja", "muy estúpido y tonto", "xyz"]
    
    kmp = KMPAlgorithm()
    boyer_moore = BoyerMooreAlgorithm()
    
    for pattern in patterns:
        print(f"\nBuscando patrón: '{pattern}'")
        print(f"Longitud del patrón: {len(pattern)} caracteres")
        print("-" * 40)
        
        # KMP
        kmp_result = kmp.find_pattern_info(text, pattern)
        print(f"KMP encontró: {kmp_result['total_matches']} coincidencias")
        if kmp_result['found']:
            print(f"Posiciones KMP: {kmp_result['positions']}")
        
        # Boyer-Moore
        bm_result = boyer_moore.find_pattern_info(text, pattern)
        print(f"Boyer-Moore encontró: {bm_result['total_matches']} coincidencias")
        if bm_result['found']:
            print(f"Posiciones Boyer-Moore: {bm_result['positions']}")
        
        # Verificar que ambos algoritmos dan el mismo resultado
        if kmp_result['positions'] == bm_result['positions']:
            print("✓ Ambos algoritmos coinciden")
        else:
            print("✗ Los algoritmos NO coinciden")

def test_algorithm_selector():
    """
    Prueba el selector automático de algoritmos.
    """
    print("\n" + "=" * 60)
    print("PRUEBA DEL SELECTOR AUTOMÁTICO")
    print("=" * 60)
    
    selector = AlgorithmSelector()
    
    # Patrones de prueba con diferentes características
    test_patterns = [
        "hola",              # Corto
        "jajajaja",          # Repetitivo
        "jejejejeje",        # Muy repetitivo
        "cállate idiota",    # Mediano
        "esto es un patrón muy largo sin repeticiones", # Largo sin repeticiones
        "abcdefghijklmnop",  # Largo sin repeticiones
        "aaaaaa",            # Repetitivo
        ""                   # Vacío
    ]
    
    for pattern in test_patterns:
        analysis = selector.analyze_pattern(pattern)
        print(f"\nPatrón: '{pattern}'")
        print(f"Longitud: {analysis['length']}")
        print(f"Ratio de repetición: {analysis['repetition_ratio']:.2f}")
        print(f"Tiene repeticiones: {analysis['has_repetitions']}")
        print(f"Algoritmo recomendado: {analysis['recommended_algorithm']}")
        print(f"Razón: {analysis['reason']}")

def test_cyberbullying_analyzer():
    """
    Prueba el analizador completo de ciberacoso.
    """
    print("\n" + "=" * 60)
    print("PRUEBA DEL ANALIZADOR DE CIBERACOSO")
    print("=" * 60)
    
    analyzer = CyberbullyingAnalyzer()
    
    # Textos de prueba
    test_texts = [
        "Hola, ¿cómo estás? Espero que tengas un buen día.",
        "Eres un idiota y muy tonto. Nadie te quiere aquí.",
        "Jajajaja qué loser eres. Cállate mejor y vete.",
        "Estúpido, no sirves para nada. Mejor muérete.",
        "¿Podrías ayudarme con esta tarea? Gracias."
    ]
    
    for i, text in enumerate(test_texts, 1):
        print(f"\n--- TEXTO {i} ---")
        print(f"Texto: {text}")
        print("-" * 40)
        
        result = analyzer.analyze_text(text)
        
        print(f"¿Es ciberacoso?: {result['is_cyberbullying']}")
        print(f"Nivel de riesgo: {result['risk_level']}")
        print(f"Total de patrones encontrados: {result['total_patterns_found']}")
        print(f"Total de coincidencias: {result['total_matches']}")
        
        if result['matches']:
            print("Patrones detectados:")
            for match in result['matches']:
                pattern_info = match['pattern_info']
                print(f"  - '{pattern_info['pattern']}' ({pattern_info['category']}, {pattern_info['severity']})")
                print(f"    Algoritmo usado: {match['algorithm_used']}")
                print(f"    Coincidencias: {match['total_matches']}")
        
        print(f"Resumen: {result['analysis_summary']}")

def test_pattern_statistics():
    """
    Prueba las estadísticas de patrones.
    """
    print("\n" + "=" * 60)
    print("ESTADÍSTICAS DE PATRONES")
    print("=" * 60)
    
    analyzer = CyberbullyingAnalyzer()
    stats = analyzer.get_pattern_statistics()
    
    print(f"Total de patrones: {stats['total_patterns']}")
    print(f"\nPor categoría:")
    for category, count in stats['by_category'].items():
        print(f"  {category}: {count}")
    
    print(f"\nPor severidad:")
    for severity, count in stats['by_severity'].items():
        print(f"  {severity}: {count}")
    
    print(f"\nPor longitud:")
    for length_type, count in stats['by_length'].items():
        print(f"  {length_type}: {count}")

if __name__ == "__main__":
    print("SISTEMA DE DETECCIÓN DE CIBERACOSO")
    print("Prueba de Algoritmos KMP y Boyer-Moore")
    print("Desarrollado por Harry Guajan y Joel Tinitana")
    print("EPN - Estructura de Datos y Algoritmos II")
    
    try:
        test_individual_algorithms()
        test_algorithm_selector()
        test_cyberbullying_analyzer()
        test_pattern_statistics()
        
        print("\n" + "=" * 60)
        print("TODAS LAS PRUEBAS COMPLETADAS EXITOSAMENTE")
        print("=" * 60)
        
    except Exception as e:
        print(f"\nError durante las pruebas: {e}")
        import traceback
        traceback.print_exc()
