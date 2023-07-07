import streamlit as st
import pandas as pd

st.title('DASHBOARD IDH')
st.write('Projeto Final da Disciplina Análise e Visualização de Dados')
st.write('Equipe 12: Arthur Perruci, Daniel, Enio')
tab1, tab2, tab3 = st.tabs(["IDH", "Dog", "Tabela de dados"])

with tab1:
   st.header("O que representa o Índice de Desenvolvimento Humano - IDH")
   st.write("O Índice de Desenvolvimento Humano (IDH) compara indicadores de países nos itens riqueza, alfabetização, educação, esperança de vida, natalidade e outros, com o intuito de avaliar o bem-estar de uma população")
   st.write("fonte:" + https://www.ipea.gov.br/desafios/index.php?option=com_content&id=2144:catid=28#:~:text=O%20que%20%C3%A9%3F,IDH&text=O%20%C3%8Dndice%20de%20Desenvolvimento%20Humano,uma%20popula%C3%A7%C3%A3o%2C%20especialmente%20das%20crian%C3%A7as.)
   st.image("https://static.streamlit.io/examples/cat.jpg", width=200)

with tab2:
   st.header("A dog")
   st.image("https://static.streamlit.io/examples/dog.jpg", width=200)

with tab3:
   st.header("An owl")
   st.image("https://static.streamlit.io/examples/owl.jpg", width=200)
   df = pd.read_csv("atlas.csv")
   df
