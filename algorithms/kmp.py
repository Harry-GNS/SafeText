"""
Implementación del algoritmo Knuth-Morris-Pratt (KMP) para búsqueda de patrones.
Ideal para patrones cortos o con caracteres repetidos.
"""

class KMPAlgorithm:
    def __init__(self):
        self.name = "KMP (Knuth-Morris-Pratt)"
        self.best_for = "Patrones cortos o con repeticiones"
    
    def compute_lps(self, pattern):
        """
        Computa la tabla LPS (Longest Proper Prefix which is also Suffix)
        para el patrón dado.
        
        Args:
            pattern (str): El patrón de búsqueda
            
        Returns:
            list: Tabla LPS
        """
        m = len(pattern)
        lps = [0] * m
        length = 0  # Longitud del prefijo más largo que es también sufijo
        i = 1
        
        # Construir la tabla LPS
        while i < m:
            if pattern[i] == pattern[length]:
                length += 1
                lps[i] = length
                i += 1
            else:
                if length != 0:
                    length = lps[length - 1]
                else:
                    lps[i] = 0
                    i += 1
        
        return lps
    
    def search(self, text, pattern):
        """
        Busca todas las ocurrencias del patrón en el texto usando KMP.
        
        Args:
            text (str): El texto donde buscar
            pattern (str): El patrón a buscar
            
        Returns:
            list: Lista de posiciones donde se encontró el patrón
        """
        if not pattern or not text:
            return []
        
        # Convertir a minúsculas para búsqueda insensible a mayúsculas
        text = text.lower()
        pattern = pattern.lower()
        
        n = len(text)
        m = len(pattern)
        
        # Crear tabla LPS
        lps = self.compute_lps(pattern)
        
        matches = []
        i = 0  # Índice para el texto
        j = 0  # Índice para el patrón
        
        while i < n:
            if pattern[j] == text[i]:
                i += 1
                j += 1
            
            if j == m:
                matches.append(i - j)
                j = lps[j - 1]
            elif i < n and pattern[j] != text[i]:
                if j != 0:
                    j = lps[j - 1]
                else:
                    i += 1
        
        return matches
    
    def find_pattern_info(self, text, pattern):
        """
        Encuentra información detallada sobre las ocurrencias del patrón.
        
        Args:
            text (str): El texto donde buscar
            pattern (str): El patrón a buscar
            
        Returns:
            dict: Información detallada de las coincidencias
        """
        matches = self.search(text, pattern)
        
        return {
            'algorithm': self.name,
            'pattern': pattern,
            'total_matches': len(matches),
            'positions': matches,
            'pattern_length': len(pattern),
            'found': len(matches) > 0,
            'matches_detail': [
                {
                    'position': pos,
                    'context_start': max(0, pos - 10),
                    'context_end': min(len(text), pos + len(pattern) + 10),
                    'context': text[max(0, pos - 10):min(len(text), pos + len(pattern) + 10)]
                }
                for pos in matches
            ]
        }
