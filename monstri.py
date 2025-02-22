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
    
    st.write("### Types de variables")
    numeric_cols = df.select_dtypes(include=['number']).columns.tolist()
    categorical_cols = df.select_dtypes(exclude=['number']).columns.tolist()
    st.write(f"Variables numériques : {numeric_cols}")
    st.write(f"Variables catégoriques : {categorical_cols}")

# Fonction pour analyser les données
def analyze_data(df):
    st.title("Analyse des Données")
    
    st.subheader("Analyse Univariée")
    variable_uni = st.selectbox("Choisissez une variable numérique :", df.select_dtypes(include=['number']).columns)
    if st.button("Afficher l'analyse univariée"):
        st.write(df[variable_uni].describe())
        fig, ax = plt.subplots()
        sns.histplot(df[variable_uni], kde=True, ax=ax)
        ax.set_title(f"Distribution de {variable_uni}")
        st.pyplot(fig)
    
    st.subheader("Analyse Bivariée")
    col_x = st.selectbox("Choisissez une variable numérique (axe X) :", df.select_dtypes(include=['number']).columns)
    col_y = st.selectbox("Choisissez une autre variable numérique (axe Y) :", df.select_dtypes(include=['number']).columns)
    if st.button("Afficher l'analyse bivariée"):
        fig, ax = plt.subplots()
        sns.scatterplot(x=df[col_x], y=df[col_y], ax=ax)
        ax.set_title(f"Relation entre {col_x} et {col_y}")
        st.pyplot(fig)
    
    st.subheader("Analyse des Variables Catégoriques")
    variable_cat = st.selectbox("Choisissez une variable catégorique :", df.select_dtypes(exclude=['number']).columns)
    if st.button("Afficher l'analyse des variables catégoriques"):
        count_data = df[variable_cat].value_counts()
        st.write(count_data)
        fig, ax = plt.subplots()
        sns.barplot(x=count_data.index, y=count_data.values, ax=ax)
        ax.set_title(f"Distribution de {variable_cat}")
        plt.xticks(rotation=45)
        st.pyplot(fig)

# Interface Streamlit
st.sidebar.title("Navigation")
pages = {"Contexte": show_context, "Exploration": explore_data, "Analyse": analyze_data}
choix = st.sidebar.radio("Aller vers :", list(pages.keys()))

df = load_data()
pages[choix](df)
