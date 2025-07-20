"""
Test rápido para verificar la nueva visualización de patrones resaltados.
"""

import sys
import os
sys.path.append(os.path.dirname(os.path.abspath(__file__)))

from algorithms.analyzer import CyberbullyingAnalyzer

def test_highlighted_patterns():
    """
    Prueba la funcionalidad con diferentes textos.
    """
    analyzer = CyberbullyingAnalyzer()
    
    casos_prueba = [
        {
            'nombre': 'Texto Simple con Pocos Patrones',
            'texto': 'Hola Juan, no seas tonto. Eso que dices es correcto.'
        },
        {
            'nombre': 'Texto con Múltiples Patrones',
            'texto': 'Eres un idiota y estúpido. No sirves para nada, mejor cállate de una vez.'
        },
        {
            'nombre': 'Texto Crítico',
            'texto': 'Eres un inútil, nadie te quiere. Vete a morir, te voy a pegar si sigues hablando.'
        }
    ]
    
    print("=" * 80)
    print("TEST: VISUALIZACIÓN DE PATRONES RESALTADOS")
    print("=" * 80)
    
    for i, caso in enumerate(casos_prueba, 1):
        print(f"\n{i}. {caso['nombre'].upper()}")
        print("-" * 60)
        print(f"Texto original: '{caso['texto']}'")
        
        # Analizar
        resultado = analyzer.analyze_text(caso['texto'])
        
        print(f"\nResultados:")
        print(f"- Patrones encontrados: {resultado['total_patterns_found']}")
        print(f"- Coincidencias totales: {resultado['total_matches']}")
        print(f"- Nivel de riesgo: {resultado['risk_level']}")
        
        if resultado['matches']:
            print(f"\nPatrones detectados:")
            for match in resultado['matches']:
                pattern_info = match['pattern_info']
                print(f"  • '{pattern_info['pattern']}' ({pattern_info['severity']}) en posiciones: {match['positions']}")
                print(f"    Categoría: {pattern_info['category']}")
                print(f"    Algoritmo: {match['algorithm_used']}")
        
        # Simular la función de resaltado
        texto_resaltado = simular_resaltado(caso['texto'], resultado['matches'])
        print(f"\nTexto con patrones resaltados (simulado):")
        print(f"'{texto_resaltado}'")
        
        print("\n" + "=" * 80)

def simular_resaltado(texto, matches):
    """
    Simula cómo se vería el texto con los patrones resaltados.
    """
    if not matches:
        return f"✅ {texto} (Sin patrones detectados)"
    
    # Crear lista de todas las posiciones a resaltar
    destacados = []
    for match in matches:
        pattern = match['pattern_info']['pattern']
        severity = match['pattern_info']['severity']
        for pos in match['positions']:
            destacados.append({
                'start': pos,
                'end': pos + len(pattern),
                'pattern': pattern,
                'severity': severity
            })
    
    # Ordenar por posición (de mayor a menor)
    destacados.sort(key=lambda x: x['start'], reverse=True)
    
    # Aplicar formato
    texto_resultado = texto
    for item in destacados:
        before = texto_resultado[:item['start']]
        highlighted = texto_resultado[item['start']:item['end']]
        after = texto_resultado[item['end']:]
        
        # Simular el resaltado con símbolos
        if item['severity'] == 'Critical':
            formato = f"🚨[{highlighted}]🚨"
        elif item['severity'] == 'High':
            formato = f"⚠️[{highlighted}]⚠️"
        elif item['severity'] == 'Medium':
            formato = f"🟡[{highlighted}]🟡"
        else:
            formato = f"🔵[{highlighted}]🔵"
        
        texto_resultado = before + formato + after
    
    return texto_resultado

if __name__ == '__main__':
    test_highlighted_patterns()
