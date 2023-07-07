import streamlit as st
import pandas as pd

st.title('DASHBOARD IDH')
st.write('Projeto Final da Disciplina Análise e Visualização de Dados')
st.write('Equipe 12: Arthur Perruci, Daniel, Enio')
tab1, tab2, tab3 = st.tabs(["IDH", "Dog", "Tabela de dados"])

with tab1:
   st.header("O que representa o Índice de Desenvolvimento Humano - IDH")
   st.image("https://static.streamlit.io/examples/cat.jpg", width=200)

with tab2:
   st.header("A dog")
   st.image("https://static.streamlit.io/examples/dog.jpg", width=200)

with tab3:
   st.header("An owl")
   st.image("https://static.streamlit.io/examples/owl.jpg", width=200)
   df = pd.read_csv("atlas.csv")
   df
