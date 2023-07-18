import streamlit as st
import pandas as pd
import plotly.express as px
import matplotlib.pyplot as plt
import PIL
from PIL import Image
import plotly.graph_objects as go

#Leitura do data frame
df = pd.read_csv("data/atlas.csv")
df_leg_ren = pd.read_csv("data/legendas_ren.csv")

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
fig_ren_renpcap = Image.open('assets/fig_ren_renpcap.png')
fig_ren_ag_ban = Image.open('assets/fig_ren_ag_ban.png')

#Início da página
st.title('IDH - Renda')

#Colunas para as imagens
col1, col2, col3, col4 = st.columns(4)
with col1:
     st.image(fig_ren_renpcap)
with col2:
     st.image(fig_ren_ag_ban)

#Gráfico mapa de calor indicadores renda e idh
st.markdown("No gráfico abaixo verifica-se a relação dos indicadores relacionados à renda com o idh-r e idh final. Destacam-se como mais fortes as relações do idhm com os indicadores de renda per capta (em vários recortes) e percentual de população residente em domicílios com água encanada e banheiro.")
ano_grafico = st.sidebar.radio('Ano', df['ano'].unique())
df = df.loc[df['ano'] == ano_grafico]
df_comp_ren = df[df_leg_ren['INDICADOR']].copy()
comp_ren = df_comp_ren.corr(method='pearson')
fig_idh_ren = px.imshow(comp_ren)
fig_idh_ren.update_layout(title="Indicadores IDH Renda - " + str(ano_grafico))
fig_idh_ren_leg = go.Figure()
fig_idh_ren_leg.add_trace(
     go.Table(
       header = dict(values=['Indicador','Descrição']),
       cells = dict(values=[
            df_leg_ren['INDICADOR'],
            df_leg_ren['DESCRIÇÃO']
            ],
       align=['center','left']),
       columnwidth=[1,4]
       )
     )
st.plotly_chart(fig_idh_ren)
st.plotly_chart(fig_idh_ren_leg)

#Gráfico Renda per capita e idh
st.markdown("Renda per capita e IDH")
fig_idh_rdpc = go.Figure()
fig_idh_rdpc.update_layout(title="Relação renda per capita e IDH - " + str(ano_grafico))
fig_idh_rdpc.add_trace(go.Scattergl(x=df['rdpc'], y=df['idhm'], mode="markers"))
fig_idh_rdpc.update_xaxes(title_text="Renda per capita")
fig_idh_rdpc.update_yaxes(title_text="Idhm")
st.plotly_chart(fig_idh_rdpc)

#Gráfico pop residente em domicílio com água encanada, banheiro e idh
st.markdown("Água encanada, banheiro e IDH")
fig_idh_aguaban = go.Figure()
fig_idh_aguaban.update_layout(title="Relação entre população residente em domicílio com água encanada e banheiro e IDH - " + str(ano_grafico))
fig_idh_aguaban.add_trace(go.Scattergl(x=df['t_agua'], y=df['idhm'], mode="markers", name="população residente em domicílio com água encanada"))
fig_idh_aguaban.add_trace(go.Scattergl(x=df['t_banagua'], y=df['idhm'], mode="markers", name="população residente em domicílio com banheiro e água encanada"))
fig_idh_aguaban.legend(loc='upper center', bbox_to_anchor=(0.5,-0.05), fancybox=True, shadow=True, ncol=5)
fig_idh_aguaban.update_xaxes(title_text="Percentual da população")
fig_idh_aguaban.update_yaxes(title_text="Idhm")
st.plotly_chart(fig_idh_aguaban)
