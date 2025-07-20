# SafeText - Sistema de Detección de Ciberacoso

**Desarrollado por:** Harry Guajan y Joel Tinitana  
**Institución:** Escuela Politécnica Nacional (EPN)  
**Materia:** Estructura de Datos y Algoritmos II  
**Año:** 2025

## Descripción

SafeText es un sistema avanzado de detección de ciberacoso que utiliza algoritmos de búsqueda de patrones (KMP y Boyer-Moore) para identificar mensajes de acoso en tiempo real. El sistema está diseñado para entornos educativos y utiliza una estrategia automática para seleccionar el algoritmo más eficiente según las características del patrón a buscar.

## Algoritmos Implementados

### 1. KMP (Knuth-Morris-Pratt)
- **Uso:** Patrones cortos o con caracteres repetidos
- **Ventajas:** Ligero, eficiente para patrones con repeticiones
- **Ejemplos:** "jejejeje", "calla", "tonto"

### 2. Boyer-Moore
- **Uso:** Patrones largos (>10 caracteres) con baja repetición
- **Ventajas:** Muy eficiente para patrones largos y diversos
- **Ejemplos:** "no sirves para nada", "eres muy feo y tonto"

### 3. Selector Automático
El sistema decide automáticamente qué algoritmo usar basándose en:
- Longitud del patrón
- Ratio de repetición de caracteres
- Presencia de patrones repetitivos

## Estructura del Proyecto

```
Proyecto-EDA-Segundo-Bimestre/
├── algorithms/
│   ├── __init__.py
│   ├── kmp.py              # Implementación KMP
│   ├── boyer_moore.py      # Implementación Boyer-Moore
│   ├── selector.py         # Selector automático
│   └── analyzer.py         # Analizador principal
├── templates/              # Frontend HTML
│   ├── index.html
│   ├── config.html
│   └── resultados.html
├── static/                 # Archivos CSS y JS
│   └── styles.css
├── app.py                  # API Flask
├── test_algorithms.py      # Script de pruebas
├── requirements.txt        # Dependencias Python
├── patrones.csv           # Base de datos de patrones
└── README_BACKEND.md      # Este archivo
```

## Instalación y Configuración

### 1. Requisitos Previos
- Python 3.7 o superior
- pip (administrador de paquetes de Python)

### 2. Instalación de Dependencias
```bash
pip install -r requirements.txt
```

### 3. Ejecutar el Sistema

#### Opción A: Solo Backend (API)
```bash
python app.py
```
La API estará disponible en: `http://localhost:5000`

#### Opción B: Pruebas de Algoritmos
```bash
python test_algorithms.py
```

## Uso de la API

### Endpoints Disponibles

#### 1. Analizar Texto Completo
```http
POST /api/analyze
Content-Type: application/json

{
    "text": "Texto a analizar para detectar ciberacoso"
}
```

**Respuesta:**
```json
{
    "success": true,
    "result": {
        "is_cyberbullying": true,
        "risk_level": "Medium",
        "total_patterns_found": 2,
        "total_matches": 3,
        "matches": [...],
        "analysis_summary": "..."
    }
}
```

#### 2. Buscar Patrón Específico
```http
POST /api/search-pattern
Content-Type: application/json

{
    "text": "Texto donde buscar",
    "pattern": "patrón específico"
}
```

#### 3. Analizar Características de Patrón
```http
POST /api/analyze-pattern
Content-Type: application/json

{
    "pattern": "patrón a analizar"
}
```

#### 4. Obtener Todos los Patrones
```http
GET /api/patterns
```

#### 5. Recargar Patrones
```http
POST /api/patterns/reload
```

## Estrategia de Selección de Algoritmos

El sistema utiliza las siguientes reglas para seleccionar automáticamente el algoritmo:

1. **KMP se usa cuando:**
   - El patrón tiene ≤ 10 caracteres
   - El ratio de repetición > 0.5
   - Se detectan patrones repetitivos (ej: "jajaja", "jejeje")

2. **Boyer-Moore se usa cuando:**
   - El patrón tiene > 10 caracteres
   - Baja repetición de caracteres
   - Patrones diversos y largos

3. **Por defecto:** KMP

## Niveles de Riesgo

El sistema calcula automáticamente el nivel de riesgo basándose en:

- **None:** Sin patrones detectados
- **Low:** Patrones leves (peso: 1)
- **Medium:** Patrones moderados (peso: 3)
- **High:** Patrones graves (peso: 7)
- **Critical:** Patrones críticos (peso: 15)

## Categorías de Patrones

- **Insulto:** Palabras ofensivas directas
- **Agresión:** Comandos agresivos
- **Exclusión:** Mensajes de exclusión social
- **Apariencia:** Burlas por apariencia física
- **Autoestima:** Ataques a la autoestima
- **Amenaza:** Amenazas directas o indirectas
- **Burla:** Expresiones de burla

## Gestión de Patrones

Los patrones se almacenan en `patrones.csv` con la estructura:
```csv
id,pattern,category,severity,description
1,idiota,Insulto,Medium,Insulto común
```

### Agregar Nuevos Patrones
1. Editar `patrones.csv`
2. Usar la API `/api/patterns/reload` para recargar
3. O reiniciar el servidor

## Ejemplos de Uso

### Ejemplo 1: Análisis Básico
```python
from algorithms.analyzer import CyberbullyingAnalyzer

analyzer = CyberbullyingAnalyzer()
result = analyzer.analyze_text("Eres un idiota y muy tonto")

print(f"¿Es ciberacoso?: {result['is_cyberbullying']}")
print(f"Nivel de riesgo: {result['risk_level']}")
```

### Ejemplo 2: Búsqueda Específica
```python
from algorithms.selector import AlgorithmSelector

selector = AlgorithmSelector()
result = selector.search_pattern("Texto de prueba", "prueba")

print(f"Algoritmo usado: {result['algorithm_used']}")
print(f"Coincidencias: {result['total_matches']}")
```

## Métricas de Rendimiento

El sistema proporciona información sobre:
- Algoritmo utilizado para cada búsqueda
- Tiempo de procesamiento
- Número de comparaciones
- Eficiencia por tipo de patrón

## Contribución

Para contribuir al proyecto:
1. Fork el repositorio
2. Crear una rama para la feature
3. Implementar cambios
4. Ejecutar pruebas: `python test_algorithms.py`
5. Crear Pull Request

## Limitaciones Actuales

- Solo detección basada en patrones exactos
- No incluye análisis semántico
- Limitado a idioma español
- Base de patrones inicial básica

## Trabajo Futuro

- Implementar análisis semántico con NLP
- Agregar soporte multiidioma
- Machine Learning para detección avanzada
- Interfaz de administración web
- Base de datos más robusta

## Licencia

Este proyecto es de uso libre para fines educativos y de investigación.

## Contacto

- **Harry Guajan:** harry.gns@outlook.com
- **Joel Tinitana:** joel.tinitana@epn.edu.ec

---

*Desarrollado como proyecto académico para Estructura de Datos y Algoritmos II - EPN 2025*
