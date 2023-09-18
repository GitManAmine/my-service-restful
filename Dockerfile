# Utilisez une image Python officielle en tant qu'image de base
FROM python:3.8-slim

# Définissez le répertoire de travail dans le conteneur
WORKDIR /app

# Copiez le fichier requirements.txt et installez les dépendances
COPY requirements.txt .
RUN pip install -r requirements.txt

# Copiez le reste de votre application dans le conteneur
COPY . .

# Exposez le port sur lequel votre application Flask écoute
EXPOSE 5000

# Démarrez votre application Flask lorsque le conteneur est démarré
CMD ["python", "app.py"]
