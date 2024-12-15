import pandas as pd
import streamlit as st
import duckdb

data = {"a" : [1, 2, 3], "b" : [4, 5, 6]}
df = pd.DataFrame(data)
tab1, tab2, tab3 = st.tabs(["Cat", "Dog", "Owl"])

with tab1:
    # Entrée utilisateur avec un placeholder pour guider
    sql_query = st.text_area(label="Entrez votre requête SQL :", placeholder="Exemple : SELECT * FROM df")

    # Vérification de la requête utilisateur
    if sql_query.strip():  # Assurez-vous que la requête n'est pas vide
        try:
            # Connexion à DuckDB
            con = duckdb.connect()  # Connexion temporaire
            con.register("df", df)  # Enregistrement du DataFrame comme une table SQL

            # Exécution de la requête
            result = con.execute(sql_query).df()  # Convertit le résultat en DataFrame

            # Affichage des résultats
            st.write(f"Vous avez entré la requête suivante :")
            st.code(sql_query, language="sql")  # Affiche la requête avec mise en forme
            st.dataframe(result)  # Affiche le résultat sous forme de tableau

        except Exception as e:
            # Affiche un message d'erreur détaillé
            st.error(f"Erreur lors de l'exécution de la requête : {e}")
    else:
        # Message si la zone de texte est vide
        st.warning("Veuillez entrer une requête SQL valide dans la zone ci-dessus.")
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