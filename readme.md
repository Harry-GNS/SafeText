![Portada del Proyecto](media/Portada%20Github.jpg)

![Python](https://img.shields.io/badge/Python-3.8%2B-blue)
![License](https://img.shields.io/badge/License-MIT-green)
![Pattern Matching](https://img.shields.io/badge/Pattern%20Matching-KMP%20%7C%20Boyer--Moore-orange)
![Web](https://img.shields.io/badge/Web-HTML%20%7C%20CSS%20%7C%20JS-lightgrey)

# 🛡️ Sistema de Detección de Ciberacoso Escolar

> Un sistema web que utiliza algoritmos de búsqueda de patrones para detectar y prevenir el ciberacoso en entornos educativos.

## 🌐 **Acceso al Proyecto**

📍 **¡Prueba el sistema en vivo!**  
🔗 **URL:** https://web-production-5a61.up.railway.app/

*El proyecto está completamente funcional y desplegado en Railway para demostración y pruebas.*

## 👥 Autores

- **Harry Guajan**
- **Joel Tinitana**

---

## 📋 Descripción del Proyecto

Este proyecto implementa un sistema de detección  de ciberacoso dirigido  al entorno escolar. Utiliza algoritmos clásicos de búsqueda de patrones (KMP y Boyer-Moore) para identificar contenido ofensivo, amenazas e insultos en mensajes de texto, proporcionando una herramienta valiosa para educadores, orientadores y administradores escolares.

### 🎯 Objetivo Principal

Desarrollar una aplicación web que permita analizar mensajes de texto en tiempo real para detectar patrones de ciberacoso, clasificarlos por nivel de gravedad y proporcionar recomendaciones de acción apropiadas.

---

## ✨ Características Principales

### 🔍 Detección Inteligente
- **Algoritmos KMP y Boyer-Moore** para búsqueda eficiente de patrones
- **Base de datos de 115 patrones** configurables con insultos, amenazas, exclusión social y acoso sexual
- **Clasificación por severidad**: Low, Medium, High, Critical (0-100 puntos)
- **Detección insensible a mayúsculas/minúsculas**
- **Selector automático de algoritmo** basado en características del patrón

### 🌐 Interfaz Web Moderna
- **Análisis en tiempo real** con feedback visual inmediato
- **Texto resaltado** mostrando patrones detectados con tooltips informativos
- **Cálculo inteligente de porcentajes** considerando densidad de patrones y longitud del texto
- **Sistema de recomendaciones personalizadas** basado en el tipo de riesgo detectado
- **Exportación de reportes** detallados en formato texto

### 📊 Análisis Avanzado
- **Categorización automática** por tipo de patrón (Insultos, Amenazas, Exclusión Social, Acoso Sexual)
- **Algoritmos usados** mostrados transparentemente en cada detección
- **Nivel de riesgo dinámico** calculado por múltiples factores
- **Recomendaciones específicas** según severidad y categoría detectada


---

## 🛠️ Tecnologías Utilizadas

| Tecnología | Propósito | Estado |
|------------|-----------|---------|
| **Python 3.8+** | Backend y algoritmos principales | ✅ Implementado |
| **Flask** | Framework web y API RESTful | ✅ Implementado |
| **HTML5 + CSS3** | Frontend moderno y responsivo | ✅ Implementado |
| **JavaScript (Vanilla)** | Interactividad y llamadas a API | ✅ Implementado |
| **CSV** | Base de datos de patrones | ✅ 115 patrones |
| **Algoritmo KMP** | Búsqueda de patrones cortos | ✅ Implementado |
| **Algoritmo Boyer-Moore** | Búsqueda de patrones largos | ✅ Implementado |

### 🏗️ Arquitectura del Sistema
- **Frontend**: SPA (Single Page Application) con navegación fluida
- **Backend**: API REST con endpoints especializados
- **Motor de Recomendaciones**: Sistema inteligente de sugerencias personalizadas
- **Análisis**: Procesamiento en tiempo real con retroalimentación visual

---

## 📁 Estructura del Proyecto

```
```


---

## 🚀 Cómo Funciona la Aplicación

### 👨‍🏫 Usuarios Objetivo
- **Profesores y educadores**
- **Orientadores escolares**
- **Administradores educativos**
- **Padres de familia** (con adaptación)

---

## 🧪 Casos de Prueba

El sistema ha sido probado  con:

(Todavia no hemos hecho pruebas exaustas)



---

##  Estado del Desarrollo

### ✅ **Funcionalidades Completadas**
- ✅ Algoritmos KMP y Boyer-Moore implementados y optimizados
- ✅ Sistema de análisis en tiempo real funcionando
- ✅ Interface web moderna y responsiva
- ✅ Motor de recomendaciones inteligentes personalizado
- ✅ Base de datos de 115 patrones categorizados
- ✅ Cálculo inteligente de porcentajes basado en densidad
- ✅ Exportación de reportes detallados
- ✅ API RESTful completa con todos los endpoints
- ✅ Sistema de resaltado visual de patrones detectados
- ✅ Categorización automática por tipo de patrón


### 🚧 **Tareas Pendientes (Por Implementar)**
- 🔄 **Visualización de patrones en opciones**: Mostrar la lista completa de 115 patrones en el panel de configuración
- 🔄 **Mejorar decisión de recomendaciones**: Arreglar el algoritmo de selección de recomendaciones para mayor precisión contextual
- 🔄 **Mejorar layout del resumen de análisis**: Optimizar la presentación visual de estadísticas y métricas
- 🔄 **Gestión completa de patrones**: Implementar CRUD (crear, editar, eliminar) para patrones personalizados
- 🔄 **Historial de análisis**: Sistema de almacenamiento y consulta de análisis anteriores


---

## �🔮 Funcionalidades Avanzadas (Futuras Mejoras Algun Dia)

### 🤖 Integración con IA
- **Procesamiento de Lenguaje Natural (NLP)**
- **Detección de sarcasmo e ironía**
- **Análisis de sentimientos contextual**
- **Corrección automática de errores ortográficos**

### 📱 Características Adicionales
- **Aplicación móvil** para reportes anónimos
- **Dashboard analytics** con métricas de incidentes
- **Sistema de notificaciones** en tiempo real
- **Integración con plataformas educativas** (Google Classroom, Teams)
- **Multiidioma** para comunidades diversas

---

## 🎓 Contexto Académico

Este proyecto forma parte del curso **Estructura de Datos y Algoritmos II** y tiene como objetivos pedagógicos:

- Implementar algoritmos clásicos de búsqueda de patrones
- Aplicar estructuras de datos eficientes
- Desarrollar soluciones tecnológicas con impacto social
- Analizar complejidad computacional y optimización
- Integrar conocimientos teóricos en aplicaciones prácticas

---

## 🛡️ Consideraciones Éticas

- **Privacidad**: Los mensajes no se almacenan permanentemente
- **Transparencia**: Algoritmos explicables y auditables
- **Prevención**: Enfoque educativo, no punitivo
- **Inclusión**: Respeto a la diversidad cultural y lingüística

---

## 🤝 Contribuciones

Este es un proyecto académico desarrollado por estudiantes de EDA II. Las contribuciones futuras pueden incluir:

- Mejoras en algoritmos de detección
- Expansión de la base de datos de patrones
- Optimizaciones de rendimiento
- Nuevas funcionalidades de interfaz

---


## 📄 Licencia

Este proyecto es desarrollado con fines académicos y educativos como parte del curso EDA II - Escuela Politécnica Nacional (EPN).

---

