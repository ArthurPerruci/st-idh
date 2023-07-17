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
st.markdown("Expectativa de anos de estudo e IDH")
fig_idh_e_anosestudos = alt.Chart(df, title="Relação entre a expectativa de anos de estudo  e IDH - " + str(ano_grafico)).mark_circle().encode(
     x=alt.X('e_anosestudos'), #, scale=alt.Scale(domain=[40,100])
     y=alt.Y('idhm', scale=alt.Scale(domain=[0,1])),
     color='regiao',
     ).interactive()
st.altair_chart(fig_idh_e_anosestudos, theme="streamlit", use_container_width=True)
st.markdown("Taxa de frequência escolar e IDH")
fig_idh_t_fbmed = alt.Chart(df, title="Relação entre afrequência escolar bruta no ensino médio e IDH - " + str(ano_grafico)).mark_circle().encode(
     x=alt.X('t_fbmed'), #, scale=alt.Scale(domain=[40,100])
     y=alt.Y('idhm', scale=alt.Scale(domain=[0,1])),
     color='regiao',
     ).interactive()
st.altair_chart(fig_idh_t_fbmed, theme="streamlit", use_container_width=True)
