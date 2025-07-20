"""
Demostración de cómo el selector elige algoritmos para los patrones del CSV.
"""

import sys
import os
sys.path.append(os.path.dirname(os.path.abspath(__file__)))

from algorithms.selector import AlgorithmSelector
#Harry comit
def demo_algorithm_selection():
    """
    Demuestra cómo el selector elige algoritmos para cada patrón.
    """
    selector = AlgorithmSelector()
    
    # Patrones de tu CSV
    patrones_csv = [
        "eres un inútil",
        "no sirves para nada", 
        "cállate de una vez",
        "ese tipo me da asco",
        "idiota",
        "estúpido", 
        "tonto",
        "feo",
        "gordo",
        "perdedor",
        "fracasado",
        "nadie te quiere",
        "vete a morir",
        "te voy a pegar",
        "déjame en paz",
        "no me hables", 
        "eres patético",
        "qué asco",
        "me das pena",
        "eres un monstruo"
    ]
    
    print("=" * 80)
    print("ANÁLISIS DE SELECCIÓN DE ALGORITMOS PARA CADA PATRÓN")
    print("=" * 80)
    print(f"{'Patrón':<25} {'Longitud':<8} {'Algoritmo':<12} {'Razón'}")
    print("-" * 80)
    
    kmp_count = 0
    boyer_moore_count = 0
    
    for pattern in patrones_csv:
        analysis = selector.analyze_pattern(pattern)
        algorithm = analysis['recommended_algorithm']
        reason = analysis['reason']
        length = analysis['length']
        
        if algorithm == 'KMP':
            kmp_count += 1
        else:
            boyer_moore_count += 1
        
        print(f"{pattern:<25} {length:<8} {algorithm:<12} {reason}")
    
    print("-" * 80)
    print(f"RESUMEN:")
    print(f"- Patrones que usan KMP: {kmp_count}")
    print(f"- Patrones que usan Boyer-Moore: {boyer_moore_count}")
    print(f"- Total de patrones: {len(patrones_csv)}")
    
    # Ejemplo de búsqueda en texto grande
    print("\n" + "=" * 80)
    print("EJEMPLO DE BÚSQUEDA EN TEXTO GRANDE")
    print("=" * 80)
    
    texto_ejemplo = """
    Hola Juan, ¿cómo estás? He notado que últimamente has estado muy callado en clase.
    Ayer escuché a algunos compañeros decirte cosas como 'eres un inútil' y 'no sirves para nada'.
    También vi que te dijeron 'cállate de una vez' cuando intentaste participar.
    Esto no está bien, nadie debe decirte que 'eres patético' o que 'nadie te quiere'.
    Si alguien te dice 'vete a morir' o 'te voy a pegar', debes reportarlo inmediatamente.
    Recuerda que eres valioso y que estos comentarios como 'idiota' o 'estúpido' no te definen.
    """
    
    print(f"Texto a analizar ({len(texto_ejemplo)} caracteres):")
    print(f"'{texto_ejemplo[:100]}...'")
    print()
    
    matches_found = []
    algorithms_used = {}
    
    for pattern in patrones_csv:
        result = selector.search_pattern(texto_ejemplo, pattern)
        
        if result['found']:
            matches_found.append({
                'pattern': pattern,
                'algorithm': result['algorithm_used'],
                'matches': result['total_matches'],
                'positions': result['positions']
            })
            
            algo = result['algorithm_used']
            algorithms_used[algo] = algorithms_used.get(algo, 0) + 1
    
    print("PATRONES ENCONTRADOS:")
    print("-" * 50)
    for match in matches_found:
        print(f"Patrón: '{match['pattern']}'")
        print(f"  Algoritmo usado: {match['algorithm']}")
        print(f"  Coincidencias: {match['matches']}")
        print(f"  Posiciones: {match['positions']}")
        print()
    
    print("ESTADÍSTICAS DE ALGORITMOS USADOS:")
    print("-" * 40)
    for algo, count in algorithms_used.items():
        print(f"- {algo}: {count} patrones encontrados")

if __name__ == '__main__':
    demo_algorithm_selection()
