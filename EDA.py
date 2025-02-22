import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns

df = pd.read_csv('bank.csv')
df.head(20)

df.info()

# Analyse univariée variable continue

df['age'].describe()

sns.displot(df['age'], bins=20, kde=True) 

sns.boxplot(x='age', data=df)

df["balance"].describe().round(2)


# #Analyse

print("#Analyse")
print("- L'âge minimum de nos clients est de 18 ans")
print("- L'âge maximum de nos clients est de 95 ans")
print("- L'âge moyen des clients est de 41 ans")
print("- 50% de nos clients ont moins de 39 ans inclu et 70% de nos clients ont moins de 49 ans inclu")



df['duration'].describe()



sns.displot(df['duration'], bins=20, kde=True)
plt.title('Distribution de la durée des appels')
plt.xlabel('Durée des appels')
plt.ylabel('Nombre de clients') 


sns.boxplot(x='duration', data=df)
plt.title('Distribution de la durée des appels')



df['campaign'].describe()



sns.displot(df['campaign'], bins=20, kde=True)


sns.boxplot(x='campaign', data=df)


# Analyse univariée variable discrète


df['job'].value_counts()


sns.countplot(y='job', data=df, order = df['job'].value_counts().index)


print(df["marital"].value_counts())
df["marital"].value_counts().plot(kind='bar')



print(df["education"].value_counts())
df["education"].value_counts().plot(kind='bar')



print(df["default"].value_counts())
df["default"].value_counts().plot(kind='bar')



print(df["housing"].value_counts())
df["housing"].value_counts().plot(kind='bar')



print(df["loan"].value_counts())
df["loan"].value_counts().plot(kind='bar')



print(df["contact"].value_counts())
df["contact"].value_counts().plot(kind='bar')


print(df["poutcome"].value_counts())
df["poutcome"].value_counts().plot(kind='bar')


print(df["deposit"].value_counts())
df["deposit"].value_counts().plot(kind='bar')


# Analyse multivariée variables Continue-Continue


sns.scatterplot(x='age', y='balance', data=df)
plt.show()


sns.scatterplot(x='age', y='duration', data=df)
plt.show()



sns.scatterplot(x='age', y='campaign', data=df)
plt.show()


sns.scatterplot(x='balance', y='duration', data=df)
plt.show()

sns.scatterplot(x='balance', y='campaign', data=df)
plt.show()

sns.scatterplot(x='duration', y='campaign', data=df)
plt.show()


# Analyse multivariée discrète discrète

pd.crosstab(df['job'], df['deposit']).plot(kind='bar', stacked=True)



pd.crosstab(df['marital'], df['deposit'])
sns.heatmap(pd.crosstab(df['marital'], df['deposit']), annot=True, fmt='d')



pd.crosstab(df['education'], df['deposit'])
sns.heatmap(pd.crosstab(df['education'], df['deposit']), annot=True, fmt='d')


pd.crosstab(df['default'], df['deposit'])
sns.heatmap(pd.crosstab(df['default'], df['deposit']), annot=True, fmt='d')



pd.crosstab(df['housing'], df['deposit'])
sns.heatmap(pd.crosstab(df['housing'], df['deposit']), annot=True, fmt='d')


pd.crosstab(df['loan'], df['deposit'])
sns.heatmap(pd.crosstab(df['loan'], df['deposit']), annot=True, fmt='d')


pd.crosstab(df['contact'], df['deposit'])
sns.heatmap(pd.crosstab(df['contact'], df['deposit']), annot=True, fmt='d')


pd.crosstab(df['poutcome'], df['deposit'])
sns.heatmap(pd.crosstab(df['poutcome'], df['deposit']), annot=True, fmt='d')


pd.crosstab(df['job'], df['deposit'])
sns.heatmap(pd.crosstab(df['job'], df['deposit']), annot=True, fmt='d')


# Analyse multivariée Discrète continue

sns.pairplot(df, hue='deposit')
plt.show()




