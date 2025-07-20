"""
Selector automático de algoritmo para búsqueda de patrones.
Decide entre KMP y Boyer-Moore según las características del patrón.
"""

from .kmp import KMPAlgorithm
from .boyer_moore import BoyerMooreAlgorithm
import re

class AlgorithmSelector:
    def __init__(self):
        self.kmp = KMPAlgorithm()
        self.boyer_moore = BoyerMooreAlgorithm()
    
    def analyze_pattern(self, pattern):
        """
        Analiza las características del patrón para decidir qué algoritmo usar.
        
        Args:
            pattern (str): El patrón a analizar
            
        Returns:
            dict: Información del análisis del patrón
        """
        if not pattern:
            return {
                'length': 0,
                'has_repetitions': False,
                'repetition_ratio': 0,
                'recommended_algorithm': 'KMP',
                'reason': 'Patrón vacío'
            }
        
        length = len(pattern)
        
        # Calcular repeticiones
        char_count = {}
        for char in pattern.lower():
            char_count[char] = char_count.get(char, 0) + 1
        
        # Calcular ratio de repetición
        max_repetitions = max(char_count.values()) if char_count else 0
        repetition_ratio = max_repetitions / length if length > 0 else 0
        
        # Detectar patrones repetitivos (como "jejeje", "jajaja")
        has_repetitions = repetition_ratio > 0.5 or self._has_repetitive_patterns(pattern)
        
        # Decidir algoritmo
        if length <= 10:
            algorithm = 'KMP'
            reason = f'Patrón corto ({length} caracteres)'
        elif has_repetitions:
            algorithm = 'KMP'
            reason = f'Patrón con repeticiones (ratio: {repetition_ratio:.2f})'
        else:
            algorithm = 'Boyer-Moore'
            reason = f'Patrón largo ({length} caracteres) con baja repetición'
        
        return {
            'length': length,
            'has_repetitions': has_repetitions,
            'repetition_ratio': repetition_ratio,
            'recommended_algorithm': algorithm,
            'reason': reason,
            'char_distribution': char_count
        }
    
    def _has_repetitive_patterns(self, pattern):
        """
        Detecta patrones repetitivos comunes en el texto.
        
        Args:
            pattern (str): El patrón a analizar
            
        Returns:
            bool: True si tiene patrones repetitivos
        """
        pattern_lower = pattern.lower()
        
        # Detectar repeticiones de 2-3 caracteres
        for length in [2, 3]:
            for i in range(len(pattern_lower) - length + 1):
                substring = pattern_lower[i:i + length]
                # Contar cuántas veces aparece este substring
                count = len(re.findall(substring, pattern_lower))
                if count >= 3:  # Si aparece 3 o más veces
                    return True
        
        return False
    
    def select_algorithm(self, pattern):
        """
        Selecciona el algoritmo más apropiado para el patrón dado.
        
        Args:
            pattern (str): El patrón de búsqueda
            
        Returns:
            tuple: (algoritmo_seleccionado, información_del_análisis)
        """
        analysis = self.analyze_pattern(pattern)
        
        if analysis['recommended_algorithm'] == 'KMP':
            return self.kmp, analysis
        else:
            return self.boyer_moore, analysis
    
    def search_pattern(self, text, pattern):
        """
        Busca un patrón en el texto usando el algoritmo más apropiado.
        
        Args:
            text (str): El texto donde buscar
            pattern (str): El patrón a buscar
            
        Returns:
            dict: Resultados de la búsqueda con información del algoritmo usado
        """
        algorithm, analysis = self.select_algorithm(pattern)
        
        # Realizar la búsqueda
        result = algorithm.find_pattern_info(text, pattern)
        
        # Agregar información del análisis
        result['algorithm_analysis'] = analysis
        result['algorithm_used'] = analysis['recommended_algorithm']
        result['selection_reason'] = analysis['reason']
        
        return result
