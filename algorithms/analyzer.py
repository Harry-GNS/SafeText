"""
Analizador principal para detección de ciberacoso.
Coordina la búsqueda de múltiples patrones y genera reportes.
"""

import csv
import os
from .selector import AlgorithmSelector

class CyberbullyingAnalyzer:
    def __init__(self, patterns_file=None):
        self.selector = AlgorithmSelector()
        self.patterns = []
        self.patterns_file = patterns_file or 'patrones.csv'
        self.load_patterns()
    
    def load_patterns(self):
        """
        Carga los patrones desde el archivo CSV.
        """
        self.patterns = []
        
        if not os.path.exists(self.patterns_file):
            # Crear archivo con patrones por defecto si no existe
            self.create_default_patterns()
        
        try:
            with open(self.patterns_file, 'r', encoding='utf-8') as file:
                reader = csv.DictReader(file)
                for row in reader:
                    # Mapear severidad numérica a categórica
                    nivel = int(row.get('nivel_gravedad', 50))
                    if nivel >= 80:
                        severity = 'Critical'
                    elif nivel >= 70:
                        severity = 'High'
                    elif nivel >= 50:
                        severity = 'Medium'
                    else:
                        severity = 'Low'
                    
                    self.patterns.append({
                        'id': row.get('id', ''),
                        'pattern': row.get('frase', '').strip('"'),  # Quitar comillas
                        'category': row.get('categorias', 'General'),
                        'severity': severity,
                        'description': row.get('descripcion', '').strip('"')
                    })
        except Exception as e:
            print(f"Error al cargar patrones: {e}")
            self.create_default_patterns()
    
    def create_default_patterns(self):
        """
        Crea un archivo CSV con patrones por defecto.
        """
        default_patterns = [
            {'id': '1', 'pattern': 'idiota', 'category': 'Insulto', 'severity': 'Medium', 'description': 'Insulto común'},
            {'id': '2', 'pattern': 'estúpido', 'category': 'Insulto', 'severity': 'Medium', 'description': 'Insulto común'},
            {'id': '3', 'pattern': 'tonto', 'category': 'Insulto', 'severity': 'Low', 'description': 'Insulto leve'},
            {'id': '4', 'pattern': 'cállate', 'category': 'Agresión', 'severity': 'Medium', 'description': 'Comando agresivo'},
            {'id': '5', 'pattern': 'nadie te quiere', 'category': 'Exclusión', 'severity': 'High', 'description': 'Exclusión social'},
            {'id': '6', 'pattern': 'eres feo', 'category': 'Apariencia', 'severity': 'Medium', 'description': 'Burla por apariencia'},
            {'id': '7', 'pattern': 'no sirves para nada', 'category': 'Autoestima', 'severity': 'High', 'description': 'Ataque a la autoestima'},
            {'id': '8', 'pattern': 'mejor muérete', 'category': 'Amenaza', 'severity': 'Critical', 'description': 'Amenaza grave'},
            {'id': '9', 'pattern': 'jajajaja', 'category': 'Burla', 'severity': 'Low', 'description': 'Burla repetitiva'},
            {'id': '10', 'pattern': 'loser', 'category': 'Insulto', 'severity': 'Medium', 'description': 'Insulto en inglés'}
        ]
        
        try:
            with open(self.patterns_file, 'w', newline='', encoding='utf-8') as file:
                fieldnames = ['id', 'pattern', 'category', 'severity', 'description']
                writer = csv.DictWriter(file, fieldnames=fieldnames)
                writer.writeheader()
                writer.writerows(default_patterns)
            
            self.patterns = default_patterns
        except Exception as e:
            print(f"Error al crear archivo de patrones: {e}")
    
    def analyze_text(self, text):
        """
        Analiza un texto buscando todos los patrones de ciberacoso.
        
        Args:
            text (str): El texto a analizar
            
        Returns:
            dict: Resultado completo del análisis
        """
        if not text:
            return {
                'text_length': 0,
                'total_patterns_found': 0,
                'matches': [],
                'severity_summary': {},
                'category_summary': {},
                'algorithms_used': {},
                'is_cyberbullying': False,
                'risk_level': 'None'
            }
        
        matches = []
        algorithms_used = {}
        severity_counts = {'Low': 0, 'Medium': 0, 'High': 0, 'Critical': 0}
        category_counts = {}
        
        # Analizar cada patrón
        for pattern_info in self.patterns:
            pattern = pattern_info['pattern']
            if not pattern:
                continue
            
            # Buscar el patrón en el texto
            result = self.selector.search_pattern(text, pattern)
            
            if result['found']:
                # Agregar información del patrón
                result['pattern_info'] = pattern_info
                matches.append(result)
                
                # Contar algoritmos usados
                algorithm = result['algorithm_used']
                algorithms_used[algorithm] = algorithms_used.get(algorithm, 0) + 1
                
                # Contar severidad
                severity = pattern_info['severity']
                severity_counts[severity] += result['total_matches']
                
                # Contar categorías
                category = pattern_info['category']
                category_counts[category] = category_counts.get(category, 0) + result['total_matches']
        
        # Calcular nivel de riesgo
        total_matches = sum(severity_counts.values())
        risk_level = self._calculate_risk_level(severity_counts, total_matches)
        
        return {
            'text_length': len(text),
            'total_patterns_found': len(matches),
            'total_matches': total_matches,
            'matches': matches,
            'severity_summary': severity_counts,
            'category_summary': category_counts,
            'algorithms_used': algorithms_used,
            'is_cyberbullying': total_matches > 0,
            'risk_level': risk_level,
            'analysis_summary': self._generate_summary(matches, risk_level)
        }
    
    def _calculate_risk_level(self, severity_counts, total_matches):
        """
        Calcula el nivel de riesgo basado en la severidad de los patrones encontrados.
        
        Args:
            severity_counts (dict): Conteo por nivel de severidad
            total_matches (int): Total de coincidencias
            
        Returns:
            str: Nivel de riesgo
        """
        if total_matches == 0:
            return 'None'
        
        # Pesos para cada nivel de severidad
        weights = {'Low': 1, 'Medium': 3, 'High': 7, 'Critical': 15}
        
        # Calcular puntuación ponderada
        weighted_score = sum(severity_counts[level] * weights[level] for level in weights)
        
        # Determinar nivel de riesgo
        if weighted_score >= 15:
            return 'Critical'
        elif weighted_score >= 7:
            return 'High'
        elif weighted_score >= 3:
            return 'Medium'
        else:
            return 'Low'
    
    def _generate_summary(self, matches, risk_level):
        """
        Genera un resumen del análisis.
        
        Args:
            matches (list): Lista de coincidencias encontradas
            risk_level (str): Nivel de riesgo calculado
            
        Returns:
            str: Resumen del análisis
        """
        if not matches:
            return "No se detectaron patrones de ciberacoso en el texto."
        
        total_patterns = len(matches)
        total_matches = sum(match['total_matches'] for match in matches)
        
        summary = f"Se detectaron {total_patterns} tipos de patrones de ciberacoso "
        summary += f"con un total de {total_matches} coincidencias. "
        summary += f"Nivel de riesgo: {risk_level}."
        
        if risk_level in ['High', 'Critical']:
            summary += " Se recomienda intervención inmediata."
        elif risk_level == 'Medium':
            summary += " Se recomienda monitoreo y posible intervención."
        
        return summary
    
    def get_pattern_statistics(self):
        """
        Obtiene estadísticas de los patrones cargados.
        
        Returns:
            dict: Estadísticas de los patrones
        """
        if not self.patterns:
            return {
                'total_patterns': 0,
                'by_category': {},
                'by_severity': {},
                'by_length': {}
            }
        
        by_category = {}
        by_severity = {}
        by_length = {'short': 0, 'medium': 0, 'long': 0}
        
        for pattern in self.patterns:
            # Por categoría
            category = pattern['category']
            by_category[category] = by_category.get(category, 0) + 1
            
            # Por severidad
            severity = pattern['severity']
            by_severity[severity] = by_severity.get(severity, 0) + 1
            
            # Por longitud
            length = len(pattern['pattern'])
            if length <= 5:
                by_length['short'] += 1
            elif length <= 15:
                by_length['medium'] += 1
            else:
                by_length['long'] += 1
        
        return {
            'total_patterns': len(self.patterns),
            'by_category': by_category,
            'by_severity': by_severity,
            'by_length': by_length
        }
