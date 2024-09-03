# Usa una imagen base oficial de Python
FROM python:3.9

# Establece el directorio de trabajo en /app
WORKDIR /app

# Copia el archivo requirements.txt en el directorio de trabajo
COPY ./todos/requirements.txt .

# Instala las dependencias
RUN pip install --no-cache-dir -r requirements.txt

# Copia el contenido del proyecto en el directorio de trabajo
COPY ./todos .

# Expone el puerto 80 para la aplicación
EXPOSE 80

# Comando para ejecutar la aplicación
CMD ["uvicorn", "api:app", "--host", "0.0.0.0", "--port", "80"]