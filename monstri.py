import pandas as pd 
import numpy as np 
import streamlit as st 
import seaborn as sns 
import matplotlib.pyplot as plt
import plotly.express as px


df = pd.read_csv('bank.csv')


st.sidebar.title("Sommaire")

pages = ["Contexte du projet", "Exploration des données", "Analyse de données"]

page = st.sidebar.radio("Aller vers la page :", pages)

if page == pages[0] : 
    
    st.write("### Contexte du projet")
    
    st.write("Ce projet s'inscrit dans un contexte de campagne marketing dans le secteur bancaire. L'objectif est d'explorer er analyser les données afin de decrire leurs comportements à partir de leurs données clients ainsi que d'autres données leurs caracterisant.Nous avons à notre disposition le fichier bank.csv qui contient des données clients. Chaque observation en ligne correspond à un client. Chaque variable en colonne est une caractéristique decrivant le client ainsi que ces activitées dans notre banque.Dans un premier temps, nous explorerons ce dataset. Puis nous l'analyserons visuellement pour en extraire des informations selon certains axes d'étude. Pour en tirer des conclusions qui vont nous permettre de mieux ciblé nos client lors de nos campagne marketing.")

    st.image("campagne-marketing-banque.jpg")
    
elif page == pages[1]:
    st.write("### Exploration des données")
    
    st.dataframe(df.head())
    
    st.write("Les informations sur notre dataset:")
    
    st.write(df.info())
    
    if st.checkbox("Afficher les valeurs manquantes") : 
        st.dataframe(df.isna().sum())
        
    if st.checkbox("Afficher les doublons") : 
        st.write(df.duplicated().sum())
        
elif page == pages[2]:
    st.write("### Analyse de données")
    st.checkbox("Les statistiques descriptives de la variable age")
    st.write(df['age'].describe())
    fig = sns.displot(x='age', data=df, kde=True)
    plt.title("Distribution de la variable age")
    st.pyplot(fig)
    
    fig = sns.boxplot(x='age', data=df)
    plt.title("boxplot de la variable age")
    st.pyplot(fig)
    
    
    st.checkbox("Observation lors de l'analyse de la variable age de nos clients")
    st.write("- L'âge minimum de nos clients est de 18 ans")
    st.write("- L'âge maximum de nos clients est de 95 ans")
    st.write("- L'âge moyen des clients est de 41 ans")
    st.write("- 50% de nos clients ont moins de 39 ans inclu et 75% de nos clients ont moins de 49 ans inclu")

    st.checkbox("Analyse de la variable job")
    st.write(df['job'].value_counts())
    fig = sns.countplot(x='job', data=df)
    plt.title("Distribution de la variable job")
    st.pyplot(fig)
    
    st.checkbox("Observation lors de l'analyse de la variable job de nos clients")
    st.write("- Les clients les plus representés sont les clients qui sont le management")
    st.write("- Les clients les plus representés sont les clients dont nous ne connaissons pas le métier")
    

