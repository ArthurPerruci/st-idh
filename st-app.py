import streamlit as st
import pandas as pd

st.title('DASHBOARD IDH')
st.write('Cesar School - Curso de Especialização em Engenharia e Análise de Dados')
st.write('Projeto Final da Disciplina Análise e Visualização de Dados')
st.write('Equipe 12: Arthur Perruci, Daniel, Enio')
tab1, tab2, tab3 = st.tabs(["IDH", "Dog", "Tabela de dados"])

with tab1:
   st.header("O que representa o Índice de Desenvolvimento Humano - IDH")
   st.write("O Índice de Desenvolvimento Humano (IDH) compara indicadores de países nos itens riqueza, alfabetização, educação, esperança de vida, natalidade e outros, com o intuito de avaliar o bem-estar de uma população")
   st.write("fonte: https://encurtador.com.br/eQS35")
   st.image("https://static.streamlit.io/examples/cat.jpg", width=50)

with tab2:
   st.header("A dog")
   st.image("https://static.streamlit.io/examples/dog.jpg", width=200)

with tab3:
   st.header("An owl")
   st.image("https://static.streamlit.io/examples/owl.jpg", width=200)
   df = pd.read_csv("atlas.csv")
   df
