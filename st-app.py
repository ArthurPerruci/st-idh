import streamlit as st
import pandas as pd
import plotly.express as px
import PIL
from PIL import Image

df = pd.read_csv("atlas.csv")
idh_composicao = Image.open('idh_composicao.png')
fig_gini_esc = px.box(df, x='gini', y='i_escolaridade')


st.title('DASHBOARD IDH')
texto1 = 'Cesar School - Curso de Especialização em Engenharia e Análise de Dados\nProjeto Final da Disciplina Análise e Visualização de Dados\nEquipe 12: Arthur Perruci, Daniel Duarte, Enio Kilder'
st.text(texto1)
tab1, tab2, tab3 = st.tabs(["O que é IDH?", "GINI e Escolaridade", "Tabela de dados"])

with tab1:
   st.markdown("**O que representa o Índice de Desenvolvimento Humano - IDH**")
   st.text("O Índice de Desenvolvimento Humano (IDH) compara indicadores de países\nnos itens riqueza, alfabetização, educação, esperança de vida, natalidade e outros,\ncom o intuito de avaliar o bem-estar de uma população")
   st.write("fonte: IPEA / Desafios do Desenvolvimento ( https://encurtador.com.br/eQS35 )")
   st.image(idh_composicao)

with tab2:
   st.markdown("**GINI e escolaridade**")
   st.plotly_chart(fig_gini_esc)

with tab3:
   st.markdown("**Tabela base**")   
   df
