# ProDAM

ProDAM es un sistema de análisis de datos diseñado específicamente para la industria manufacturera. Proporciona visualizaciones interactivas y modelos de machine learning para ayudar en la toma de decisiones y la mejora de la productividad en diferentes departamentos de una fábrica.

<img width="1728" alt="image" src="https://github.com/D-Arenas/Project-1-analitica/assets/68788933/7461861e-3806-47d3-9a4e-e2804c33244a">
<img width="1713" alt="image" src="https://github.com/D-Arenas/Project-1-analitica/assets/68788933/1f4c4441-f5f9-49fc-856e-08505814172e">

## Instalación

1. Clona este repositorio en una instancia EC2 de AWS.
2. Ejecuta `DevOps/setup.sh`.
3. (Opcional) Configura `cron` siguiendo los pasos en `DevOps/crono_pull.sh`.

## Estructura de Directorios

- Business Analysis: Documentos relacionados con el análisis de negocio.
- Business Context: Información contextual sobre el negocio y la industria.
- Dashboard: Código fuente para el panel de visualización.
- Data Analysis: Archivos y scripts relacionados con el análisis de datos.
- Data Engineering: Scripts para la ingeniería y limpieza de datos.
- Data Science: Modelos de machine learning y análisis predictivo.
- DevOps: Configuración y scripts de despliegue.
- Results: Resultados y conclusiones obtenidas del análisis.

## Uso

1. Ejecuta el servidor del panel de visualización con `screen -S dashboard_session -d -m python app.py`.
2. Abre un navegador web y navega a `http://<EC2_PUBLIC_IP>:8050` para acceder al panel de ProDAM.

## Funcionalidades

- Visualización de la distribución de la productividad según la cantidad de incentivos.
- Análisis comparativo de la productividad real y esperada por equipo y por departamento.
- Representación de la relación entre el tiempo asignado a la tarea y la productividad real.
- Modelos de machine learning para predecir la productividad en los departamentos de Sweing y Finishing.

## Autores

- Daniela Arenas - k.arenas@uniandes.edu.co
- Haider Fonseca - h.fonseca@uniandes.edu.co
- Sebastian Urrea - js.urrea@uniandes.edu.co

## Licencia

Este proyecto está bajo la Licencia MIT - ver el archivo LICENSE para más detalles.
