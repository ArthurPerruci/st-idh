import streamlit as st
import pandas as pd
import plotly.express as px
import matplotlib.pyplot as plt
import PIL
from PIL import Image
import plotly.graph_objects as go

#Leitura do data frame
df = pd.read_csv("data/atlas.csv")

st.title('IDH e GINI')
st.markdown("O Índice de Gini mede o grau de concentração de renda. Ele aponta a diferença entre os rendimentos dos mais pobres e dos mais ricos. Varia de zero a um, onde zero representa a situação de igualdade (todos têm a mesma renda) e um é extremo oposto (uma só pessoa detém toda a riqueza).")
st.write("fonte: IPEA / Desafios do Desenvolvimento ( https://www.ipea.gov.br/desafios/index.php?option=com_content&id=2048:catid=28 )")
st.markdown("O gráfico evidencia que não há uma relação forte entre o valor do idhm e do gini, independente do ano e da região.")
ano_grafico = st.sidebar.selectbox('Ano', df['ano'].unique())
df = df.loc[df['ano'] == ano_grafico]
fig_idh_gini = px.scatter(df, x="gini", y="idhm", color="regiao")
fig_idh_gini.update_layout(title="Relação IDH x GINI - " + str(ano_grafico))
st.plotly_chart(fig_idh_gini)
st.text("Os dados foram capturados em três anos base: 1991, 2000 e 2010.\nEscolha o ano a ser visualizado na barra à esquerda.\nNo gráfico cada esfera representa um município.\nClique no nome da Região para ocultá-la ou visualizá-la.")
