# 🎬 Cinespoilers API

**Cinespoilers API** es una API REST desarrollada con **Django** y **Django REST Framework** para la gestión de películas y géneros en un sistema de cine.

El proyecto permite administrar películas, registrar géneros cinematográficos y relacionar una película con varios géneros mediante una relación muchos a muchos.

Además, cuenta con el panel administrativo de Django y con la interfaz navegable de Django REST Framework para probar los endpoints de forma visual.

> Proyecto colaborativo **Carlos Carbajal**, **Sarai Soto** y **Eduardo Quiquia**

---

## 📌 Tabla de contenido

- [Descripción general](#-descripción-general)
- [Objetivos del proyecto](#-objetivos-del-proyecto)
- [Funcionalidades principales](#-funcionalidades-principales)
- [Tecnologías utilizadas](#-tecnologías-utilizadas)
- [Capturas del proyecto](#-capturas-del-proyecto)
- [Endpoints principales](#-endpoints-principales)
- [Evidencias de endpoints](#-evidencias-de-endpoints)
- [Ejemplos de uso](#-ejemplos-de-uso)
- [Estructura del proyecto](#-estructura-del-proyecto)
- [Instalación y ejecución](#-instalación-y-ejecución)
- [Estado actual](#-estado-actual)
- [Posibles mejoras](#-posibles-mejoras)
- [Autor](#-autor)

---

## 📖 Descripción general

**Cinespoilers API** es una solución backend enfocada en la administración de películas dentro de un sistema de cine.

Permite registrar, consultar, actualizar y eliminar películas mediante endpoints REST. También permite registrar géneros cinematográficos como acción, drama, terror o comedia, y asociarlos a una o varias películas.

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

A continuación, se muestran capturas del funcionamiento en diferentes perspectivas.

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

## 🖼️ Evidencias de endpoints

En esta sección se muestran las capturas de las pruebas realizadas en los endpoints de la API.

### 1. POST Genre

Permite crear un nuevo género.

![POST Genre](docs/endpoints/post%20genre.png)

---

### 2. GET Movie con relación de géneros

Permite visualizar una película junto con sus géneros relacionados.

![GET Movie con relación](docs/endpoints/get%20movie%20relacion.png)

---

### 3. POST Movie

Permite crear una nueva película y relacionarla con géneros existentes.

![POST Movie](docs/endpoints/post%20movie.png)

---

### 4. GET Movie

Permite listar las películas registradas.

![GET Movie](docs/endpoints/get%20movie.png)

---

### 5. PUT Movie

Permite actualizar completamente la información de una película.

![PUT Movie](docs/endpoints/put%20movie.png)

---

### 6. Detalle de Movie

Permite consultar la información de una película específica.

![Detalle de Movie](docs/endpoints/movie%20intace.png)

# Eduardo Quiquia - Evidencias

## Listar peliculas
** Ruta: GET /api/movies/
![GET movie](docs/eduardo/image.png)

## Crear pelicula
**Ruta: POST /api/movies/
![POST movie](docs/eduardo/moviegk.png)

## Actualizar pelicula
**Ruta: PUT /api/movies/4
![PUT movie](docs/eduardo/updategk.png)

## Eliminar pelicula
**Ruta: DELETE /api/movies/4
![DELETE movie](docs/eduardo/deletegk.png)

## Data Base - MOVIES
![TABLA MOVIES](docs/eduardo/db_movies.png)

## Listar genres
** Ruta: GET /api/genres/
![GET genres](docs/eduardo/genres.png)

## Crear genres
**Ruta: POST /api/genres/
![POST genres](docs/eduardo/genre1.png)
![POST genres](docs/eduardo/genre2.png)

## Actualizar genre
**Ruta: PUT /api/genres/1
![PUT genre](docs/eduardo/genret.png)

## Eliminar genre
**Ruta: DELETE /api/genres/1
![DELETE movie](docs/eduardo/genredelete.png)

## Data Base - MOVIES
![TABLA GENRES](docs/eduardo/db_genres.png)