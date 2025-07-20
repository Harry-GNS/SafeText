"""
Sistema de Recomendaciones Inteligentes para SafeText
Generador de recomendaciones personalizadas basadas en el análisis de ciberacoso
"""

class RecommendationsEngine:
    def __init__(self):
        self.recommendations_bank = {
            # Recomendaciones para contenido seguro (eliminar la manual)
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
                },
                {
                    "id": "safe_004",
                    "icon": "🌟",
                    "title": "Comunicación Ejemplar",
                    "description": "El contenido refleja un intercambio comunicativo respetuoso y constructivo.",
                    "action": "Use este ejemplo como modelo para capacitaciones sobre comunicación digital positiva.",
                    "priority": 2
                }
            ],            # Recomendaciones por categorías de patrones
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
                        "action": "Organize talleres sobre netiqueta y comunicación respetuosa en línea.",
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
            
            # Recomendaciones generales por contexto (más variedad, sin manual)
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
                },
                {
                    "id": "general_003",
                    "icon": "📋",
                    "title": "Documentación de Incidentes",
                    "description": "Mantener registros detallados ayuda a identificar patrones y tendencias.",
                    "action": "Implemente un sistema de documentación para todos los incidentes de comunicación digital.",
                    "priority": 3
                },
                {
                    "id": "general_004",
                    "icon": "🎯",
                    "title": "Capacitación Especializada",
                    "description": "El personal debe estar preparado para identificar y manejar situaciones de ciberacoso.",
                    "action": "Organice capacitaciones especializadas para educadores y personal administrativo.",
                    "priority": 2
                },
                {
                    "id": "general_005",
                    "icon": "🔒",
                    "title": "Políticas de Seguridad Digital",
                    "description": "Las políticas claras establecen expectativas y consecuencias.",
                    "action": "Desarrolle y actualice políticas específicas sobre uso responsable de tecnología.",
                    "priority": 3
                }
            ]
        }

    def generate_recommendations(self, analysis_result):
        """
        Genera recomendaciones inteligentes basadas en el resultado del análisis
        
        Args:
            analysis_result (dict): Resultado del análisis de ciberacoso
            
        Returns:
            list: Lista de recomendaciones seleccionadas y ordenadas por prioridad
        """
        try:
            selected_recommendations = []
            
            # Seleccionar recomendaciones basadas en el análisis
            if not analysis_result.get('is_cyberbullying', False):
                # Contenido seguro - seleccionar 1 recomendación preventiva + 1 general
                selected_recommendations = self._select_recommendations_by_type('safe', 1)
                selected_recommendations.extend(self._select_recommendations_by_type('general', 1))
            else:
                # Contenido problemático - seleccionar por severidad
                risk_level = analysis_result.get('risk_level', 'Low')
                selected_recommendations = self._select_recommendations_by_severity(risk_level, 1)
                
                # Agregar recomendaciones por categorías detectadas
                if analysis_result.get('matches'):
                    categories_found = list(set([
                        match.get('pattern_info', {}).get('category', '')
                        for match in analysis_result['matches']
                        if match.get('pattern_info', {}).get('category')
                    ]))
                    
                    for category in categories_found[:1]:  # Solo 1 categoría para evitar repetición
                        category_recs = self._select_recommendations_by_category(category, 1)
                        selected_recommendations.extend(category_recs)
                
                # Agregar recomendación general si hay espacio
                if len(selected_recommendations) < 2:
                    selected_recommendations.extend(self._select_recommendations_by_type('general', 1))
            
            # Seleccionar solo la recomendación de mayor prioridad
            selected_recommendations = sorted(
                selected_recommendations, 
                key=lambda x: x['priority']
            )
            
            # Tomar solo la primera recomendación (mayor prioridad)
            main_recommendation = selected_recommendations[0] if selected_recommendations else None
            
            if not main_recommendation:
                # Fallback si no hay recomendaciones - usar una recomendación de educación
                main_recommendation = {
                    'id': 'fallback_education',
                    'icon': '�',
                    'title': 'Educación y Prevención',
                    'description': 'La educación continua es la mejor herramienta para prevenir el ciberacoso.',
                    'action': 'Implemente programas de concientización sobre comunicación digital responsable y respeto en línea.',
                    'priority': 1
                }
            
            # No incluir resumen en la respuesta
            return {
                'main_recommendation': main_recommendation
            }
            
        except Exception as e:
            print(f"Error generando recomendaciones: {e}")
            # Fallback con recomendación educativa
            fallback_recommendation = {
                'id': 'fallback_education',
                'icon': '�',
                'title': 'Educación y Prevención',
                'description': 'La educación continua es la mejor herramienta para prevenir el ciberacoso.',
                'action': 'Implemente programas de concientización sobre comunicación digital responsable y respeto en línea.',
                'priority': 1
            }
            
            return {
                'main_recommendation': fallback_recommendation
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

    def _get_fallback_recommendations(self):
        """Recomendaciones de respaldo en caso de error"""
        return [
            {
                "id": "fallback_001",
                "icon": "👀",
                "title": "Revisión Manual Recomendada",
                "description": "Se sugiere una revisión manual del contenido.",
                "action": "Evalúe el contexto completo de la comunicación y tome medidas apropiadas.",
                "priority": 1
            },
            {
                "id": "fallback_002", 
                "icon": "📚",
                "title": "Educación Preventiva",
                "description": "La educación es fundamental para prevenir el ciberacoso.",
                "action": "Implemente programas de concientización sobre comunicación digital responsable.",
                "priority": 2
            }
        ]

    def _generate_analysis_summary(self, analysis_result, top_recommendations):
        """Genera un resumen del análisis"""
        try:
            is_cyberbullying = analysis_result.get('is_cyberbullying', False)
            risk_level = analysis_result.get('risk_level', 'None')
            patterns_found = analysis_result.get('total_patterns_found', 0)
            total_matches = analysis_result.get('total_matches', 0)
            
            if not is_cyberbullying:
                return {
                    'status': 'Contenido Seguro',
                    'risk_level': 'Bajo',
                    'patterns_detected': 0,
                    'description': 'No se detectaron patrones de ciberacoso. El contenido parece apropiado para la comunicación digital.',
                    'next_steps': 'Mantener buenas prácticas de comunicación y seguir monitoreando.'
                }
            else:
                risk_description = {
                    'Low': 'Se detectaron algunos patrones menores que requieren atención.',
                    'Medium': 'Se identificaron patrones moderados de riesgo que necesitan intervención.',
                    'High': 'Se encontraron patrones serios de ciberacoso que requieren acción inmediata.',
                    'Critical': 'Se detectaron patrones críticos que demandan intervención urgente.'
                }.get(risk_level, 'Patrones detectados requieren evaluación.')
                
                next_steps = {
                    'Low': 'Educar sobre comunicación apropiada y monitorear de cerca.',
                    'Medium': 'Implementar medidas de intervención y seguimiento regular.',
                    'High': 'Tomar acción inmediata e involucrar a autoridades apropiadas.',
                    'Critical': 'Intervención de emergencia y medidas de protección inmediatas.'
                }.get(risk_level, 'Evaluar situación y tomar medidas apropiadas.')
                
                return {
                    'status': f'Riesgo {risk_level}',
                    'risk_level': risk_level,
                    'patterns_detected': patterns_found,
                    'total_matches': total_matches,
                    'description': risk_description,
                    'next_steps': next_steps
                }
                
        except Exception as e:
            print(f"Error generando resumen: {e}")
            return {
                'status': 'Error en análisis',
                'risk_level': 'Desconocido',
                'patterns_detected': 0,
                'description': 'Hubo un error al generar el resumen del análisis.',
                'next_steps': 'Realizar revisión manual del contenido.'
            }

    def get_all_recommendations(self):
        """Retorna todas las recomendaciones disponibles (para propósitos de debugging)"""
        return self.recommendations_bank


# Función para usar desde el backend
def get_recommendations_for_analysis(analysis_result):
    """
    Función principal para obtener recomendaciones desde el backend
    
    Args:
        analysis_result (dict): Resultado del análisis de ciberacoso
        
    Returns:
        dict: Respuesta con las recomendaciones generadas
    """
    try:
        engine = RecommendationsEngine()
        result = engine.generate_recommendations(analysis_result)
        
        return {
            "success": True,
            "recommendation": result['main_recommendation']
        }
        
    except Exception as e:
        fallback_recommendation = {
            "id": "fallback_education",
            "icon": "�",
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
    print(f"Número de recomendaciones: {result['total_recommendations']}")
    
    for i, rec in enumerate(result['recommendations'], 1):
        print(f"\n{i}. {rec['title']}")
        print(f"   Prioridad: {rec['priority']}")
        print(f"   Descripción: {rec['description']}")
