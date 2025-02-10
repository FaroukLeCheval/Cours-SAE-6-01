Projet Jupyter Notebook et Application Streamlit

📅 Travail réalisé le 04/02/2025

Ce projet a pour objectif d'explorer les tendances salariales dans le domaine de la Data Science en utilisant Jupyter Notebook et une application interactive développée avec Streamlit.

📌 Objectifs du projet

Importer et analyser un dataset de salaires en Data Science.

Visualiser les tendances salariales en fonction de plusieurs critères.

Explorer les relations entre différents facteurs (expérience, télétravail, localisation, etc.).

Développer une application interactive permettant d'explorer les données de manière dynamique.

📝 Instructions d'installation

📌 Prérequis

Assurez-vous d'avoir installé toutes les bibliothèques nécessaires avant d'exécuter le projet. Vous pouvez créer un environnement Conda en exécutant la commande suivante :

conda create -n projet python pandas numpy matplotlib seaborn streamlit plotly

📂 Structure du projet

projet_notebook.ipynb : Analyse et visualisation des données en Jupyter Notebook.

app.py : Application Streamlit interactive pour explorer les données.

ds_salaries.csv : Fichier de données contenant les informations sur les salaires.

🔍 Analyse exploratoire des données

📥 Importation et lecture des données

Chargement du fichier ds_salaries.csv

Gestion des erreurs en cas d'absence du fichier

📊 Visualisation et statistiques générales

Affichage d'un aperçu des données

Statistiques descriptives générales

Distribution des salaires en France par rôle et niveau d'expérience

Évolution des salaires pour les postes les plus courants

📈 Analyse des tendances salariales

Salaire moyen par expérience, type de contrat, rôle et localisation

Corrélation entre différentes variables

Impact du télétravail sur le salaire

Salaire médian par taille d'entreprise

🎛️ Filtres dynamiques

Sélection de plages de salaires via un st.slider

Filtrage avancé par niveau d'expérience et taille d'entreprise via st.multiselect

🖥️ Fonctionnalités de l'application Streamlit

🚀 Interactivité et visualisation

L'application permet aux utilisateurs d'interagir avec les données grâce à plusieurs outils :

✅ Aperçu des données : possibilité d'afficher le dataset brut.

📌 Statistiques descriptives : affichage des mesures statistiques principales.

📈 Visualisations dynamiques :

Graphiques boxplot pour la distribution des salaires en fonction des rôles et de l'expérience.

Graphiques en barres pour comparer les salaires moyens selon différents critères.

Carte thermique (heatmap) pour visualiser les corrélations entre variables numériques.

Courbes d'évolution des salaires pour les 10 postes les plus courants.

🎚️ Filtres dynamiques :

Sélection de plages de salaire avec un st.slider

Choix du niveau d'expérience et de la taille d'entreprise avec st.multiselect

Exploration des impacts du télétravail sur les salaires par pays

📌 Exécution de l'application Streamlit

Pour exécuter l'application, ouvrez un terminal dans le répertoire du projet et tapez :

streamlit run app.py

L'application s'ouvrira dans votre navigateur et vous pourrez interagir avec les visualisations.

📚 Conclusion

Ce projet permet d'explorer en profondeur les salaires dans le domaine de la Data Science à travers une approche interactive et visuelle. Grâce à Jupyter Notebook, nous avons pu analyser les données en détail, et avec Streamlit, nous offrons une plateforme intuitive pour explorer ces informations de manière dynamique.

🚀 Bonnes explorations et bonnes analyses !
