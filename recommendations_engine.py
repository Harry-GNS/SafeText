"""
Sistema de Recomendaciones Inteligentes para SafeText
Generador de recomendaciones personalizadas basadas en el análisis de ciberacoso
"""

class RecommendationsEngine:
    def __init__(self):
        self.recommendations_bank = {
            # Recomendaciones para contenido seguro
            "safe": [
                {
                    "id": "safe_001",
                    "icon": "✅",
                    "title": "Contenido Apropiado Detectado",
                    "description": "El texto analizado muestra una comunicación respetuosa y apropiada.",
                    "action": "Continúe promoviendo este tipo de comunicación positiva en el entorno digital.",
                    "priority": 1
                },
                {
                    "id": "safe_002", 
                    "icon": "🛡️",
                    "title": "Ambiente Digital Saludable",
                    "description": "No se detectaron signos de hostigamiento o intimidación.",
                    "action": "Mantenga las buenas prácticas de comunicación establecidas y fomente el respeto mutuo.",
                    "priority": 1
                },
                {
                    "id": "safe_003",
                    "icon": "📚",
                    "title": "Prevención Continua",
                    "description": "Aunque el contenido es seguro, la prevención es clave.",
                    "action": "Implemente programas regulares de concientización sobre ciberacoso y comunicación digital responsable.",
                    "priority": 2
                }
            ],
            
            # Recomendaciones por categorías de patrones
            "categories": {
                "Insultos y Ofensas": [
                    {
                        "id": "insult_001",
                        "icon": "⚠️",
                        "title": "Lenguaje Ofensivo Detectado",
                        "description": "Se han identificado insultos o palabras ofensivas en el texto.",
                        "action": "Implemente sesiones de educación sobre comunicación respetuosa y establezca consecuencias claras para el lenguaje inapropiado.",
                        "priority": 2
                    },
                    {
                        "id": "insult_002",
                        "icon": "💬",
                        "title": "Intervención Comunicativa",
                        "description": "El uso de insultos puede escalar a formas más severas de acoso.",
                        "action": "Facilite un diálogo constructivo entre las partes involucradas para resolver conflictos de manera pacífica.",
                        "priority": 1
                    }
                ],
                "Amenazas": [
                    {
                        "id": "threat_001",
                        "icon": "🚨",
                        "title": "Amenazas Identificadas - Acción Inmediata",
                        "description": "Se detectaron amenazas que requieren intervención urgente.",
                        "action": "Contacte inmediatamente a las autoridades escolares y considere involucrar a los padres o tutores.",
                        "priority": 1
                    },
                    {
                        "id": "threat_002",
                        "icon": "📋",
                        "title": "Documentación de Evidencia",
                        "description": "Las amenazas deben ser documentadas adecuadamente.",
                        "action": "Preserve todas las evidencias digitales y elabore un reporte detallado del incidente.",
                        "priority": 2
                    }
                ],
                "Exclusión Social": [
                    {
                        "id": "exclusion_001",
                        "icon": "👥",
                        "title": "Patrones de Exclusión Detectados",
                        "description": "Se identificaron comportamientos que buscan aislar o excluir a la víctima.",
                        "action": "Promueva actividades de integración grupal y fortalezca la cohesión social en el entorno.",
                        "priority": 2
                    },
                    {
                        "id": "exclusion_002",
                        "icon": "🤝",
                        "title": "Fomento de Inclusión",
                        "description": "La exclusión social puede tener efectos psicológicos duraderos.",
                        "action": "Implemente programas de mentorías entre pares y actividades colaborativas.",
                        "priority": 1
                    }
                ],
                "Acoso Sexual": [
                    {
                        "id": "sexual_001",
                        "icon": "🔴",
                        "title": "Contenido de Naturaleza Sexual Detectado",
                        "description": "Se han identificado patrones de acoso sexual que requieren acción inmediata.",
                        "action": "Contacte inmediatamente a las autoridades competentes y proporcione apoyo psicológico a la víctima.",
                        "priority": 1
                    },
                    {
                        "id": "sexual_002",
                        "icon": "🛡️",
                        "title": "Medidas de Protección Urgentes",
                        "description": "El acoso sexual requiere medidas de protección inmediatas.",
                        "action": "Implemente medidas de protección para la víctima y considere la suspensión temporal del agresor.",
                        "priority": 1
                    }
                ]
            },
            
            # Recomendaciones por nivel de severidad
            "severity": {
                "Low": [
                    {
                        "id": "low_001",
                        "icon": "👀",
                        "title": "Monitoreo Preventivo",
                        "description": "Nivel de riesgo bajo, pero requiere seguimiento.",
                        "action": "Establezca un monitoreo discreto y eduque sobre comunicación digital apropiada.",
                        "priority": 1
                    },
                    {
                        "id": "low_002",
                        "icon": "📖",
                        "title": "Educación Temprana",
                        "description": "La intervención temprana previene la escalación.",
                        "action": "Organice talleres sobre netiqueta y comunicación respetuosa en línea.",
                        "priority": 2
                    }
                ],
                "Medium": [
                    {
                        "id": "medium_001",
                        "icon": "⚠️",
                        "title": "Intervención Necesaria",
                        "description": "Riesgo moderado que requiere atención activa.",
                        "action": "Convoque a una reunión con todas las partes involucradas para abordar la situación.",
                        "priority": 1
                    },
                    {
                        "id": "medium_002",
                        "icon": "📝",
                        "title": "Plan de Acción Estructurado",
                        "description": "Desarrolle un plan de intervención específico.",
                        "action": "Cree un plan de seguimiento con objetivos claros y plazos definidos.",
                        "priority": 2
                    }
                ],
                "High": [
                    {
                        "id": "high_001",
                        "icon": "🚨",
                        "title": "Acción Inmediata Requerida",
                        "description": "Alto riesgo que demanda intervención urgente.",
                        "action": "Contacte inmediatamente a los padres, autoridades escolares y considere apoyo psicológico.",
                        "priority": 1
                    },
                    {
                        "id": "high_002",
                        "icon": "🏥",
                        "title": "Apoyo Profesional",
                        "description": "La situación requiere intervención de profesionales.",
                        "action": "Derive a la víctima a servicios de apoyo psicológico y considere medidas disciplinarias.",
                        "priority": 1
                    }
                ],
                "Critical": [
                    {
                        "id": "critical_001",
                        "icon": "🆘",
                        "title": "Emergencia - Contactar Autoridades",
                        "description": "Situación crítica que requiere intervención inmediata de autoridades.",
                        "action": "Contacte inmediatamente a las autoridades competentes y preserve toda la evidencia digital.",
                        "priority": 1
                    },
                    {
                        "id": "critical_002",
                        "icon": "🚑",
                        "title": "Apoyo de Emergencia",
                        "description": "La víctima necesita apoyo inmediato y protección.",
                        "action": "Proporcione apoyo de emergencia a la víctima y considere medidas de protección inmediatas.",
                        "priority": 1
                    }
                ]
            },
            
            # Recomendaciones generales por contexto
            "general": [
                {
                    "id": "general_001",
                    "icon": "👨‍👩‍👧‍👦",
                    "title": "Involucrar a la Familia",
                    "description": "La colaboración familiar es clave en la prevención del ciberacoso.",
                    "action": "Organice sesiones informativas para padres sobre ciberacoso y seguridad digital.",
                    "priority": 2
                },
                {
                    "id": "general_002",
                    "icon": "🔄",
                    "title": "Seguimiento Continuo",
                    "description": "El monitoreo regular previene la recurrencia de patrones problemáticos.",
                    "action": "Establezca un sistema de seguimiento regular para evaluar la efectividad de las medidas.",
                    "priority": 2
                }
            ]
        }

    def _get_fallback_recommendation(self):
        """Recomendación de respaldo"""
        return {
            'id': 'fallback_education',
            'icon': '📚',
            'title': 'Educación y Prevención',
            'description': 'La educación continua es la mejor herramienta para prevenir el ciberacoso.',
            'action': 'Implemente programas de concientización sobre comunicación digital responsable y respeto en línea.',
            'priority': 1
        }

    def generate_recommendations(self, analysis_result):
        """
        Genera recomendaciones inteligentes basadas en el resultado del análisis
        
        Args:
            analysis_result (dict): Resultado del análisis de ciberacoso
            
        Returns:
            dict: Recomendación principal seleccionada
        """
        try:
            print(f"DEBUG: Análisis recibido: {analysis_result}")  # Debug
            
            # Verificar si es ciberacoso
            is_cyberbullying = analysis_result.get('is_cyberbullying', False)
            
            if not is_cyberbullying:
                # Contenido seguro - seleccionar recomendación de seguridad
                safe_recommendations = self.recommendations_bank.get('safe', [])
                if safe_recommendations:
                    main_recommendation = safe_recommendations[0]  # Primera recomendación de seguridad
                    print(f"DEBUG: Seleccionada recomendación de contenido seguro: {main_recommendation['title']}")
                else:
                    main_recommendation = self._get_fallback_recommendation()
            else:
                # Contenido problemático - lógica inteligente de selección
                candidates = []
                
                # 1. Priorizar por severidad del riesgo
                risk_level = analysis_result.get('risk_level', 'Low')
                print(f"DEBUG: Nivel de riesgo: {risk_level}")
                
                severity_recs = self.recommendations_bank['severity'].get(risk_level, [])
                if severity_recs:
                    candidates.extend(severity_recs)
                    print(f"DEBUG: Agregadas {len(severity_recs)} recomendaciones por severidad")
                
                # 2. Agregar recomendaciones específicas por categoría detectada
                if analysis_result.get('matches'):
                    categories_found = list(set([
                        match.get('pattern_info', {}).get('category', '')
                        for match in analysis_result['matches']
                        if match.get('pattern_info', {}).get('category')
                    ]))
                    
                    print(f"DEBUG: Categorías encontradas: {categories_found}")
                    
                    for category in categories_found:
                        category_recs = self.recommendations_bank['categories'].get(category, [])
                        if category_recs:
                            candidates.extend(category_recs)
                            print(f"DEBUG: Agregadas recomendaciones para categoría '{category}': {len(category_recs)}")
                
                # 3. Seleccionar la mejor recomendación
                if candidates:
                    # Priorizar por: 1) Prioridad más alta (número menor), 2) Categoría específica sobre severidad general
                    best_recommendation = min(candidates, key=lambda x: (x['priority'], 0 if x['id'].startswith(('threat_', 'sexual_', 'insult_', 'exclusion_')) else 1))
                    main_recommendation = best_recommendation
                    print(f"DEBUG: Mejor recomendación seleccionada: {main_recommendation['title']}")
                else:
                    print("DEBUG: No se encontraron candidatos, usando fallback")
                    main_recommendation = self._get_fallback_recommendation()
            
            return {
                'main_recommendation': main_recommendation
            }
            
        except Exception as e:
            print(f"Error generando recomendaciones: {e}")
            return {
                'main_recommendation': self._get_fallback_recommendation()
            }

    def _select_recommendations_by_type(self, rec_type, count):
        """Selecciona recomendaciones por tipo"""
        recommendations = self.recommendations_bank.get(rec_type, [])
        return recommendations[:count]

    def _select_recommendations_by_severity(self, severity, count):
        """Selecciona recomendaciones por nivel de severidad"""
        recommendations = self.recommendations_bank['severity'].get(
            severity, 
            self.recommendations_bank['severity']['Low']
        )
        return recommendations[:count]

    def _select_recommendations_by_category(self, category, count):
        """Selecciona recomendaciones por categoría de patrón"""
        recommendations = self.recommendations_bank['categories'].get(category, [])
        return recommendations[:count]

    def get_all_recommendations(self):
        """Retorna todas las recomendaciones disponibles (para propósitos de debugging)"""
        return self.recommendations_bank


# Función para usar desde el backend
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
    # Ejemplo de uso para testing
    test_analysis = {
        "is_cyberbullying": True,
        "risk_level": "High",
        "total_patterns_found": 2,
        "total_matches": 3,
        "matches": [
            {
                "pattern_info": {
                    "category": "Amenazas",
                    "severity": "High"
                }
            },
            {
                "pattern_info": {
                    "category": "Insultos y Ofensas", 
                    "severity": "Medium"
                }
            }
        ]
    }
    
    result = get_recommendations_for_analysis(test_analysis)
    print("Resultado del test:")
    print(f"Éxito: {result['success']}")
    
    if result['recommendation']:
        rec = result['recommendation']
        print(f"\nRecomendación seleccionada:")
        print(f"  Título: {rec['title']}")
        print(f"  Prioridad: {rec['priority']}")
        print(f"  Descripción: {rec['description']}")
        print(f"  Acción: {rec['action']}")
