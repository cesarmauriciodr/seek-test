# Sistema de Gestión de Libros

Este proyecto implementa un backend para la gestión de información de libros utilizando Django, Django REST Framework, y MongoDB. Proporciona una API REST para realizar operaciones CRUD y una funcionalidad adicional para obtener el precio promedio de los libros publicados en un año específico.

## Requisitos

- Python 3.x
- MongoDB
- Django 3.x o superior
- Django REST Framework
- pymongo
- drf-yasg
- djangorestframework-simplejwt

## Instalación

1. Clona el repositorio:
    ```sh
    git clone https://github.com/cesarmauriciodr/seek-test.git
    cd seek-test
    ```

2. Crea un entorno virtual e instala las dependencias:
    ```sh
    python -m venv env
    source env/bin/activate
    pip install -r requirements.txt
    ```

3. Configura la base de datos MongoDB en `book_management/settings.py`:
    ```python
    DATABASES = {
        'default': {
            'ENGINE': 'djongo',
            'NAME': 'bookdb',
        }
    }
    ```

4. Ejecuta las migraciones y carga los datos iniciales:
    ```sh
    python manage.py migrate
    python manage.py load_books
    ```

5. Crea un superusuario para acceder al panel de administración de Django:
    ```sh
    python manage.py createsuperuser
    ```

6. Ejecuta el servidor de desarrollo:
    ```sh
    python manage.py runserver
    ```

### Uso con Docker

Para utilizar este proyecto con Docker, sigue los siguientes pasos:

1. Asegúrate de tener Docker instalado en tu sistema.

2. Clona el repositorio:
    ```sh
    git clone https://github.com/cesarmauriciodr/seek-test.git
    cd seek-test
    ```

3. Construye la imagen de Docker:
    ```sh
    docker build -t seek-test .
    ```

4. Crea un contenedor a partir de la imagen:
    ```sh
    docker run -d -p 8000:8000 --name seek-test-container seek-test
    ```

5. Accede a la aplicación en tu navegador web:
    ```
    http://localhost:8000
    ```

¡Listo! Ahora puedes utilizar la aplicación utilizando Docker.



### Autenticación

Primero, obtén un token de acceso mediante la API de autenticación:

1. Envia una solicitud POST a `/api/token/` con las credenciales del usuario:
    ```json
    {
        "username": "tu_usuario",
        "password": "tu_contraseña"
    }
    ```

2. Utiliza el token en el encabezado de las solicitudes para acceder a las APIs protegidas:
    ```
    Authorization: Bearer <tu_token>
    ```

### Endpoints

- **Listar todos los libros:**
    ```
    GET /api/books/
    ```

- **Crear un nuevo libro:**
    ```
    POST /api/books/
    {
        "title": "Nuevo Libro",
        "author": "Autor",
        "published_date": "2024-01-01",
        "genre": "Ficción",
        "price": "29.99"
    }
    ```

- **Obtener un libro por ID:**
    ```
    GET /api/books/{id}/
    ```

- **Actualizar un libro por ID:**
    ```
    PUT /api/books/{id}/
    {
        "title": "Libro Actualizado",
        "author": "Autor Actualizado",
        "published_date": "2024-01-01",
        "genre": "No Ficción",
        "price": "39.99"
    }
    ```

- **Eliminar un libro por ID:**
    ```
    DELETE /api/books/{id}/
    ```

- **Obtener el precio promedio de los libros publicados en un año específico:**
    ```
    GET /api/books/average_price/?year=2022
    ```

### Documentación de la API

La documentación Swagger de la API está disponible en:

    ```
    http://127.0.0.1:8000/swagger/
    ```
    
### Entregables:
- Repositorio de GitHub con el código fuente. [https://github.com/cesarmauriciodr/seek-test.git](https://github.com/cesarmauriciodr/seek-test.git)
- URL de la API desplegada en Amazon Web Services (AWS) (o en Azure o en GCP) usando los servicios en su capa free. (No desplegue el repositorio, no tengo posibilidad de desplegar en capa gratuita por el momento)
- Documentación de los endpoints en Swagger (disponible en pdf [swagger.pdf](swagger.pdf))
- Una colección en Postman con las llamadas a cada una de las APIs, incluyendo un par de casos ya grabados (uno con HTTP Status 200, exitoso y uno con 500, para caso de error) por cada endpoint.	(disponible en json file [postman.json](postman.json))
