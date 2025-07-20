"""
Implementación del algoritmo Boyer-Moore para búsqueda de patrones.
Ideal para patrones largos (>10 caracteres) con baja repetición.
"""

class BoyerMooreAlgorithm:
    def __init__(self):
        self.name = "Boyer-Moore"
        self.best_for = "Patrones largos con baja repetición"
    
    def bad_character_table(self, pattern):
        """
        Construye la tabla de caracteres malos para el algoritmo Boyer-Moore.
        
        Args:
            pattern (str): El patrón de búsqueda
            
        Returns:
            dict: Tabla de caracteres malos
        """
        table = {}
        m = len(pattern)
        
        # Para cada carácter en el patrón, guardar su última posición
        for i in range(m):
            table[pattern[i]] = i
        
        return table
    
    def good_suffix_table(self, pattern):
        """
        Construye la tabla de sufijos buenos para el algoritmo Boyer-Moore.
        
        Args:
            pattern (str): El patrón de búsqueda
            
        Returns:
            list: Tabla de sufijos buenos
        """
        m = len(pattern)
        table = [0] * m
        last_prefix_position = m
        
        # Llenar la tabla desde el final hacia el inicio
        for i in range(m - 1, -1, -1):
            if self.is_prefix(pattern, i + 1):
                last_prefix_position = i + 1
            table[m - 1 - i] = last_prefix_position - i + m - 1
        
        # Buscar sufijos que coincidan con prefijos
        for i in range(m - 1):
            suffix_length = self.suffix_length(pattern, i)
            table[suffix_length] = m - 1 - i + suffix_length
        
        return table
    
    def is_prefix(self, pattern, p):
        """
        Verifica si el sufijo a partir de la posición p es un prefijo del patrón.
        
        Args:
            pattern (str): El patrón
            p (int): Posición de inicio del sufijo
            
        Returns:
            bool: True si es prefijo, False en caso contrario
        """
        j = 0
        for i in range(p, len(pattern)):
            if pattern[i] != pattern[j]:
                return False
            j += 1
        return True
    
    def suffix_length(self, pattern, p):
        """
        Calcula la longitud del sufijo que termina en la posición p.
        
        Args:
            pattern (str): El patrón
            p (int): Posición final del sufijo
            
        Returns:
            int: Longitud del sufijo
        """
        length = 0
        j = len(pattern) - 1
        i = p
        
        while i >= 0 and pattern[i] == pattern[j]:
            length += 1
            i -= 1
            j -= 1
        
        return length
    
    def search(self, text, pattern):
        """
        Busca todas las ocurrencias del patrón en el texto usando Boyer-Moore.
        
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
        
        if m > n:
            return []
        
        # Construir tablas
        bad_char = self.bad_character_table(pattern)
        good_suffix = self.good_suffix_table(pattern)
        
        matches = []
        i = 0  # Posición en el texto
        
        while i <= n - m:
            j = m - 1  # Empezar desde el final del patrón
            
            # Comparar desde el final del patrón hacia el inicio
            while j >= 0 and pattern[j] == text[i + j]:
                j -= 1
            
            if j < 0:
                # Patrón encontrado
                matches.append(i)
                # Mover usando la tabla de sufijos buenos
                i += good_suffix[0] if m > 1 else 1
            else:
                # Calcular el desplazamiento usando ambas reglas
                bad_char_shift = j - bad_char.get(text[i + j], -1)
                good_suffix_shift = good_suffix[m - 1 - j]
                
                # Usar el mayor desplazamiento
                i += max(bad_char_shift, good_suffix_shift, 1)
        
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
