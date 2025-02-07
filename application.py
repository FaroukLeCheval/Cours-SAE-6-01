"""
📝 **Instructions** :
- Installez toutes les bibliothèques nécessaires en fonction des imports présents dans le code, utilisez la commande suivante :conda create -n projet python pandas numpy ..........
- Complétez les sections en écrivant votre code où c’est indiqué.
- Ajoutez des commentaires clairs pour expliquer vos choix.
- Utilisez des emoji avec windows + ;
- Interprétez les résultats de vos visualisations (quelques phrases).
"""

### 1. Importation des librairies et chargement des données
# import os
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
import streamlit as st
import plotly.express as px

# Chargement des données
try:
    df_salaire = pd.read_csv("C:/projet_notebook/ds_salaries.csv")
    #df_salaire['work_year'] = df_salaire['work_year'].replace(",","")
    #df_salaire['work_year_clear'] = pd.to_datetime(df_salaire['work_year'], format='%Y').dt.year
    #df_salaire['work_year'].astype('str')
    #df_salaire = df_salaire[(df_salaire['salary'] <= 15000000)]
except FileNotFoundError:
    st.error("Erreur: Le fichier 'ds_salaries.csv' n'a pas été trouvé. Veuillez vérifier qu'il est bien présent dans le répertoire.")
    st.stop()
except Exception as e:
    st.error(f"Une erreur s'est produite lors du chargement des données: {str(e)}")
    st.stop()

### 2. Exploration visuelle des données
st.title("📊 Visualisation des Salaires en Data Science")
st.markdown("Explorez les tendances des salaires à travers différentes visualisations interactives.")

if st.checkbox("Afficher un aperçu des données"):
    st.write(df_salaire)


#Statistique générales avec describe pandas 
st.subheader("📌 Statistiques générales")
st.write(df_salaire.describe())


### 3. Distribution des salaires en France par rôle et niveau d'expérience, uilisant px.box et st.plotly_chart

df_tmp = df_salaire[df_salaire['employee_residence'] == 'FR']
st.subheader("📈 Distribution des salaires en France")
#fig = px.box(df_tmp, x="experience_level", y="salary", color="job_title")
fig = px.box(df_tmp, x="job_title", y="salary", color="experience_level",
            title="Distribution des salaires en France par rôle et niveau d'expérience")
st.plotly_chart(fig)

### 4. Analyse des tendances de salaires :
#### Salaire moyen par catégorie : en choisisant une des : ['experience_level', 'employment_type', 'job_title', 'company_location'], utilisant px.bar et st.selectbox 

selected = st.selectbox(label="Choix de la variable", options=['experience_level','employment_type','job_title','company_location'])
#st.write(selected)

fig = px.bar(df_salaire, x=selected, y='salary')
st.plotly_chart(fig)

### 5. Corrélation entre variables
# Sélectionner uniquement les colonnes numériques pour la corrélation

numeric_df = df_salaire.select_dtypes(include=[np.number])
#st.write(numeric_df)

# Calcul de la matrice de corrélation
matrix = numeric_df.corr()
#st.write(matrix)

# Affichage du heatmap avec sns.heatmap
st.subheader("🔗 Corrélations entre variables numériques")
plot = sns.heatmap(matrix, annot=True, cmap='coolwarm')
st.pyplot(plot.get_figure())

### 6. Analyse interactive des variations de salaire
# Une évolution des salaires pour les 10 postes les plus courants
# count of job titles pour selectionner les postes
# calcule du salaire moyen par an
#utilisez px.line

top_poste = df_salaire['job_title'].value_counts().head(10)
top_poste = list(top_poste.index)
#st.write(top_poste)

x = df_salaire[df_salaire["job_title"].isin(top_poste)]
salary_evolution = x.groupby(['work_year', 'job_title'])['salary_in_usd'].mean().reset_index()
fig = px.line(salary_evolution, x='work_year', y='salary_in_usd', color='job_title', title='Évolution des salaires moyens (USD) par poste',
               labels={
                   'work_year': 'Année',
                   'salary_in_usd': 'Salaire moyen (USD)',
                   'job_title': 'Poste'
               })

st.plotly_chart(fig)

x = df_salaire[df_salaire["job_title"].isin(top_poste)]
salary_evolution = x.groupby(['work_year', 'job_title'])['salary'].mean().reset_index()
fig = px.line(salary_evolution, x='work_year', y='salary', color='job_title', title='Évolution des salaires moyens par poste',
               labels={
                   'work_year': 'Année',
                   'salary_in_usd': 'Salaire moyen',
                   'job_title': 'Poste'
               })

st.plotly_chart(fig)


### 7. Salaire médian par expérience et taille d'entreprise

fig = px.bar(df_salaire.groupby('company_size')['salary'].median(), title="Salaire médian par expérience et taille d'entreprise")
st.plotly_chart(fig)

### 8. Ajout de filtres dynamiques
#Filtrer les données par salaire utilisant st.slider pour selectionner les plages 

selected = st.slider(label='Choix de la plage des salaires', value=[df_salaire['salary'].min(), df_salaire['salary'].max()])
min_select = selected[0]
max_select = selected[1]
df_tmp = df_salaire[(df_salaire['salary'] >= min_select) & (df_salaire['salary'] <= max_select)]
st.write(df_tmp)

### 9.  Impact du télétravail sur le salaire selon le pays

impact = df_salaire.groupby("company_location").apply(lambda x: x["remote_ratio"].corr(x["salary"]))
st.write(impact)

### 10. Filtrage avancé des données avec deux st.multiselect, un qui indique "Sélectionnez le niveau d'expérience" et l'autre "Sélectionnez la taille d'entreprise"
#votre code 

lvl_ent = st.multiselect(
    "Sélectionnez le niveau d'expérience",
    df_salaire['experience_level'].unique(),
    default=df_salaire['experience_level'].unique()
)
size_ent = st.multiselect(
    "Sélectionnez la taille d'entreprise",
    df_salaire['company_size'].unique(),
    default=df_salaire['company_size'].unique()
)

df_tmp = df_salaire[(df_salaire['experience_level'].isin(lvl_ent)) & (df_salaire['company_size'].isin(size_ent))]
st.write(df_tmp)
