import streamlit as st
import openai
from dotenv import load_dotenv
import os

# Charger les variables d'environnement à partir du fichier .env
load_dotenv()

# Obtenez la clé API à partir de la variable d'environnement
openai.api_key = os.getenv('OPENAI_API_KEY')

st.title("Générateur d'Images en Langue Fon")

st.write("""
    Entrez une description en langue Fon de l'image que vous souhaitez générer.
    L'application utilisera l'API d'OpenAI pour créer l'image correspondante.
""")

# Champ de texte pour la description en langue Fon
description = st.text_area("Description en Fon")

# Bouton pour générer l'image
if st.button("Générer l'Image"):
    if description:
        try:
            # Appel à l'API d'OpenAI pour générer l'image
            response = openai.images.generate(
                prompt=description,
                n=1,
                size="512x512"
            )
            # Récupération de l'URL de l'image générée
            image_url = response['data'][0]['url']
            st.image(image_url, caption="Image Générée", use_column_width=True)
        except Exception as e:
            st.error(f"Erreur lors de la génération de l'image: {e}")
    else:
        st.error("Veuillez entrer une description en langue Fon.")
