import streamlit as st
import pandas as pd
import plotly.express as px
import matplotlib.pyplot as plt
import PIL
from PIL import Image
import plotly.graph_objects as go
import altair as alt
from st_pages import show_pages_from_config

show_pages_from_config()

#Leitura do data frame
df = pd.read_csv("data/atlas.csv")
df_leg_long = pd.read_csv("data/legendas_long.csv")

#incorporação do dado Região ao dataframe
uf = [[43, 42, 41], [35, 33, 32, 31], [29, 28, 27, 26, 25, 24, 23, 22, 21], [17, 15, 16, 14, 13, 12, 11], [51, 52, 53, 50]]
sul, sudeste, nordeste, norte, centro_oeste = uf[0], uf[1], uf[2], uf[3], uf[4]

def check_regiao(uf):
  if sul.count(uf) > 0:
    return 'Sul'
  elif sudeste.count(uf) > 0:
    return 'Sudeste'
  elif centro_oeste.count(uf) > 0:
    return 'Centro Oeste'
  elif nordeste.count(uf) > 0:
    return 'Nordeste'
  else:
    return 'Norte'

df['regiao'] = df['uf'].apply(check_regiao)

#carregamento de imagens
fig_long_esp_vid = Image.open('assets/fig_long_esp_vid.png')
fig_long_sobr_40 = Image.open('assets/fig_long_sobr_40.png')
fig_long_sobr_60 = Image.open('assets/fig_long_sobr_60.png')

#Início da página
st.title("IDH - Longevidade")

#Colunas para as imagens
col1, col2, col3, col4 = st.columns(4)
with col1:
     st.image(fig_long_esp_vid)
with col2:
     st.image(fig_long_sobr_40)
with col3:
     st.image(fig_long_sobr_60)

#Gráfico mapa de calor indicadores longevidade e idh
st.markdown("Vários indicadores relacionados a longevidade, educação e renda são utilizados no cálculo do idh. No gráfico abaixo verifica-se a relação dos indicadores relacionados à longevidade com o idh-l e idh final. No gráfico destacam-se como mais forte a relação do idhm com os indicadores Esperança de vida ao nascer, Probabilidade de sobrevivência até 40 anos e Probabilidade de sobrevivência até 60 anos.")
ano_grafico = st.sidebar.radio('Ano', df['ano'].unique())
df = df.loc[df['ano'] == ano_grafico]
df_comp_long = df[df_leg_long['INDICADOR']].copy()
comp_long = df_comp_long.corr(method='pearson')
fig_idh_long = px.imshow(comp_long)
fig_idh_long.update_layout(title="Indicadores IDH Longevidade - " + str(ano_grafico))
fig_idh_long_leg = go.Figure()
fig_idh_long_leg.add_trace(
     go.Table(
       header = dict(values=['Indicador','Descrição']),
       cells = dict(values=[
            df_leg_long['INDICADOR'],
            df_leg_long['DESCRIÇÃO']
            ],
       align=['center','left']),
       columnwidth=[1,4]
       )
     )
st.plotly_chart(fig_idh_long)
st.plotly_chart(fig_idh_long_leg)

#Gráfico scatter esperança de vida ao nascer e idh
st.markdown("Esperança de Vida ao Nascer e IDH")
fig_idh_espvida = go.Figure()
fig_idh_espvida.add_trace(go.Scattergl(x=df['espvida'], y=df['idhm'], mode="markers"))
fig_idh_espvida.update_layout(title="Relação entre Esperança de vida ao Nascer e IDH - " + str(ano_grafico))
fig_idh_espvida.update_xaxes(title_text="Esperança de vida ao nascer")
fig_idh_espvida.update_yaxes(title_text="Idhm")
st.plotly_chart(fig_idh_espvida)

#Gráfico scatter probabilidade de sobrevivência até 40 anos e idh
st.markdown("Probabilidade de sobrevivência até os 40 anos e IDH")
fig_idh_sobre40 = go.Figure()
fig_idh_sobre40.add_trace(go.Scattergl(x=df['sobre40'], y=df['idhm'], mode="markers"))
fig_idh_sobre40.update_layout(title="Relação entre a probabilidade de sobrevivência até os 40 anos e IDH - " + str(ano_grafico))
fig_idh_sobre40.update_xaxes(title_text="Probabilidade de sobrevivência até os 40 anos")
fig_idh_sobre40.update_yaxes(title_text="Idhm")
st.plotly_chart(fig_idh_sobre40)

#Gráfico scatter probabilidade de sobrevivência até 60 anos e idh
st.markdown("Probabilidade de sobrevivência até os 60 anos e IDH")
fig_idh_sobre60 = go.Figure()
fig_idh_sobre60.add_trace(go.Scattergl(x=df['sobre60'], y=df['idhm'], mode="markers"))
fig_idh_sobre60.update_layout(title="Relação entre a probabilidade de sobrevivência até os 60 anos e IDH - " + str(ano_grafico))
fig_idh_sobre60.update_xaxes(title_text="Probabilidade de sobrevivência até os 60 anos")
fig_idh_sobre60.update_yaxes(title_text="Idhm")
st.plotly_chart(fig_idh_sobre60)

