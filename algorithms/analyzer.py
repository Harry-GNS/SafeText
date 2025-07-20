"""
Analizador principal para detección de ciberacoso.
Coordina la búsqueda de múltiples patrones y genera reportes.
"""

import csv
import os
from .selector import AlgorithmSelector

class CyberbullyingAnalyzer:
    def __init__(self, patterns_file=None, uploads_folder='uploads'):
        self.selector = AlgorithmSelector()
        self.patterns = []
        self.patterns_file = patterns_file or 'patrones.csv'
        self.uploads_folder = uploads_folder
        # 🔹 Carga inicial desde archivo base
        self.load_patterns()

    def load_patterns(self, custom_path=None):
        """
        Carga patrones desde un archivo específico.
        Si se pasa custom_path, se cargan desde ese archivo.
        """
        self.patterns = []
        path = custom_path if custom_path else self.patterns_file

        if not os.path.exists(path):
            print(f"[INFO] {path} no existe. Creando patrones por defecto.")
            self.create_default_patterns()
            return

        try:
            with open(path, 'r', encoding='utf-8') as file:
                reader = csv.DictReader(file)
                for row in reader:
                    self._agregar_patron(row)
            print(f"[INFO] Patrones cargados desde: {path} ({len(self.patterns)} patrones)")
        except Exception as e:
            print(f"[ERROR] No se pudieron cargar patrones desde {path}: {e}")
            self.create_default_patterns()

    def load_all_patterns(self):
        """
        Fusiona patrones base + todos los de uploads.
        """
        patrones_fusionados = []

        # Cargar base
        if os.path.exists(self.patterns_file):
            try:
                with open(self.patterns_file, 'r', encoding='utf-8') as base:
                    reader = csv.DictReader(base)
                    for row in reader:
                        patrones_fusionados.append(self._mapear_patron(row))
            except Exception as e:
                print(f"[ERROR] No se pudo leer el archivo base: {e}")

        # Cargar uploads
        if os.path.exists(self.uploads_folder):
            for archivo in os.listdir(self.uploads_folder):
                ruta = os.path.join(self.uploads_folder, archivo)
                if os.path.isfile(ruta) and archivo.lower().endswith(('.csv', '.txt')):
                    try:
                        with open(ruta, 'r', encoding='utf-8') as f:
                            reader = csv.DictReader(f)
                            for row in reader:
                                patrones_fusionados.append(self._mapear_patron(row))
                    except Exception as e:
                        print(f"[ERROR] No se pudo leer {archivo}: {e}")

        # Cargar en memoria
        self.patterns = patrones_fusionados
        print(f"[INFO] Patrones fusionados cargados: {len(self.patterns)} en total.")

    def _mapear_patron(self, row):
        """Convierte fila CSV en dict interno."""
        try:
            nivel = int(row.get('nivel_gravedad', 50))
        except ValueError:
            nivel = 50
        if nivel >= 80:
            severity = 'Critical'
        elif nivel >= 70:
            severity = 'High'
        elif nivel >= 50:
            severity = 'Medium'
        else:
            severity = 'Low'

        return {
            'id': row.get('id', ''),
            'pattern': row.get('frase', '').strip('"'),
            'category': row.get('categorias', 'General'),
            'severity': severity,
            'description': row.get('descripcion', '').strip('"')
        }

    def _agregar_patron(self, row):
        self.patterns.append(self._mapear_patron(row))

    def create_default_patterns(self):
        """
        Crea archivo base con patrones por defecto.
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
                fieldnames = ['id', 'frase', 'categorias', 'nivel_gravedad', 'descripcion']
                writer = csv.DictWriter(file, fieldnames=fieldnames)
                writer.writeheader()
                for p in default_patterns:
                    writer.writerow({
                        'id': p['id'],
                        'frase': p['pattern'],
                        'categorias': p['category'],
                        'nivel_gravedad': 50,
                        'descripcion': p['description']
                    })
            self.patterns = [self._mapear_patron({
                'id': p['id'],
                'frase': p['pattern'],
                'categorias': p['category'],
                'nivel_gravedad': 50,
                'descripcion': p['description']
            }) for p in default_patterns]
            print(f"[INFO] Archivo base {self.patterns_file} creado con {len(self.patterns)} patrones por defecto.")
        except Exception as e:
            print(f"[ERROR] No se pudo crear archivo base: {e}")

    # ---------------- ANALIZAR TEXTO ----------------
    def analyze_text(self, text):
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

        for pattern_info in self.patterns:
            pattern = pattern_info['pattern']
            if not pattern:
                continue
            result = self.selector.search_pattern(text, pattern)
            if result['found']:
                result['pattern_info'] = pattern_info
                matches.append(result)
                algo = result['algorithm_used']
                algorithms_used[algo] = algorithms_used.get(algo, 0) + 1
                severity_counts[pattern_info['severity']] += result['total_matches']
                category_counts[pattern_info['category']] = category_counts.get(pattern_info['category'], 0) + result['total_matches']

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
        if total_matches == 0:
            return 'None'
        weights = {'Low': 1, 'Medium': 3, 'High': 7, 'Critical': 15}
        weighted_score = sum(severity_counts[lvl] * weights[lvl] for lvl in weights)
        if weighted_score >= 15:
            return 'Critical'
        elif weighted_score >= 7:
            return 'High'
        elif weighted_score >= 3:
            return 'Medium'
        else:
            return 'Low'

    def _generate_summary(self, matches, risk_level):
        if not matches:
            return "No se detectaron patrones de ciberacoso."
        total_patterns = len(matches)
        total_matches = sum(m['total_matches'] for m in matches)
        resumen = f"Se detectaron {total_patterns} patrones con {total_matches} coincidencias. Nivel de riesgo: {risk_level}."
        if risk_level in ['High', 'Critical']:
            resumen += " Requiere intervención inmediata."
        elif risk_level == 'Medium':
            resumen += " Se recomienda monitoreo."
        return resumen

    def get_pattern_statistics(self):
        if not self.patterns:
            return {'total_patterns': 0, 'by_category': {}, 'by_severity': {}, 'by_length': {}}

        by_category, by_severity = {}, {}
        by_length = {'short': 0, 'medium': 0, 'long': 0}
        for p in self.patterns:
            by_category[p['category']] = by_category.get(p['category'], 0) + 1
            by_severity[p['severity']] = by_severity.get(p['severity'], 0) + 1
            l = len(p['pattern'])
            if l <= 5:
                by_length['short'] += 1
            elif l <= 15:
                by_length['medium'] += 1
            else:
                by_length['long'] += 1

        return {
            'total_patterns': len(self.patterns),
            'by_category': by_category,
            'by_severity': by_severity,
            'by_length': by_length
        }
