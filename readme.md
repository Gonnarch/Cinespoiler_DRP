# 🎬 Cinespoilers API

**Cinespoilers API** es una API REST desarrollada con **Django** y **Django REST Framework** para la gestión de películas y géneros en un sistema de cine.

El proyecto permite administrar películas, registrar géneros cinematográficos y relacionar una película con varios géneros mediante una relación muchos a muchos.

Además, cuenta con el panel administrativo de Django y la interfaz navegable de Django REST Framework para probar los endpoints de forma visual.

---

## 📌 Tabla de contenido

- [Descripción general](#-descripción-general)
- [Objetivos del proyecto](#-objetivos-del-proyecto)
- [Funcionalidades principales](#-funcionalidades-principales)
- [Tecnologías utilizadas](#-tecnologías-utilizadas)
- [Capturas del proyecto](#-capturas-del-proyecto)
- [Endpoints principales](#-endpoints-principales)
- [Estructura del proyecto](#-estructura-del-proyecto)
- [Instalación y ejecución](#-instalación-y-ejecución)
- [Estado actual](#-estado-actual)
- [Posibles mejoras](#-posibles-mejoras)
- [Autor](#-autor)

---

## 📖 Descripción general

**Cinespoilers API** es una solución backend enfocada en la administración de películas dentro de un sistema de cine.

Permite registrar, consultar, actualizar y eliminar películas mediante endpoints REST. También permite registrar géneros como acción, drama, terror o comedia, y asociarlos a una o varias películas.

El proyecto utiliza **Django REST Framework**, lo que facilita la creación de una API limpia, ordenada y fácil de probar desde el navegador.

---

## 🎯 Objetivos del proyecto

Los principales objetivos de este proyecto son:

- Desarrollar una API REST funcional usando Django y Django REST Framework.
- Aplicar operaciones CRUD sobre películas.
- Crear una entidad `Genre` para administrar géneros.
- Relacionar `Movie` y `Genre` mediante una relación muchos a muchos.
- Utilizar serializers para transformar datos entre objetos Python y JSON.
- Gestionar datos desde el panel administrativo de Django.
- Probar los endpoints desde la Browsable API.
- Mantener una base simple y ordenada para futuras mejoras.

---

## ⚙️ Funcionalidades principales

Actualmente, el sistema permite:

- Registrar nuevas películas.
- Listar todas las películas.
- Consultar el detalle de una película.
- Editar información de películas.
- Eliminar películas.
- Registrar géneros.
- Listar géneros disponibles.
- Consultar el detalle de un género.
- Editar y eliminar géneros.
- Relacionar una película con varios géneros.
- Gestionar películas y géneros desde el panel de administración.
- Consumir la API desde la interfaz navegable de Django REST Framework.
- Obtener respuestas en formato JSON.

---

## 🚀 Tecnologías utilizadas

Este proyecto fue desarrollado con las siguientes tecnologías:

- Python
- Django
- Django REST Framework
- SQLite
- Git
- GitHub

---

## 🖼️ Capturas del proyecto


A continuación, se muestran capturas del funcionamiento del sistema.


## Carlos Carbajal

### Panel de administración

![Panel de administración](docs/admin.png)

### Listado de géneros

![Listado de géneros](docs/genre%20list.png)

### Detalle de género

![Detalle de género](docs/genre%20instance.png)

### Respuesta JSON de géneros

![Respuesta JSON de géneros](docs/genre%20list%20json.png)

### Listado de películas

![Listado de películas](docs/movie%20list.png)

### Detalle de película

![Detalle de película](docs/movie%20instance.png)

### Respuesta JSON de películas

![Respuesta JSON de películas](docs/movie%20list%20json.png)

---

## 🔗 Endpoints principales

### Movies

| Método | Endpoint | Descripción |
|---|---|---|
| GET | `/api/movies/` | Lista todas las películas |
| POST | `/api/movies/` | Crea una nueva película |
| GET | `/api/movies/{id}/` | Muestra el detalle de una película |
| PUT | `/api/movies/{id}/` | Actualiza una película completa |
| PATCH | `/api/movies/{id}/` | Actualiza parcialmente una película |
| DELETE | `/api/movies/{id}/` | Elimina una película |

### Genres

| Método | Endpoint | Descripción |
|---|---|---|
| GET | `/api/genres/` | Lista todos los géneros |
| POST | `/api/genres/` | Crea un nuevo género |
| GET | `/api/genres/{id}/` | Muestra el detalle de un género |
| PUT | `/api/genres/{id}/` | Actualiza un género completo |
| PATCH | `/api/genres/{id}/` | Actualiza parcialmente un género |
| DELETE | `/api/genres/{id}/` | Elimina un género |

---

## 📌 Ejemplo de creación de género

Endpoint:

```http
POST /api/genres/