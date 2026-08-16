# fastapi-store-api

Proyecto para el curso de FastAPI en la universidad. Este repositorio presenta una API REST construida con **FastAPI** para introducir conceptos clave de arquitectura REST, modelo cliente-servidor y desarrollo back-end.

## ¿Qué es Internet?
Internet es una red global de redes que permite que computadoras y dispositivos se comuniquen entre sí usando protocolos comunes. Gracias a Internet, una aplicación cliente (como un navegador o app móvil) puede conectarse a un servidor para solicitar y recibir información.

## ¿Qué es HTTP?
**HTTP (HyperText Transfer Protocol)** es el protocolo de comunicación más utilizado en la Web. Define cómo un cliente envía una solicitud (request) a un servidor y cómo el servidor responde (response).

En una API REST, HTTP es el canal por el que se intercambian recursos, normalmente en formato JSON.

## Arquitectura cliente-servidor
En el modelo cliente-servidor:

- **Cliente**: consume la API (frontend, app móvil, Postman, etc.).
- **Servidor**: procesa solicitudes, aplica lógica de negocio y responde datos (FastAPI en este proyecto).

Esta separación permite escalar, mantener y evolucionar cada parte de forma más clara.

## ¿Qué es el desarrollo back-end?
El desarrollo back-end se enfoca en la parte del sistema que no ve directamente el usuario:

- Definición de endpoints y reglas de negocio.
- Validación de datos.
- Conexión con bases de datos.
- Seguridad y control de acceso.
- Manejo de errores y respuestas HTTP.

FastAPI facilita este trabajo gracias a su rendimiento, tipado con Python y documentación automática.

## Métodos HTTP principales en una API REST

- **GET**: obtener recursos (lectura).
- **POST**: crear nuevos recursos.
- **PUT**: reemplazar un recurso completo.
- **PATCH**: actualizar parcialmente un recurso.
- **DELETE**: eliminar un recurso.

Ejemplo conceptual para una tienda:

- `GET /products` → lista productos.
- `POST /products` → crea un producto.
- `GET /products/{id}` → obtiene un producto específico.
- `PATCH /products/{id}` → actualiza campos del producto.
- `DELETE /products/{id}` → elimina el producto.

## Códigos de estado HTTP comunes

- **200 OK**: solicitud exitosa.
- **201 Created**: recurso creado correctamente.
- **204 No Content**: éxito sin contenido de respuesta.
- **400 Bad Request**: solicitud inválida.
- **401 Unauthorized**: falta autenticación válida.
- **403 Forbidden**: acceso denegado.
- **404 Not Found**: recurso no encontrado.
- **422 Unprocessable Entity**: datos válidos en formato, pero con errores de validación (muy común en FastAPI).
- **500 Internal Server Error**: error inesperado del servidor.

## Objetivo académico del proyecto
Este proyecto sirve como introducción práctica a:

1. Creación de APIs REST con FastAPI.
2. Uso correcto de métodos HTTP.
3. Interpretación de códigos de estado.
4. Comprensión de la comunicación cliente-servidor.
5. Fundamentos del desarrollo back-end.

## Pasos para correr el proyecto (guía para estudiantes)

### 1) Clonar el repositorio
```bash
git clone https://github.com/itsronalds/fastapi-store-api.git
cd fastapi-store-api
```

### 2) Crear el entorno virtual (`.venv`)
```bash
python -m venv .venv
```

### 3) Activar el entorno virtual
En **Windows (PowerShell)**:
```bash
.venv\Scripts\Activate.ps1
```

En **macOS/Linux**:
```bash
source .venv/bin/activate
```

### 4) Instalar todas las librerías
```bash
pip install -r requirements.txt
```

### 5) Iniciar el proyecto
```bash
uvicorn src.app:app --reload
```

### 6) Probar en el navegador
- API: `http://127.0.0.1:8000`
- Documentación automática: `http://127.0.0.1:8000/docs`
