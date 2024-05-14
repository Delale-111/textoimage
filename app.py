import streamlit as st
import openai

# Remplacez 'your_openai_api_key_here' par votre clé API OpenAI réelle
openai.api_key = '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'

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
