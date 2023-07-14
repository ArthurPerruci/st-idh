import streamlit as st
import pandas as pd
import plotly.express as px
import matplotlib.pyplot as plt
import PIL
from PIL import Image
import plotly.graph_objects as go

#Leitura do data frame
df = pd.read_csv("data/atlas.csv")
df_leg_edu = pd.read_csv("data/legendas_edu.csv")

#carregamento de imagens
fig_edu_anos_est = Image.open('assets/fig_edu_anos_est.png')
fig_edu_tx_freq = Image.open('assets/fig_edu_tx_freq.png')
fig_edu_ens_comp = Image.open('assets/fig_edu_ens_comp.png')
fig_edu_nao_atraso = Image.open('assets/fig_edu_nao_atraso.png')

st.set_page_config(page_title="IDH Educação", page_icon=":book:")
st.title('IDH - Educação')

col1, col2, col3, col4 = st.columns(4)

with col1:
     st.image(fig_edu_anos_est)
with col2:
     st.image(fig_edu_tx_freq)
with col3:     
     st.image(fig_edu_ens_comp)
with col4:     
     st.image(fig_edu_nao_atraso)

st.markdown("Vários indicadores relacionados a longevidade, educação e renda são utilizados no cálculo do idh. No gráfico abaixo verifica-se a relação dos indicadores relacionados à educação com o idh-e e idh final. No gráfico destacam-se como mais forte a relação do idhm com os indicadores expectativa de anos de estudos, percentual de estudantes sem atraso no ensino fundamental e básico, taxas de frequência escolar nos ensino médio e superior e percentual de pessoas com ensino fundamental completo.")
ano_grafico = st.sidebar.selectbox('Ano', df['ano'].unique())
df = df.loc[df['ano'] == ano_grafico]
df_comp_edu = df[df_leg_edu['INDICADOR']].copy()
comp_edu = df_comp_edu.corr(method='pearson')
fig_idh_edu = px.imshow(comp_edu)
fig_idh_edu.update_layout(title="Indicadores IDH Educação - " + str(ano_grafico))
fig_idh_edu_leg = go.Figure()
fig_idh_edu_leg.add_trace(
     go.Table(
       header = dict(values=['Indicador','Descrição']),
       cells = dict(values=[
            df_leg_edu['INDICADOR'],
            df_leg_edu['DESCRIÇÃO']
            ],
       align=['center','left']),
       columnwidth=[1,4]
       )
     )
st.plotly_chart(fig_idh_edu)
st.plotly_chart(fig_idh_edu_leg)
