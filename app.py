import streamlit as st
import pandas as pd
import mysql.connector

st.header("Aula de laboratório de banco de dados")
st.title("Título")
st.markdown("Primeiro *texto* **texto2** :rainbow[colors]")

st.sidebar.header("Cabeçalho sidebar")
st.sidebar.radio("radiobutton", [1,2])

conn = mysql.connector.connect(host="localhost"
                               , user="bruno", password="1234"
                               , port=3306, db="labbd"
                               , auth_plugin='mysql_native_password')
cursor = conn.cursor()

cursor.execute("select * from escola;")
res = cursor.fetchall()
df = pd.DataFrame(res, columns=cursor.column_names)

# st.write(df)


######################### CACHING ##########################
@st.cache_data
def load_escolas_cache():
    cursor.execute("select * from vw_escola;")
    res = cursor.fetchall()
    df = pd.DataFrame(res, columns=cursor.column_names)
    return res


def load_escolas():
    cursor.execute("select * from vw_escola;")
    res = cursor.fetchall()
    df = pd.DataFrame(res, columns=cursor.column_names)
    return df

df = load_escolas_cache()
####################################################
###### SESSION 
if 'escolas' not in st.session_state:
    st.session_state['escolas'] = []

st.session_state['escolas'] = load_escolas_cache()
st.write(st.session_state['escolas'])

####################################################

##### Escrita na página
#st.write(st.session_state['escolas'])

###### SECRETS
st.write("Segredo: " + st.secrets['db_username'])