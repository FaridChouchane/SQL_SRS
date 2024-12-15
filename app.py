import pandas as pd
import streamlit as st
import duckdb

data = {"a" : [1, 2, 3], "b" : [4, 5, 6]}
df = pd.DataFrame(data)
tab1, tab2, tab3 = st.tabs(["Cat", "Dog", "Owl"])

with tab1:
    # Entrée utilisateur
    sql_query = st.text_area(label="Entrez votre requête SQL :", placeholder="Exemple : SELECT * FROM df")

    # Vérification de l'entrée utilisateur
    if sql_query.strip():  # S'assurer que l'entrée n'est pas vide
        try:
            # Connexion DuckDB et enregistrement de la table
            con = duckdb.connect()
            con.register("df", df)

            # Exécution de la requête SQL
            result = con.execute(sql_query).df()

            # Affichage des résultats
            st.write("Vous avez entré la requête suivante :")
            st.code(sql_query, language="sql")
            st.dataframe(result)

        except Exception as e:
            # Éviter d'afficher tout l'objet exception brute
            st.error("Une erreur est survenue lors de l'exécution de la requête.")

            # Facultatif : Affiche une version nettoyée de l'erreur dans la console pour déboguer
            with st.expander("Afficher les détails de l'erreur pour débogage"):
                st.exception(e)  # Affiche l'exception dans un cadre dédié
    else:
        st.warning("Veuillez entrer une requête SQL valide.")
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