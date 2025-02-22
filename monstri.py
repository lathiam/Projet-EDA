import pandas as pd
import streamlit as st
import seaborn as sns
import matplotlib.pyplot as plt
import io

# Fonction pour charger les données
def load_data():
    try:
        return pd.read_csv('bank.csv')
    except FileNotFoundError:
        st.error("Le fichier 'bank.csv' est introuvable. Assurez-vous qu'il est dans le même répertoire que ce script.")
        st.stop()

# Fonction pour afficher le contexte du projet
def show_context():
    st.title("Contexte du Projet")
    st.write(
        """
        Ce projet explore des données issues d'une campagne marketing bancaire.
        L'objectif est d'analyser les comportements des clients afin d'améliorer le ciblage marketing.
        """
    )
    st.image("campagne-marketing-banque.jpg")

# Fonction pour explorer les données
def explore_data(df):
    st.title("Exploration des Données")
    st.write("### Aperçu du dataset")
    st.dataframe(df.head())
    
    st.write("### Informations générales")
    buffer = io.StringIO()
    df.info(buf=buffer)
    st.text(buffer.getvalue())
    
    if st.checkbox("Afficher les valeurs manquantes"):
        st.write(df.isna().sum())
    
    if st.checkbox("Afficher les doublons"):
        st.write(f"Nombre de doublons : {df.duplicated().sum()}")

# Fonction pour analyser les données
def analyze_data(df):
    st.title("Analyse des Données")
    
    if st.checkbox("Statistiques descriptives de l'âge"):
        st.write(df['age'].describe())
        
        fig, ax = plt.subplots()
        sns.histplot(df['age'], kde=True, ax=ax)
        ax.set_title("Distribution de l'âge")
        st.pyplot(fig)
    
    if st.checkbox("Analyse de la variable 'job'"):
        job_counts = df['job'].value_counts()
        st.write(job_counts)
        
        fig, ax = plt.subplots()
        sns.barplot(x=job_counts.index, y=job_counts.values, ax=ax)
        ax.set_title("Distribution des métiers")
        ax.set_xlabel("Métier")
        ax.set_ylabel("Nombre de clients")
        plt.xticks(rotation=45)
        st.pyplot(fig)

# Interface Streamlit
st.sidebar.title("Navigation")
pages = {"Contexte": show_context, "Exploration": explore_data, "Analyse": analyze_data}
choix = st.sidebar.radio("Aller vers :", list(pages.keys()))

df = load_data()
pages[choix](df)
