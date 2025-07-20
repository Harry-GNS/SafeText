#!/usr/bin/env python
"""
Archivo de entrada para Railway - SafeText optimizado para usar créditos eficientemente
"""

from app import app
import os

if __name__ == "__main__":
    # Railway asigna automáticamente el puerto
    port = int(os.environ.get("PORT", 5000))
    
    # Configuración optimizada para Railway:
    # - debug=False para producción
    # - host="0.0.0.0" para acceso público
    # - threaded=True para mejor rendimiento
    app.run(
        host="0.0.0.0", 
        port=port, 
        debug=False,
        threaded=True
    )
