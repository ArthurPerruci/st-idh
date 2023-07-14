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

st.set_page_config(page_title="IDH Educação", page_icon=":book:")
st.title('IDH - Educação')
#st.image(fig_long_esp_vid)
#st.image(fig_long_sobr_40)
#st.image(fig_long_sobr_60)

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
