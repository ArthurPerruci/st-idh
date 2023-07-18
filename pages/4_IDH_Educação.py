import streamlit as st
import pandas as pd
import plotly.express as px
import matplotlib.pyplot as plt
import PIL
from PIL import Image
import plotly.graph_objects as go
import altair as alt
from plotly.subplots import make_subplots

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

#Início da página
st.title('IDH - Educação')

#Colunas para as imagens
col1, col2, col3, col4 = st.columns(4)
with col1:
     st.image(fig_edu_anos_est)
with col2:
     st.image(fig_edu_tx_freq)
with col3:     
     st.image(fig_edu_ens_comp)
with col4:     
     st.image(fig_edu_nao_atraso)

#Gráfico Mapa de calor indicadores educação e idhm
st.markdown("No gráfico abaixo verifica-se a relação dos indicadores relacionados à educação com o idh-e e idh final. Destacam-se como mais fortes as relações do idhm com os indicadores expectativa de anos de estudos, percentual de estudantes sem atraso no ensino fundamental e básico, taxas de frequência escolar nos ensino médio e superior e percentual de pessoas com ensino fundamental completo.")
ano_grafico = st.sidebar.radio('Ano', df['ano'].unique())
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

#Gráfico pontos expectativa de anos de estudo e idh
st.markdown("Expectativa de anos de estudo e IDH")
fig_idh_e_anosestudo = go.Figure(data=go.Scattergl(x=df['e_anosestudo'], y=df['idhm'], mode="markers"))
fig_idh_e_anosestudo.update_layout(title="Relação entre a expectativa de anos de estudo  e IDH - " + str(ano_grafico))
fig_idh_e_anosestudo.update_xaxes(title_text="Expectativa de anos de estudo")
fig_idh_e_anosestudo.update_yaxes(title_text="Idhm")
st.plotly_chart(fig_idh_e_anosestudo)

#Gráfico pontos frequência escolar e idh
st.markdown("Taxa de frequência escolar e IDH")
fig_idh_freq = go.Figure()
fig_idh_freq.update_layout(title="Relação entre a frequência escolar líquida e o IDH - " + str(ano_grafico))
fig_idh_freq.add_trace(go.Scattergl(x=df['t_flfund'], y=df['idhm'], mode="markers", name="Ensino Fundamental"))
fig_idh_freq.add_trace(go.Scattergl(x=df['t_flmed'], y=df['idhm'], mode="markers", name="Ensino Médio"))
fig_idh_freq.add_trace(go.Scattergl(x=df['t_flsuper'], y=df['idhm'], mode="markers", name="Ensino Superior"))
fig_idh_freq.update_layout(legend=dict(x=0, y=1))
fig_idh_freq.update_xaxes(title_text="Frequência líquida")
fig_idh_freq.update_yaxes(title_text="Idhm")
st.plotly_chart(fig_idh_freq)

#Gráfico pontos ensino completo e idh
st.markdown("Ensino completo e IDH")
fig_idh_comp = go.Figure()
fig_idh_comp.update_layout(title="Relação entre o percentual da população com ensino completo e o IDH - " + str(ano_grafico))
fig_idh_comp.add_trace(go.Scattergl(x=df['t_fund18m'], y=df['idhm'], mode="markers", name="população de 18 anos ou mais com ensino fundamental completo"))
fig_idh_comp.add_trace(go.Scattergl(x=df['t_med18m'], y=df['idhm'], mode="markers", name="população de 18 anos ou mais  com ensino médio completo"))
fig_idh_comp.add_trace(go.Scattergl(x=df['t_med25m'], y=df['idhm'], mode="markers", name="população de 25 anos ou mais com ensino médio completo"))
fig_idh_comp.add_trace(go.Scattergl(x=df['t_super25m'], y=df['idhm'], mode="markers", name="população de 25 anos ou mais com ensino supeior completo"))
fig_idh_comp.update_xaxes(title_text="% da população com ensino completo")
fig_idh_comp.update_yaxes(title_text="Idhm")
st.plotly_chart(fig_idh_comp)

#Gráfico pontos atraso escolar e idh
st.markdown("Atraso escolar e IDH")
fig_idh_nao_atraso = go.Figure()
fig_idh_nao_atraso.update_layout(title="Relação entre o percentual da população sem atraso escolar e o IDH - " + str(ano_grafico))
fig_idh_nao_atraso.add_trace(go.Scattergl(x=df['t_atraso_0_fund'], y=df['idhm'], mode="markers", name="população de 6 a 14 anos no ensino fundamental sem atraso"))
fig_idh_nao_atraso.add_trace(go.Scattergl(x=df['t_atraso_0_med'], y=df['idhm'], mode="markers", name="população de 15 a 17 anos no ensino médio sem atraso"))
fig_idh_nao_atraso.update_xaxes(title_text="% da população sem atraso")
fig_idh_nao_atraso.update_yaxes(title_text="Idhm")
st.plotly_chart(fig_idh_nao_atraso)
