"""
Demostración de cómo se calculan los porcentajes de seguridad en SafeText.
Muestra el proceso completo desde patrones hasta porcentajes finales.
"""

import sys
import os
sys.path.append(os.path.dirname(os.path.abspath(__file__)))

from algorithms.analyzer import CyberbullyingAnalyzer

def demo_safety_calculation():
    """
    Demuestra cómo se calculan los porcentajes de seguridad.
    """
    analyzer = CyberbullyingAnalyzer()
    
    # Casos de prueba con diferentes niveles de severidad
    casos_prueba = [
        {
            'nombre': 'Contenido Completamente Seguro',
            'texto': 'Hola, ¿cómo estás? Espero que tengas un buen día. Nos vemos mañana en clase.'
        },
        {
            'nombre': 'Riesgo Bajo - Insulto Leve',
            'texto': 'No seas tonto, eso no es así. Pero bueno, todos nos equivocamos.'
        },
        {
            'nombre': 'Riesgo Medio - Varios Insultos',
            'texto': 'Eres un idiota y estúpido. No entiendes nada. Mejor cállate.'
        },
        {
            'nombre': 'Riesgo Alto - Insultos Graves',
            'texto': 'Eres un inútil, no sirves para nada. Nadie te quiere aquí. Eres patético.'
        },
        {
            'nombre': 'Riesgo Crítico - Amenazas',
            'texto': 'Eres un inútil, no sirves para nada. Vete a morir. Te voy a pegar si no te callas.'
        }
    ]
    
    print("=" * 100)
    print("DEMOSTRACIÓN: CÁLCULO DE PORCENTAJES DE SEGURIDAD")
    print("=" * 100)
    
    for i, caso in enumerate(casos_prueba, 1):
        print(f"\n{i}. {caso['nombre'].upper()}")
        print("-" * 80)
        print(f"Texto: '{caso['texto']}'")
        
        # Realizar análisis
        resultado = analyzer.analyze_text(caso['texto'])
        
        print(f"\n📊 RESULTADOS DEL ANÁLISIS:")
        print(f"   • Es ciberacoso: {resultado['is_cyberbullying']}")
        print(f"   • Nivel de riesgo: {resultado['risk_level']}")
        print(f"   • Patrones detectados: {resultado['total_patterns_found']}")
        print(f"   • Total coincidencias: {resultado['total_matches']}")
        
        # Mostrar distribución de severidad
        if resultado['severity_summary']:
            print(f"\n🎯 DISTRIBUCIÓN DE SEVERIDAD:")
            for severity, count in resultado['severity_summary'].items():
                if count > 0:
                    print(f"   • {severity}: {count} coincidencia(s)")
        
        # Calcular y mostrar porcentajes
        porcentajes = calcular_porcentajes_seguridad(resultado)
        
        print(f"\n📈 PORCENTAJES DE SEGURIDAD:")
        print(f"   🟢 Contenido Seguro: {porcentajes['seguro']}%")
        print(f"   🟡 Contenido Sospechoso: {porcentajes['sospechoso']}%")
        print(f"   🔴 Contenido Peligroso: {porcentajes['peligroso']}%")
        
        # Explicar el cálculo
        print(f"\n🧮 EXPLICACIÓN DEL CÁLCULO:")
        if not resultado['is_cyberbullying']:
            print("   → Sin ciberacoso detectado = 100% seguro")
        else:
            print(f"   → Nivel de riesgo '{resultado['risk_level']}' determina la distribución:")
            explicar_calculo_porcentajes(resultado['risk_level'])
        
        print("\n" + "=" * 100)

def calcular_porcentajes_seguridad(resultado):
    """
    Replica la lógica del frontend para calcular porcentajes.
    """
    if not resultado['is_cyberbullying']:
        return {'seguro': 100, 'sospechoso': 0, 'peligroso': 0}
    
    # Lógica basada en el nivel de riesgo (del archivo resultados.html)
    nivel_riesgo = resultado['risk_level']
    
    if nivel_riesgo == 'Low':
        return {'seguro': 70, 'sospechoso': 30, 'peligroso': 0}
    elif nivel_riesgo == 'Medium':
        return {'seguro': 50, 'sospechoso': 40, 'peligroso': 10}
    elif nivel_riesgo == 'High':
        return {'seguro': 30, 'sospechoso': 30, 'peligroso': 40}
    elif nivel_riesgo == 'Critical':
        return {'seguro': 10, 'sospechoso': 20, 'peligroso': 70}
    else:
        return {'seguro': 90, 'sospechoso': 10, 'peligroso': 0}

