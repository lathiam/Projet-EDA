import streamlit as st
import pandas as pd
import io
import matplotlib.pyplot as plt
import seaborn as sns


df = pd.read_csv('bank.csv')
df.head(20)




df.info()


df['age'].describe()


sns.displot(df['age'], bins=20, kde=True) 


sns.boxplot(x='age', data=df)




# Assurez-vous que df (le DataFrame) est défini avant l'utilisation

# Titre de l'application
st.title('Analyse de la variable "âge"')

# Informations sur le dataset
st.write("## Informations sur le dataset")
buffer = io.StringIO()
df.info(buf=buffer)
s = buffer.getvalue()
st.text(s)

# Description de la variable "âge"
st.write("## Description de l'âge")
st.write(df['age'].describe())

# Distribution de l'âge
st.write("## Distribution de l'âge")
fig, ax = plt.subplots()
sns.histplot(df['age'], bins=20, kde=True, ax=ax)  # Correction: sns.histplot est mieux adapté pour Streamlit
st.pyplot(fig)

# Boxplot de l'âge
st.write("## Boxplot de l'âge")
fig, ax = plt.subplots()
sns.boxplot(x=df['age'], ax=ax)  # Correction: passage direct de la série df['age']
st.pyplot(fig)

# Analyse des données
st.write("## Analyse")
st.write("- L'âge minimum de nos clients est de 18 ans")
st.write("- L'âge maximum de nos clients est de 95 ans")
st.write("- L'âge moyen des clients est de 41 ans")
st.write("- 50% de nos clients ont moins de 39 ans inclu, et 70% de nos clients ont moins de 49 ans inclu")
