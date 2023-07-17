import streamlit as st
import pandas as pd
import plotly.express as px
import matplotlib.pyplot as plt
import PIL
from PIL import Image
import plotly.graph_objects as go
import altair as alt

#Leitura do data frame
df = pd.read_csv("data/atlas.csv")
df_leg_long = pd.read_csv("data/legendas_long.csv")

#carregamento de imagens
fig_long_esp_vid = Image.open('assets/fig_long_esp_vid.png')
fig_long_sobr_40 = Image.open('assets/fig_long_sobr_40.png')
fig_long_sobr_60 = Image.open('assets/fig_long_sobr_60.png')

st.set_page_config(page_title="IDH - Longevidade", page_icon=":👴:")
st.title("IDH - Longevidade")

col1, col2, col3, col4 = st.columns(4)

with col1:
     st.image(fig_long_esp_vid)
with col2:
     st.image(fig_long_sobr_40)
with col3:
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
st.markdown("Esperança de Vida ao Nascer e IDH")
fig_idh_espvida = alt.Chart(df).mark_circle().encode(
     x='espvida',
     y='idhm',
     #color='regiao',
     ).interactive()
st.altair_chart(fig_idh_espvida, theme="streamlit", use_container_width=True)
