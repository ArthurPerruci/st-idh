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

#carregamento de imagens

st.set_page_config(page_title="IDH Renda", page_icon=":money:")
st.title('IDH - Renda')
#st.image(fig_long_esp_vid)
#st.image(fig_long_sobr_40)
#st.image(fig_long_sobr_60)

st.markdown("Vários indicadores relacionados a longevidade, educação e renda são utilizados no cálculo do idh. No gráfico abaixo verifica-se a relação dos indicadores relacionados à renda com o idh-r e idh final. No gráfico destacam-se como mais forte a relação do idhm com os indicadores de renda per capta (em vários recortes) e percentual de população residente em domicílios com água encanada e banheiro.")
ano_grafico = st.sidebar.selectbox('Ano', df['ano'].unique())
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
