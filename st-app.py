import streamlit as st
import pandas as pd

st.title('DASHBOARD IDH')
texto1 = 'Cesar School - Curso de Especialização em Engenharia e Análise de Dados\nProjeto Final da Disciplina Análise e Visualização de Dados\nEquipe 12: Arthur Perruci, Daniel, Enio'
st.text(texto1)
tab1, tab2, tab3 = st.tabs(["O que é IDH?", "Dog", "Tabela de dados"])

with tab1:
   st.subheader("O que representa o Índice de Desenvolvimento Humano - IDH")
   st.text("O Índice de Desenvolvimento Humano (IDH) compara indicadores de países\nnos itens riqueza, alfabetização, educação, esperança de vida, natalidade e outros,\ncom o intuito de avaliar o bem-estar de uma população")
   st.write("fonte: https://encurtador.com.br/eQS35")
   st.image("https://static.streamlit.io/examples/cat.jpg", width=50)

with tab2:
   st.subheader("A dog")
   st.image("https://static.streamlit.io/examples/dog.jpg", width=200)

with tab3:
   st.subheader("An owl")
   st.image("https://static.streamlit.io/examples/owl.jpg", width=200)
   df = pd.read_csv("atlas.csv")
   df
