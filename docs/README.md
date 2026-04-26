# 🎬 Cinespoiler API

**Cinespoiler API** es una API REST desarrollada con **Django** y **Django REST Framework** para la gestión de películas en un sistema de cine.

Este proyecto fue diseñado bajo una estructura clara, organizada y escalable, permitiendo administrar registros de películas mediante operaciones CRUD, integrar el panel administrativo de Django y consumir los recursos desde la interfaz navegable del framework.

Su desarrollo tiene como objetivo aplicar buenas prácticas en la construcción de servicios backend, manteniendo un código limpio, modular y fácil de mantener.

---

## 📌 Tabla de contenido

- [Descripción general](#-descripción-general)
- [Objetivos del proyecto](#-objetivos-del-proyecto)
- [Funcionalidades principales](#-funcionalidades-principales)
- [Tecnologías utilizadas](#-tecnologías-utilizadas)
- [Capturas del proyecto](#-capturas-del-proyecto)
- [Estructura del proyecto](#-estructura-del-proyecto)
- [Arquitectura general](#-arquitectura-general)
- [Instalación y ejecución](#-instalación-y-ejecución)
- [Estado actual](#-estado-actual)
- [Posibles mejoras](#-posibles-mejoras)
- [Autor](#-autor)

---

## 📖 Descripción general

**Cinespoiler API** es una solución backend enfocada en la administración de películas dentro de un entorno tipo cine.  
Permite registrar, consultar, actualizar y eliminar películas mediante endpoints REST, facilitando la gestión de la información desde distintos puntos del sistema.

Además, el proyecto incorpora el uso del panel de administración de Django, lo que permite realizar tareas de mantenimiento y gestión de registros de manera rápida y visual.

Gracias a Django REST Framework, también es posible probar los endpoints desde una interfaz navegable, haciendo más simple el proceso de desarrollo, validación y demostración del funcionamiento de la API.

---

## 🎯 Objetivos del proyecto

Los principales objetivos de este proyecto son:

- Desarrollar una API REST funcional utilizando **Django** y **Django REST Framework**
- Aplicar operaciones **CRUD** sobre una entidad principal
- Implementar una estructura de proyecto ordenada y reutilizable
- Utilizar serializadores para transformar datos entre objetos y JSON
- Gestionar datos desde el panel administrativo de Django
- Sentar una base sólida para futuras ampliaciones del sistema

---

## ⚙️ Funcionalidades principales

Actualmente, el sistema permite:

- Registrar nuevas películas
- Listar todas las películas disponibles
- Consultar el detalle de una película específica
- Editar información de películas existentes
- Eliminar registros de películas
- Gestionar datos desde el panel de administración
- Consumir la API desde la interfaz navegable de Django REST Framework
- Obtener respuestas en formato JSON

---

## 🚀 Tecnologías utilizadas

Este proyecto fue desarrollado con las siguientes tecnologías:

- **Python**
- **Django**
- **Django REST Framework**
- **SQLite**
- **Git**
- **GitHub**

---

## 🖼️ Capturas del proyecto

A continuación, se muestran algunas capturas que evidencian el funcionamiento del sistema:

### API Root
![API Root](docs/incio.png)

### Registro de películas
![Registro de películas](docs/movie_list_post.png)

### Edición de películas
![Edición de películas](docs/movie_delete.png)

### Listado de películas
![Listado de películas](docs/movie_list.png)

### Respuesta de la API en formato JSON
![Respuesta JSON](docs/json.png)

### Panel de administración
![Panel de administración](docs/admin.png)

---

## 📂 Estructura del proyecto

```bash
Cinespoiler/
├── .gitignore
├── manage.py
├── README.md
├── requirements.txt
├── config/
│   ├── __init__.py
│   ├── asgi.py
│   ├── settings.py
│   ├── urls.py
│   └── wsgi.py
└── movies/
    ├── __init__.py
    ├── admin.py
    ├── apps.py
    ├── migrations/
    ├── models.py
    ├── serializers.py
    ├── tests.py
    ├── urls.py
    └── views.py