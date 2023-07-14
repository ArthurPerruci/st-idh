import streamlit as st
import pandas as pd
import plotly.express as px
import matplotlib.pyplot as plt
import PIL
from PIL import Image
import plotly.graph_objects as go
import idh_regioes as idh_reg

#Leitura do data frame
df = pd.read_csv("data/atlas.csv")

#incorporação do dado Região ao dataframe
uf = [[43, 42, 41], [35, 33, 32, 31], [29, 28, 27, 26, 25, 24, 23, 22, 21], [17, 15, 16, 14, 13, 12, 11], [51, 52, 53, 50]]
sul, sudeste, nordeste, norte, centro_oeste = uf[0], uf[1], uf[2], uf[3], uf[4]

#def check_regiao(uf):
#  if sul.count(uf) > 0:
#    return 'Sul'
#  elif sudeste.count(uf) > 0:
#    return 'Sudeste'
#  elif centro_oeste.count(uf) > 0:
#    return 'Centro Oeste'
#  elif nordeste.count(uf) > 0:
#    return 'Nordeste'
#  else:
#    return 'Norte'

df['regiao'] = df['uf'].apply(idh_reg.check_regiao)

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
