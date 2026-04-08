from dotenv import load_dotenv
import streamlit as st
import os
import sqlite3
from langchain_groq import ChatGroq


# load environment variables
load_dotenv()


# load LLM (fast model)
llm = ChatGroq(
    model="llama-3.3-70b-versatile",
    temperature=0,
    api_key=os.getenv("groq_api"),
    max_tokens=120
)


# function to convert English → SQL
def get_groq_response(question):

    prompt = f"""
    Convert English question to SQL query.

    Table name: Student

    Columns:
    NAME, CLASS, SECTION, MARKS

    Question: {question}

    Return ONLY SQL query.
    Do not explain.
    Do not use markdown.
    """

    response = llm.invoke(prompt)

    sql_query = response.content.strip()

    sql_query = sql_query.replace("```", "")

    return sql_query



# function to execute SQL query
def read_sql_query(sql):

    conn = sqlite3.connect("company.db")

    cursor = conn.cursor()

    cursor.execute(sql)

    rows = cursor.fetchall()

    conn.close()

    return rows



# Streamlit UI
st.set_page_config(page_title="SQL AI App")

st.title("Ask Questions from SQL Database")


# input box
question = st.text_input("Enter your question")


# button
if st.button("Submit"):

    sql_query = get_groq_response(question)

    st.subheader("Generated SQL Query:")

    st.code(sql_query)


    result = read_sql_query(sql_query)


    st.subheader("Query Result:")

    for row in result:

        st.write(row)