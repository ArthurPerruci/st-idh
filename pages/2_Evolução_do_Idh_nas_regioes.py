import streamlit as st
import pandas as pd
import plotly.express as px
import matplotlib.pyplot as plt
import PIL
from PIL import Image
import plotly.graph_objects as go
from st_pages import Page, show_pages

show_pages([
  Page("st-app.py", "Início", ":house:"),
  Page("pages/1_Entenda_o_Idh.py", "Entenda o IDH", ":thinking_face:"),
  Page("pages/2_Evolução_do_Idh_nas_regioes.py", "Evolução do IDH nas Regiões", ":chart_with_upwards_trend:"),
  Page("pages/3_IDH_Longevidade.py", "IDH - Longevidade", ":older_man:"),
  Page("pages/4_IDH_Educação.py", "IDH - Educação", ":books:"),
  Page("pages/5_IDH_Renda.py", "IDH - Renda", ":moneybag:"),
  ])

#Leitura do data frame
df = pd.read_csv("data/atlas.csv")

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

st.title('A evolução do IDH nas regiões brasileiras no período de 1991 a 2010')
df_sul = df.loc[df['regiao'] == 'Sul']
df_sul_91 = df_sul.loc[df_sul['ano'] == 1991]
df_sul_00 = df_sul.loc[df_sul['ano'] == 2000]  
df_sul_10 = df_sul.loc[df_sul['ano'] == 2010]
idhm_sul_91 = df_sul_91['idhm'].sum()/len(df_sul_91)
idhm_sul_00 = df_sul_00['idhm'].sum()/len(df_sul_00)
idhm_sul_10 = df_sul_10['idhm'].sum()/len(df_sul_10)
idh_sul_evo = [idhm_sul_91, idhm_sul_00, idhm_sul_10]
df_sudeste = df.loc[df['regiao'] == 'Sudeste']
df_sudeste_91 = df_sudeste.loc[df_sudeste['ano'] == 1991]
df_sudeste_00 = df_sudeste.loc[df_sudeste['ano'] == 2000]
df_sudeste_10 = df_sudeste.loc[df_sudeste['ano'] == 2010]
idhm_sudeste_91 = df_sudeste_91['idhm'].sum()/len(df_sudeste_91)
idhm_sudeste_00 = df_sudeste_00['idhm'].sum()/len(df_sudeste_00)
idhm_sudeste_10 = df_sudeste_10['idhm'].sum()/len(df_sudeste_10)
idh_sudeste_evo = [idhm_sudeste_91, idhm_sudeste_00, idhm_sudeste_10]
df_centro_oeste = df.loc[df['regiao'] == 'Centro Oeste']
df_centro_oeste_91 = df_centro_oeste.loc[df_centro_oeste['ano'] == 1991]
df_centro_oeste_00 = df_centro_oeste.loc[df_centro_oeste['ano'] == 2000]
df_centro_oeste_10 = df_centro_oeste.loc[df_centro_oeste['ano'] == 2010]
idhm_centro_oeste_91 = df_centro_oeste_91['idhm'].sum()/len(df_centro_oeste_91) 
idhm_centro_oeste_00 = df_centro_oeste_00['idhm'].sum()/len(df_centro_oeste_00)
idhm_centro_oeste_10 = df_centro_oeste_10['idhm'].sum()/len(df_centro_oeste_10)
idh_centro_oeste_evo = [idhm_centro_oeste_91, idhm_centro_oeste_00, idhm_centro_oeste_10]
df_nordeste = df.loc[df['regiao'] == 'Nordeste']
df_nordeste_91 = df_nordeste.loc[df_nordeste['ano'] == 1991]
df_nordeste_00 = df_nordeste.loc[df_nordeste['ano'] == 2000]
df_nordeste_10 = df_nordeste.loc[df_nordeste['ano'] == 2010]
idhm_nordeste_91 = df_nordeste_91['idhm'].sum()/len(df_nordeste_91) 
idhm_nordeste_00 = df_nordeste_00['idhm'].sum()/len(df_nordeste_00) 
idhm_nordeste_10 = df_nordeste_10['idhm'].sum()/len(df_nordeste_10)
idh_nordeste_evo = [idhm_nordeste_91, idhm_nordeste_00, idhm_nordeste_10]
df_norte = df.loc[df['regiao'] == 'Norte']
df_norte_91 = df_norte.loc[df_norte['ano'] == 1991]
df_norte_00 = df_norte.loc[df_norte['ano'] == 2000]
df_norte_10 = df_norte.loc[df_norte['ano'] == 2010]
idhm_norte_91 = df_norte_91['idhm'].sum()/len(df_norte_91) 
idhm_norte_00 = df_norte_00['idhm'].sum()/len(df_norte_00) 
idhm_norte_10 = df_norte_10['idhm'].sum()/len(df_norte_10)
idh_norte_evo = [idhm_norte_91, idhm_norte_00, idhm_norte_10]
anos = [1991, 2000, 2010]
fig_idh_reg = go.Figure()
fig_idh_reg.add_trace(go.Scatter(x=anos, y=idh_sul_evo, name="Sul"))
fig_idh_reg.add_trace(go.Scatter(x=anos, y=idh_sudeste_evo, name="Sudeste"))
fig_idh_reg.add_trace(go.Scatter(x=anos, y=idh_centro_oeste_evo, name="Centro Oeste"))
fig_idh_reg.add_trace(go.Scatter(x=anos, y=idh_nordeste_evo, name="Nordeste"))
fig_idh_reg.add_trace(go.Scatter(x=anos, y=idh_norte_evo, name="Norte"))
fig_idh_reg.update_layout(
   title="Evolução do IDH médio por Região",
   xaxis_title="Ano",
   yaxis_title="idhm"
   )
st.plotly_chart(fig_idh_reg)
st.markdown("O gráfico mostra a evolução dos valores médios de idhm das cinco regiões brasileiras. Fica evidente um processo de incremento dos valores de idh entre 1991 e 2010. Percebe-se também que os valores de idh nas regiões norte e nordeste são discretamente inferiores que os das demais regiões, da mesma maneira precebe-se que esta diferença diminuiu um pouco no período.")
