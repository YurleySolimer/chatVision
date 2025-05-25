# chatVision
openai course


<p align="center">
  ChatVision es un chatbot que puede responder preguntas en tiempo real, analizar múltiples imágenes y generar imágenes utilizando DALL·E 3
</p>


## 🚀 Instalación


1. Instala las dependencias de la interfaz web e inicia el servidor

Empieza desde la carpeta `ui`

```bash
cd ui
npm install
npm run dev
```

2. Crea el entorno virtual para la API

Empieza desde la carpeta `api`

```bash
cd api
python -m venv env
source env/bin/activate
```

3. Instala las dependencias de la API

Para este curso se utilizo la librería OpenAI en su versión 1.55.3.

```bash
pip install -r requirements.txt
```

4. Inicia el servidor de la API

```bash
python app.py
```



## 📚 Estructura del proyecto

ChatVision se compone de 2 partes: una interfaz web y una API. La interfaz web es una aplicación web basada en Next.js que nos permite interactuar con el chatbot. La API es un servidor en Flask que se encarga de procesar las solicitudes de la interfaz web y de interactuar con la librería de OpenAI para las siguientes funcionalidades:

- Respuesta a preguntas en tiempo real (vía streaming)
- Procesamiento de múltiples imágenes
- Generación de imágenes
