import streamlit as st
import pandas as pd
import plotly.express as px
import PIL
from PIL import Image

df = pd.read_csv("atlas.csv")
idh_composicao = Image.open('idh_composicao.png')
idh_faixas = Image.open('idh_faixas.png')
fig_gini_esc = px.box(df, x='gini', y='i_escolaridade')


st.title('DASHBOARD IDH')
texto1 = 'Cesar School - Curso de Especialização em Engenharia e Análise de Dados\nProjeto Final da Disciplina Análise e Visualização de Dados\nEquipe 12: Arthur Perruci, Daniel Duarte, Enio Kilder'
st.text(texto1)
tab1, tab2, tab3, tab4 = st.tabs(["Entender o IDH", "ou", "GINI e Escolaridade", "Tabela de dados"])

with tab1:
   col1, col2 = st.columns(2)
      with col1:
         col1.markdown("**O que representa o Índice de Desenvolvimento Humano - IDH**")
         col1.text("O Índice de Desenvolvimento Humano (IDH) compara indicadores de países\nnos itens riqueza, alfabetização, educação, esperança de vida, natalidade e outros,\ncom o intuito de avaliar o bem-estar de uma população")
         col1.write("fonte: IPEA / Desafios do Desenvolvimento ( https://encurtador.com.br/eQS35 )")
         col1.image(idh_composicao)
      with col2:
         col2.write("O valor do IDH varia de 0 (zero) a 1, e conforme o valor pode ser considerado de muito baixo a muito alto conforme as faxias descritas na figura.")
         col2.image(idh_faixas)
         col2.write("Reproduzido de IPEA / O Índice de Desenvolvimento Humano Municipal Brasileiro (disponível para download em: https://repositorio.ipea.gov.br/handle/11058/2375) ")

with tab2:
   st.write('ou')

with tab3:
   st.markdown("**GINI e escolaridade**")
   st.plotly_chart(fig_gini_esc)

with tab4:
   st.markdown("**Tabela base**")   
   df
