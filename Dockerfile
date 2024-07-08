# Usa una imagen base oficial de Python
FROM python:3.9-slim

# Establece el directorio de trabajo en el contenedor
WORKDIR /app

# Copia el archivo de requisitos y el archivo de gestión en el directorio de trabajo
COPY requirements.txt /app/
COPY manage.py /app/

# Instala las dependencias del proyecto
RUN pip install --no-cache-dir -r requirements.txt

# Copia el resto del código de la aplicación al directorio de trabajo
COPY . /app/

# Expone el puerto que usará la aplicación
EXPOSE 8000

# Ejecuta los comandos de migración y carga de datos al iniciar el contenedor
RUN python manage.py migrate
RUN python manage.py load_books

# Comando por defecto para ejecutar la aplicación
CMD ["python", "manage.py", "runserver", "0.0.0.0:8000"]
