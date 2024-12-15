import pandas as pd
import streamlit as st
import duckdb

data = {"a" : [1, 2, 3], "b" : [4, 5, 6]}
df = pd.DataFrame(data)
tab1, tab2, tab3 = st.tabs(["Cat", "Dog", "Owl"])

with tab1:
    # Entrée utilisateur
    sql_query = st.text_area(label="Entrez votre input :", value="")  # Zone de texte initialement vide

    if sql_query.strip():  # Vérifie si une requête non vide est saisie
        try:
            # Connexion DuckDB et enregistrement de la table
            con = duckdb.connect()
            con.register("df", df)  # Enregistre le DataFrame comme une table

            # Exécution de la requête
            result = con.execute(sql_query).df()
            st.write(f"Vous avez entré la requête suivante : {sql_query}")
            st.dataframe(result)
        except Exception as e:
            # Affiche un message d'erreur clair
            st.error(f"Erreur lors de l'exécution de la requête : {e}")
    else:
        # Message d'avertissement si la zone est vide
        st.warning("Veuillez entrer une requête SQL valide.")

    # Affichage d'une image
    st.header("A cat")
    st.image("https://storage.googleapis.com/pod_public/1300/151089.jpg", width=200)
    '''
    sql_query = st.text_area(label="Entrez votre input : ")
    result = duckdb.query(sql_query).df()
    st.write(f"vous avez entré la query suivante : {sql_query}")
    st.dataframe(result)
    st.header("A cat")
    st.image("https://storage.googleapis.com/pod_public/1300/151089.jpg", width=200)
    '''
with tab2:
    st.header("A dog")
    st.image("https://cdn.britannica.com/79/232779-050-6B0411D7/German-Shepherd-dog-Alsatian.jpg", width=200)


with tab3:
    st.header("A owl")
    st.image("https://ccfriendsofwildlife.org/wp-content/uploads/2023/05/Chris-Robben.jpg", width=200)