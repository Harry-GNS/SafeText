"""
Sistema de Recomendaciones Simplificado para SafeText
Solo 3 recomendaciones básicas según nivel de riesgo
"""

def get_recommendations_for_analysis(analysis_result):
    """
    Función simplificada para obtener recomendaciones básicas según el nivel de riesgo
    
    Args:
        analysis_result (dict): Resultado del análisis de ciberacoso
        
    Returns:
        dict: Respuesta con la recomendación según el nivel de riesgo
    """
    try:
        # Determinar nivel de riesgo
        is_cyberbullying = analysis_result.get('is_cyberbullying', False)
        risk_level = analysis_result.get('risk_level', 'Low')
        
        # 3 recomendaciones básicas según el nivel de riesgo
        if not is_cyberbullying or risk_level == 'Low':
            # SEGURO - Nivel bajo o sin ciberacoso
            recommendation = {
                "id": "safe_basic",
                "icon": "✅",
                "title": "Contenido Seguro",
                "description": "El texto analizado muestra una comunicación apropiada y respetuosa.",
                "action": "Continúe promoviendo este tipo de comunicación positiva en el entorno digital. Mantenga las buenas prácticas establecidas.",
                "priority": 1
            }
        elif risk_level == 'Medium':
            # MEDIO - Nivel medio de riesgo
            recommendation = {
                "id": "medium_basic",
                "icon": "⚠️",
                "title": "Atención Requerida",
                "description": "Se detectaron elementos que requieren supervisión moderada.",
                "action": "Implemente medidas preventivas como sesiones de educación sobre comunicación respetuosa. Monitoree la situación de cerca.",
                "priority": 2
            }
        else:
            # PELIGROSO - Nivel alto o muy alto
            recommendation = {
                "id": "danger_basic",
                "icon": "🚨",
                "title": "Situación Crítica",
                "description": "Se detectó contenido altamente problemático que requiere intervención inmediata.",
                "action": "Tome medidas urgentes: documente la evidencia, notifique a las autoridades competentes y proporcione apoyo inmediato a la víctima.",
                "priority": 1
            }
        
        return {
            "success": True,
            "recommendation": recommendation
        }
        
    except Exception as e:
        # Recomendación de respaldo
        fallback_recommendation = {
            "id": "fallback_basic",
            "icon": "📚",
            "title": "Educación y Prevención",
            "description": "La educación continua es la mejor herramienta para prevenir el ciberacoso.",
            "action": "Implemente programas de concientización sobre comunicación digital responsable y respeto en línea.",
            "priority": 1
        }
        
        return {
            "success": False,
            "error": str(e),
            "recommendation": fallback_recommendation
        }


if __name__ == "__main__":
    # Ejemplos de uso para testing
    print("=== PRUEBAS DE LOS 3 NIVELES ===\n")
    
    # Ejemplo 1: SEGURO
    test_safe = {'is_cyberbullying': False, 'risk_level': 'Low'}
    result_safe = get_recommendations_for_analysis(test_safe)
    print("🟢 NIVEL SEGURO:")
    print(f"   Título: {result_safe['recommendation']['title']}")
    print(f"   Icono: {result_safe['recommendation']['icon']}")
    print(f"   Descripción: {result_safe['recommendation']['description']}\n")
    
    # Ejemplo 2: MEDIO
    test_medium = {'is_cyberbullying': True, 'risk_level': 'Medium'}
    result_medium = get_recommendations_for_analysis(test_medium)
    print("🟡 NIVEL MEDIO:")
    print(f"   Título: {result_medium['recommendation']['title']}")
    print(f"   Icono: {result_medium['recommendation']['icon']}")
    print(f"   Descripción: {result_medium['recommendation']['description']}\n")
    
    # Ejemplo 3: PELIGROSO
    test_danger = {'is_cyberbullying': True, 'risk_level': 'High'}
    result_danger = get_recommendations_for_analysis(test_danger)
    print("🔴 NIVEL PELIGROSO:")
    print(f"   Título: {result_danger['recommendation']['title']}")
    print(f"   Icono: {result_danger['recommendation']['icon']}")
    print(f"   Descripción: {result_danger['recommendation']['description']}")
