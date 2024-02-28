# Usa la imagen oficial de Python
FROM python:3.9

# Establece el directorio de trabajo
WORKDIR /app

# Copia el archivo de requisitos al contenedor
COPY requirements.txt .

# Instala las dependencias
RUN pip install --no-cache-dir -r requirements.txt

# Copia el resto de la aplicación al contenedor
COPY . .

# Expone el puerto en el que la aplicación va a ejecutarse
EXPOSE 8000