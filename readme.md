# 🛡️ Sistema de Detección de Ciberacoso Escolar

> Un sistema web  que utiliza algoritmos de búsqueda de patrones para detectar y prevenir el ciberacoso en entornos educativos.

## 👥 Autores

- **Harry Guajan**
- **Joel Tinitana**

---

## 📋 Descripción del Proyecto

Este proyecto implementa un sistema de detección automática de ciberacoso dirigido específicamente al entorno escolar. Utiliza algoritmos clásicos de búsqueda de patrones (KMP y Boyer-Moore) para identificar contenido ofensivo, amenazas e insultos en mensajes de texto, proporcionando una herramienta valiosa para educadores, orientadores y administradores escolares.

### 🎯 Objetivo Principal

Desarrollar una aplicación web que permita analizar mensajes de texto en tiempo real para detectar patrones de ciberacoso, clasificarlos por nivel de gravedad y proporcionar recomendaciones de acción apropiadas.

---

## ✨ Características Principales

### 🔍 Detección Inteligente
- **Algoritmos KMP y Boyer-Moore** para búsqueda eficiente de patrones
- **Base de datos de patrones** configurable con insultos, amenazas y exclusión social
- **Clasificación por gravedad**: Bajo, Medio, Alto
- **Detección insensible a mayúsculas/minúsculas**

### 🌐 Interfaz Web Intuitiva
- **Formulario de análisis** para pegar texto directamente
- **Carga de archivos** para analizar múltiples mensajes
- **Resultados detallados** con patrones detectados y recomendaciones
- **Panel de administración** para gestionar patrones de detección

### 📊 Sistema de Alertas
- **Alertas codificadas por colores** según el nivel de gravedad
- **Recomendaciones específicas** para cada tipo de incidente
- **Posicionamiento exacto** de patrones detectados en el texto

---

## 🛠️ Tecnologías Utilizadas

| Tecnología | Propósito |
|------------|-----------|

---

## 📁 Estructura del Proyecto



---

## 🚀 Cómo Funciona la Aplicación

### 👨‍🏫 Usuarios Objetivo
- **Profesores y educadores**
- **Orientadores escolares**
- **Administradores educativos**
- **Padres de familia** (con adaptación)

### 🔄 Flujo de Uso

1. **🌐 Acceso a la aplicación**
   - Abrir navegador en `http://localhost:5000`
   - Interfaz principal con formulario de análisis

2. **📝 Ingreso de contenido**
   - **Opción A**: Pegar texto directamente en el área de texto
   - **Opción B**: Cargar archivo `.txt` con múltiples mensajes
   
   *Ejemplo de texto a analizar:*
   ```
   "Nadie te quiere aquí. Mejor vete del grupo y no vuelvas más."
   ```

3. **🔍 Análisis automático**
   - Presionar botón **"Analizar Mensaje"**
   - El sistema procesa el texto con ambos algoritmos
   - Comparación contra base de datos de patrones

4. **📊 Visualización de resultados**
   - **Patrones detectados** con posición exacta
   - **Nivel de alerta** (🟢 Bajo, 🟡 Medio, 🔴 Alto)
   - **Recomendaciones específicas** de acción
   - **Estadísticas** del análisis

### 🎛️ Panel de Administración

- **Gestión de patrones**: Agregar, editar, eliminar
- **Configuración de alertas**: Ajustar niveles de gravedad
- **Historial de análisis**: Revisar casos anteriores

---

## 📈 Ejemplo de Resultados

**Texto analizado:**
> "No la inviten más, nadie la soporta, es una tonta."

**Detecciones:**
| Patrón | Posición | Tipo | Nivel | Algoritmo |
|--------|----------|------|-------|-----------|
| "nadie la soporta" | 17-32 | Exclusión social | 🟡 Medio | KMP |
| "tonta" | 39-43 | Insulto personal | 🔴 Alto | Boyer-Moore |

**Recomendación:** 
🚨 *Revisar inmediatamente con orientador escolar. Posible caso de acoso grupal.*

---

## 🧪 Casos de Prueba

El sistema incluye una batería completa de pruebas con:



---

## 🔮 Funcionalidades Avanzadas (Futuras Mejoras)

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

## 📞 Contacto

Para consultas sobre este proyecto académico:

- **Harry Guajan**: [email/contacto]
- **Joel Tinitana**: [email/contacto]

---

## 📄 Licencia

Este proyecto es desarrollado con fines académicos y educativos como parte del curso EDA II - Universidad [Nombre de la Universidad].

---

*"La tecnología al servicio de un entorno escolar más seguro e inclusivo"* 🎓✨
