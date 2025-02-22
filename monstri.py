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
        Ce projet s'inscrit dans un contexte de campagne marketing dans le secteur bancaire.
        Les banques lancent régulièrement des campagnes pour promouvoir leurs produits auprès de clients potentiels.
        
        L'objectif principal de ce projet est d'explorer et d'analyser les données clients afin de mieux comprendre
        leur comportement et leurs préférences. Grâce à cette analyse, nous pourrons identifier des tendances et des
        profils types permettant d'optimiser le ciblage marketing.
        
        Nous utilisons un dataset intitulé `bank.csv` qui contient diverses informations sur les clients : 
        données démographiques, profession, statut marital, historique bancaire, etc. L'analyse de ces données
        nous aidera à répondre aux questions suivantes :
        
        - Quels sont les profils des clients les plus susceptibles d'accepter une offre ?
        - Quels facteurs influencent leur décision ?
        - Quelles sont les tendances générales observées ?
        
        En combinant exploration des données et visualisation, nous pourrons extraire des insights utiles à l'amélioration
        des stratégies marketing.
        """
    )
    st.image("campagne-marketing-banque.jpg")

# Fonction pour explorer les données
def explore_data():
    df = load_data()
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
def analyze_data():
    df = load_data()
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

# Fonction pour afficher la conclusion
def show_conclusion():
    st.title("Conclusion")
    st.write(
        """
        Grâce à cette analyse, nous avons pu mieux comprendre le profil des clients et leurs comportements. 
        L'exploration des variables a permis d'identifier des tendances clés qui aideront à affiner les campagnes marketing.
        
        - L'analyse univariée a mis en évidence des tendances démographiques et des distributions intéressantes.
        - L'analyse bivariée a révélé des corrélations entre certaines caractéristiques.
        - L'étude des variables catégoriques a permis d'identifier les segments clients les plus représentés.
        
        Ces insights pourront être utilisés pour optimiser les futures stratégies marketing et améliorer le ciblage des offres bancaires.
        """
    )

# Interface Streamlit
st.sidebar.title("Navigation")
pages = {"Contexte": show_context, "Exploration": explore_data, "Analyse": analyze_data, "Conclusion": show_conclusion}
choix = st.sidebar.radio("Aller vers :", list(pages.keys()))

pages[choix]()
