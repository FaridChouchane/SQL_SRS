# pylint: disable=missing-module-docstring
import io
import ast
import duckdb
import pandas as pd
import streamlit as st


# ----------------------------------------------------------------------------------------
# ----------------------------------------------------------------------------------------
con = duckdb.connect(database = "data/exercices_sql_tables.duckdb", read_only = False)
# ----------------------------------------------------------------------------------------
# ----------------------------------------------------------------------------------------
# ----------------------------------------------------------------------------------------
# ----------------------------------------------------------------------------------------
# -----------------------------------------------------------------------------------------------------------------------
# -----------------------------------------------------------------------------------------------------------------------
with (st.sidebar):
    theme = st.selectbox(
        "What would you like to review ?\n",
        ("cross-joins", "GroupBy", "windows_functions"),
        index=None,
        placeholder="Select a theme...",
    )
    st.write("You selected", theme)

    exercise = con.execute(f"SELECT * FROM memory_state_df WHERE theme = '{theme}'").df()
    st.write(exercise)

    exercice_name = exercise.loc[0, "exercice_name"]
    with open(f"answers/{exercice_name}.sql", "r") as f:
        answer = f.read()

    solution_df = con.execute(answer).df()

st.header(" Enter your code :\n ")
query = st.text_area(label="votre code SQL ici :", key="user_input")
#
# # ----------------------------------------------------------------------------------------
# # ----------------------------------------------------------------------------------------
if query:
    result = con.execute(query).df()
    st.dataframe(result)
    # ----------------------------------------------------------------------------------------
    # ----------------------------------------------------------------------------------------
    try:
        result = result[solution_df.columns]
        st.dataframe(result.compare(solution_df))
    except KeyError as e:
        st.write("/!\  ---- SOME COLUMNS ARE MISSING ---- /!\ ")
    # ----------------------------------------------------------------------------------------
    # ----------------------------------------------------------------------------------------
    n_lines_difference = result.shape[0] - solution_df.shape[0]
    if n_lines_difference != 0:
        st.write(f"DIFFERENCE DE  {n_lines_difference} LIGNES AVEC LA SOLUTION")
# # ----------------------------------------------------------------------------------------
# # ----------------------------------------------------------------------------------------
#
# # ----------------------------------------------------------------------------------------
# # ----------------------------------------------------------------------------------------
tab2, tab3 = st.tabs(["Tables", "Solution"])
#
with tab2:
    if exercise.empty:
        st.write("No exercises found for the selected theme.")
    elif "tables" not in exercise.columns:
        st.write("The 'tables' column is missing from the exercise DataFrame.")
    else:
        try:
            exercise_tables = ast.literal_eval(exercise.loc[0, "tables"])
            for table in exercise_tables:
                st.write(f"table : {table}")
                df_table = con.execute(f"SELECT * FROM {table}").df()
                st.dataframe(df_table)
        except Exception as e:
            st.write("Error processing tables:", str(e))
#     st.write("table : food_items")
#     st.dataframe(food_items)
#     st.write("expected :")
#     st.dataframe(solution_df)
#
with tab3:
    st.write(answer)
# # ----------------------------------------------------------------------------------------
# # ----------------------------------------------------------------------------------------
