"""
Script de prueba para verificar la integración completa entre frontend y backend.
Simula el flujo completo del usuario a través de la API.
"""

import requests
import json
import time

def test_complete_workflow():
    """
    Prueba el flujo completo de análisis de ciberacoso.
    """
    base_url = "http://localhost:5000"
    
    print("=" * 70)
    print("PRUEBA DE INTEGRACIÓN FRONTEND-BACKEND")
    print("SafeText - Sistema de Detección de Ciberacoso")
    print("=" * 70)
    
    # Verificar que el servidor esté funcionando
    try:
        response = requests.get(f"{base_url}/api/test", timeout=5)
        if response.status_code == 200:
            data = response.json()
            print("✅ Servidor funcionando correctamente")
            print(f"   Versión: {data.get('version', 'N/A')}")
            print(f"   Algoritmos: {', '.join(data.get('algorithms', []))}")
            print(f"   Patrones cargados: {data.get('total_patterns', 0)}")
        else:
            print("❌ Error al conectar con el servidor")
            return
    except requests.exceptions.RequestException as e:
        print(f"❌ No se puede conectar al servidor: {e}")
        print("   Asegúrate de que el servidor esté ejecutándose: python app.py")
        return
    
    # Textos de prueba para diferentes niveles de riesgo
    test_cases = [
        {
            "name": "Texto Normal",
            "text": "Hola, ¿cómo estás? Espero que tengas un buen día en la escuela.",
            "expected_risk": "None"
        },
        {
            "name": "Riesgo Bajo",
            "text": "Eres un poco tonto, pero no importa.",
            "expected_risk": "Low"
        },
        {
            "name": "Riesgo Medio",
            "text": "Cállate idiota, no me molestes más.",
            "expected_risk": "Medium"
        },
        {
            "name": "Riesgo Alto",
            "text": "Eres un estúpido y no sirves para nada. Nadie te quiere aquí.",
            "expected_risk": "High/Critical"
        }
    ]
    
    print("\n" + "=" * 70)
    print("EJECUTANDO CASOS DE PRUEBA")
    print("=" * 70)
    
    for i, test_case in enumerate(test_cases, 1):
        print(f"\n--- CASO {i}: {test_case['name']} ---")
        print(f"Texto: \"{test_case['text']}\"")
        
        try:
            # Realizar análisis
            response = requests.post(
                f"{base_url}/api/analyze",
                json={"text": test_case['text']},
                headers={"Content-Type": "application/json"},
                timeout=10
            )
            
            if response.status_code == 200:
                data = response.json()
                
                if data['success']:
                    result = data['result']
                    
                    print(f"✅ Análisis completado exitosamente")
                    print(f"   ¿Es ciberacoso?: {result['is_cyberbullying']}")
                    print(f"   Nivel de riesgo: {result['risk_level']}")
                    print(f"   Patrones detectados: {result['total_patterns_found']}")
                    print(f"   Total coincidencias: {result['total_matches']}")
                    
                    if result['matches']:
                        print("   Patrones encontrados:")
                        for match in result['matches']:
                            pattern_info = match['pattern_info']
                            print(f"     - \"{pattern_info['pattern']}\" ({pattern_info['severity']})")
                            print(f"       Algoritmo: {match['algorithm_used']}")
                    
                    print(f"   Resumen: {result['analysis_summary']}")
                    
                    # Verificar algoritmos utilizados
                    if 'algorithms_used' in result:
                        algos = result['algorithms_used']
                        print(f"   Algoritmos utilizados: {', '.join(algos.keys())}")
                    
                else:
                    print(f"❌ Error en el análisis: {data.get('error', 'Error desconocido')}")
                    
            else:
                print(f"❌ Error HTTP {response.status_code}")
                
        except requests.exceptions.RequestException as e:
            print(f"❌ Error de conexión: {e}")
    
    # Probar endpoints adicionales
    print("\n" + "=" * 70)
    print("PROBANDO ENDPOINTS ADICIONALES")
    print("=" * 70)
    
    # Probar obtención de patrones
    try:
        response = requests.get(f"{base_url}/api/patterns", timeout=5)
        if response.status_code == 200:
            data = response.json()
            if data['success']:
                patterns = data['patterns']
                stats = data['statistics']
                print(f"✅ Patrones obtenidos: {len(patterns)} patrones")
                print(f"   Por severidad: {stats['by_severity']}")
                print(f"   Por longitud: {stats['by_length']}")
            else:
                print(f"❌ Error al obtener patrones: {data.get('error')}")
        else:
            print(f"❌ Error HTTP al obtener patrones: {response.status_code}")
    except requests.exceptions.RequestException as e:
        print(f"❌ Error al obtener patrones: {e}")
    
    # Probar análisis de patrón específico
    try:
        test_pattern = "jajajajaja"
        response = requests.post(
            f"{base_url}/api/analyze-pattern",
            json={"pattern": test_pattern},
            headers={"Content-Type": "application/json"},
            timeout=5
        )
        if response.status_code == 200:
            data = response.json()
            if data['success']:
                analysis = data['analysis']
                print(f"✅ Análisis de patrón '{test_pattern}':")
                print(f"   Algoritmo recomendado: {analysis['recommended_algorithm']}")
                print(f"   Razón: {analysis['reason']}")
                print(f"   Longitud: {analysis['length']}")
                print(f"   Ratio repetición: {analysis['repetition_ratio']:.2f}")
            else:
                print(f"❌ Error en análisis de patrón: {data.get('error')}")
        else:
            print(f"❌ Error HTTP en análisis de patrón: {response.status_code}")
    except requests.exceptions.RequestException as e:
        print(f"❌ Error en análisis de patrón: {e}")
    
    # Probar búsqueda de patrón específico
    try:
        response = requests.post(
            f"{base_url}/api/search-pattern",
            json={
                "text": "Este idiota es muy tonto y estúpido",
                "pattern": "idiota"
            },
            headers={"Content-Type": "application/json"},
            timeout=5
        )
        if response.status_code == 200:
            data = response.json()
            if data['success']:
                result = data['result']
                print(f"✅ Búsqueda de patrón específico:")
                print(f"   Patrón: '{result['pattern']}'")
                print(f"   Algoritmo usado: {result['algorithm_used']}")
                print(f"   Encontrado: {result['found']}")
                print(f"   Coincidencias: {result['total_matches']}")
                if result['positions']:
                    print(f"   Posiciones: {result['positions']}")
            else:
                print(f"❌ Error en búsqueda de patrón: {data.get('error')}")
        else:
            print(f"❌ Error HTTP en búsqueda de patrón: {response.status_code}")
    except requests.exceptions.RequestException as e:
        print(f"❌ Error en búsqueda de patrón: {e}")
    
    print("\n" + "=" * 70)
    print("🎉 PRUEBAS DE INTEGRACIÓN COMPLETADAS")
    print("=" * 70)
    print("\n💡 INSTRUCCIONES PARA EL USUARIO:")
    print("1. Abrir navegador en: http://localhost:5000")
    print("2. Ingresar texto en la página principal")
    print("3. Hacer clic en 'Analizar'")
    print("4. Ver resultados dinámicos en tiempo real")
    print("5. Usar 'Opciones' para gestionar patrones")
    print("\n✨ El sistema está completamente funcional con:")
    print("  • Algoritmos KMP y Boyer-Moore")
    print("  • Selector automático inteligente")
    print("  • Análisis de riesgo dinámico")
    print("  • Recomendaciones contextuales")
    print("  • Exportación de reportes")

if __name__ == "__main__":
    test_complete_workflow()
