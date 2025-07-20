"""
Script simple para probar la API directamente sin interferencia de caracteres especiales.
"""

import requests
import json

def test_api_simple():
    base_url = "http://localhost:5000"
    
    print("🔧 PRUEBA SIMPLE DE API")
    print("=" * 50)
    
    # Probar endpoint de test
    try:
        response = requests.get(f"{base_url}/api/test")
        print(f"GET /api/test - Status: {response.status_code}")
        if response.status_code == 200:
            data = response.json()
            print(f"✅ API funcionando - Patrones: {data.get('total_patterns', 0)}")
        else:
            print(f"❌ Error: {response.text}")
    except Exception as e:
        print(f"❌ Error de conexión: {e}")
    
    # Probar análisis de texto
    try:
        test_text = "Eres un idiota"
        response = requests.post(
            f"{base_url}/api/analyze",
            json={"text": test_text},
            headers={"Content-Type": "application/json"}
        )
        print(f"\nPOST /api/analyze - Status: {response.status_code}")
        if response.status_code == 200:
            data = response.json()
            if data.get('success'):
                result = data['result']
                print(f"✅ Análisis exitoso")
                print(f"   Ciberacoso: {result['is_cyberbullying']}")
                print(f"   Riesgo: {result['risk_level']}")
                print(f"   Patrones: {result['total_patterns_found']}")
            else:
                print(f"❌ Error en análisis: {data.get('error')}")
        else:
            print(f"❌ Error HTTP: {response.text}")
    except Exception as e:
        print(f"❌ Error: {e}")
    
    # Verificar páginas HTML
    html_pages = ['/', '/index.html', '/config.html', '/resultados.html']
    print(f"\n📄 VERIFICANDO PÁGINAS HTML")
    print("-" * 30)
    
    for page in html_pages:
        try:
            response = requests.get(f"{base_url}{page}")
            status_icon = "✅" if response.status_code == 200 else "❌"
            print(f"{status_icon} {page} - Status: {response.status_code}")
        except Exception as e:
            print(f"❌ {page} - Error: {e}")

if __name__ == "__main__":
    test_api_simple()