def explicar_calculo_porcentajes(nivel_riesgo):
    """
    Explica cómo se determinan los porcentajes para cada nivel.
    """
    explicaciones = {
        'Low': """
        • Riesgo Bajo: Insultos leves detectados
        • 70% Seguro: La mayor parte del contenido es apropiado
        • 30% Sospechoso: Algunos elementos requieren atención
        • 0% Peligroso: Sin contenido altamente dañino
        """,
        'Medium': """
        • Riesgo Medio: Múltiples insultos o contenido moderadamente agresivo
        • 50% Seguro: Mitad del contenido es problemático
        • 40% Sospechoso: Contenido que requiere intervención
        • 10% Peligroso: Algunos elementos dañinos presentes
        """,
        'High': """
        • Riesgo Alto: Insultos graves, exclusión social, ataques personales
        • 30% Seguro: Mayoría del contenido es problemático
        • 30% Sospechoso: Contenido ambiguo que necesita revisión
        • 40% Peligroso: Gran cantidad de contenido dañino
        """,
        'Critical': """
        • Riesgo Crítico: Amenazas, deseos de muerte, violencia
        • 10% Seguro: Muy poco contenido apropiado
        • 20% Sospechoso: Contenido menor comparado con lo grave
        • 70% Peligroso: Mayoría del contenido es extremadamente dañino
        """
    }
    
    print(explicaciones.get(nivel_riesgo, "Nivel no reconocido"))

def demo_scoring_algorithm():
    """
    Demuestra cómo funciona el algoritmo de puntuación ponderada.
    """
    print("\n" + "=" * 100)
    print("ALGORITMO DE PUNTUACIÓN PONDERADA")
    print("=" * 100)
    
    # Pesos del sistema (del analyzer.py)
    pesos = {'Low': 1, 'Medium': 3, 'High': 7, 'Critical': 15}
    
    print("🔢 SISTEMA DE PESOS:")
    for severity, peso in pesos.items():
        print(f"   • {severity}: {peso} puntos")
    
    print("\n📋 UMBRALES DE CLASIFICACIÓN:")
    print("   • 0-2 puntos → Riesgo LOW")
    print("   • 3-6 puntos → Riesgo MEDIUM") 
    print("   • 7-14 puntos → Riesgo HIGH")
    print("   • 15+ puntos → Riesgo CRITICAL")
    
    # Ejemplos de cálculo
    ejemplos = [
        {'Low': 2, 'Medium': 0, 'High': 0, 'Critical': 0},  # 2 puntos = Low
        {'Low': 0, 'Medium': 2, 'High': 0, 'Critical': 0},  # 6 puntos = Medium
        {'Low': 1, 'Medium': 1, 'High': 1, 'Critical': 0},  # 11 puntos = High
        {'Low': 0, 'Medium': 0, 'High': 0, 'Critical': 1},  # 15 puntos = Critical
    ]
    
    print("\n🧮 EJEMPLOS DE CÁLCULO:")
    for i, ejemplo in enumerate(ejemplos, 1):
        total = sum(ejemplo[severity] * pesos[severity] for severity in pesos)
        
        print(f"\nEjemplo {i}:")
        print("   Detecciones:", end=" ")
        for severity, count in ejemplo.items():
            if count > 0:
                print(f"{count}x{severity}({pesos[severity]}pts)", end=" ")
        
        print(f"\n   Cálculo: {' + '.join(f'{count}×{pesos[severity]}' for severity, count in ejemplo.items() if count > 0)} = {total} puntos")
        
        # Determinar clasificación
        if total >= 15:
            clasificacion = 'CRITICAL'
        elif total >= 7:
            clasificacion = 'HIGH'
        elif total >= 3:
            clasificacion = 'MEDIUM'
        else:
            clasificacion = 'LOW'
        
        print(f"   Resultado: {total} puntos → Riesgo {clasificacion}")

if __name__ == '__main__':
    demo_safety_calculation()
    demo_scoring_algorithm()
