import streamlit as st
import pandas as pd
import plotly.express as px
import matplotlib.pyplot as plt
import PIL
from PIL import Image
import plotly.graph_objects as go

#Leitura do data frame
df = pd.read_csv("data/atlas.csv")
df_leg_long = pd.read_csv("data/legendas_long.csv")

#carregamento de imagens
fig_long_esp_vid = Image.open('assets/fig_long_esp_vid.png')
fig_long_sobr_40 = Image.open('assets/fig_long_sobr_40.png')
fig_long_sobr_60 = Image.open('assets/fig_long_sobr_60.png')

st.title("IDH - Longevidade")
st.image(fig_long_esp_vid)
st.image(fig_long_sobr_40)
st.image(fig_long_sobr_60)
st.markdown("Vários indicadores relacionados a longevidade, educação e renda são utilizados no cálculo do idh. No gráfico abaixo verifica-se a relação dos indicadores relacionados à longevidade com o idh-l e idh final. No gráfico destacam-se como mais forte a relação do idhm com os indicadores Esperança de vida ao nascer, Probabilidade de sobrevivência até 40 anos e Probabilidade de sobrevivência até 60 anos.")
ano_grafico = st.sidebar.selectbox('Ano', df['ano'].unique())
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
