import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import streamlit as st
import joblib
import pickle
import plotly.express as px


#Préparation d'une fonction pour le chargement de mon modèle
@st.cache_resource
def load_model():
    url_model = r"models/model_lr.pkl"
    model = joblib.load(url_model)
    return model

pipeline_model = load_model()

#Interface de l'application
#Titre
st.title("Analyse de sentiment")
st.write("Saisissez un texte et obtenez la prédiction du modèle.")

#Champ de texte pour la saisi
text = st.text_area("Votre texte", height = 150)

emotion_map = {
    0: "Tristesse",
    1: "Joie",
    2: "Amour",
    3: "Colère",
    4: "Peur",
    5: "Surprise"
}


#touche pour faire Prediction
if st.button("Analyser"):
    if text.strip():
        #Création d'un dataframe pour le modèle
        df_test = pd.DataFrame(data = {"text": [text]})
        
        #Prédiction
        pred = pipeline_model.predict(df_test[["text"]])
        probabilities = pipeline_model.predict_proba(df_test[["text"]])[0]
        proba_df = pd.DataFrame({"Emotion" : pipeline_model.classes_,
                                 "Probabilité": probabilities})

        #On récupère la vraie valeur
        classe = pred[0]
        emotion = emotion_map[classe]
        confidence = probabilities.max()

        fig = px.bar(proba_df, x = "Probabilité", y = "Emotion", orientation = "h",                text_auto = ".1%")
        fig.update_layout(xaxis_title = "Probabilité", yaxis_title = "Emotion")

        st.subheader("Résultat")
        st.write(f" Classe prédite : {emotion.upper()}")

        #st.bar_chart(proba_df.set_index("Emotion"))
        st.plotly_chart(fig, use_container_width = True)

        st.metric("Confiance du modèle ", f"{confidence: .2%}")
        
    else:
        st.warning("Saisissez le texte.")
