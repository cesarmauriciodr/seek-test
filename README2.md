# Reto de Codificación

**Posición**: Backend Developer (Django + MongoDB + Cloud)

**Título**: Sistema de Gestión de Libros

## Contexto:
Desarrollar el backend de una aplicación que gestiona información de libros utilizando MongoDB como base de datos. La aplicación debe proporcionar una API REST utilizando Django DRF para realizar operaciones CRUD en la base de datos y realizar agregaciones mediante pipelines de MongoDB para obtener información específica.

## Requerimientos:
- Utiliza el paquete pymongo para la integración con MongoDB.
- Crea un modelo `Book` con al menos los siguientes campos: `title`, `author`, `published_date`, `genre`, `price`.
- Configura una API REST para realizar operaciones CRUD en el modelo `Book`.
- Implementa un endpoint adicional que utilice un aggregation pipeline de MongoDB para obtener el precio promedio de los libros publicados en un año específico.
- Proporciona datos de prueba iniciales para al menos 5 libros utilizando un script de migración para la BD (podrías usar un ORM de Django para esto).

## Puntos adicionales:
- Implementa autenticación de usuarios utilizando Token Authentication y proteger las APIs con este token.
- Agregar paginación a la API REST.
- Utiliza serializers personalizados para la representación de datos.
- Implementar pruebas unitarias para al menos dos funciones clave.

## Recomendaciones:
- Incluye instrucciones claras sobre cómo configurar y ejecutar la aplicación.
- Asegúrate de que el código sea legible y siga las mejores prácticas de desarrollo.
- Valora la implementación correcta de los pipelines de agregación de MongoDB.
- Considera la modularidad y reutilización del código.
- Proporciona comentarios en el código donde sea necesario.

## Duración del Reto:
- El reto debe ser entregado máximo 48 horas luego de haber recibido el reto por email.

## Entregables:
- Repositorio de GitHub con el código fuente.
- URL de la API desplegada en Amazon Web Services (AWS) (o en Azure o en GCP) usando los servicios en su capa free.
- Documentación de los endpoints en Swagger.
- Una colección en Postman con las llamadas a cada una de las APIs, incluyendo un par de casos ya grabados (uno con HTTP Status 200, exitoso y uno con 500, para caso de error) por cada endpoint.
