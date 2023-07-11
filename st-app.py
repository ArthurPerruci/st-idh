import streamlit as st
import pandas as pd
import plotly.express as px
import matplotlib.pyplot as plt
import PIL
from PIL import Image
import plotly.graph_objects as go

#Leitura do data frame
df = pd.read_csv("atlas.csv")

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
idh_composicao = Image.open('idh_composicao.png')
idh_faixas = Image.open('idh_faixas.png')

st.title('IDH')
texto1 = 'Cesar School - Curso de Especialização em Engenharia e Análise de Dados\nProjeto Final da Disciplina Análise e Visualização de Dados\nEquipe 12: Arthur Perruci, Daniel Duarte, Enio Kilder'
st.text(texto1)

#Estruturação das tabs
tab1, tab2, tab3, tab4 = st.tabs(["Entenda IDH", "IDH por Região", "IDH e GINI", "Composição do IDH"])

with tab1:
   st.markdown("**O que representa o Índice de Desenvolvimento Humano - IDH**")
   st.text("O Índice de Desenvolvimento Humano (IDH) compara indicadores de países\nnos itens riqueza, alfabetização, educação, esperança de vida, natalidade e outros,\ncom o intuito de avaliar o bem-estar de uma população")
   st.write("fonte: IPEA / Desafios do Desenvolvimento ( https://encurtador.com.br/eQS35 )")
   st.image(idh_composicao)
   st.write("O valor do IDH varia de 0 (zero) a 1, e conforme o valor pode ser considerado de muito baixo a muito alto conforme as faxias descritas na figura.")
   st.image(idh_faixas)
   st.write("Reproduzido de IPEA / O Índice de Desenvolvimento Humano Municipal Brasileiro (disponível para download em: https://repositorio.ipea.gov.br/handle/11058/2375) ")

with tab2:
   st.markdown("O gráfico mostra a evolução dos valores médios de idhm das cinco regiões brasileiras. Fica evidente um processo de incremento dos valores de idh entre 1991 e 2010. Percebe-se também que os valores de idh nas regiões norte e nordeste são discretamente inferiores que os das demais regiões, da mesma maneira precebe-se que esta diferença diminuiu um pouco no período.")
   st.sidebar.markdown('Filtros para o gráfico')
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


with tab3:
   st.markdown("O Índice de Gini mede o grau de concentração de renda. Ele aponta a diferença entre os rendimentos dos mais pobres e dos mais ricos. Varia de zero a um, onde zero representa a situação de igualdade (todos têm a mesma renda) e um é extremo oposto (uma só pessoa detém toda a riqueza).")
   st.write("fonte: IPEA / Desafios do Desenvolvimento ( https://www.ipea.gov.br/desafios/index.php?option=com_content&id=2048:catid=28 )")
   st.markdown("O gráfico evidencia que não há uma relação forte entre o valor do idhm e do gini, independente do ano e da região.")
   ano_grafico = st.sidebar.selectbox('Ano', df['ano'].unique())
   df = df.loc[df['ano'] == ano_grafico]
   fig_idh_gini = px.scatter(df, x="gini", y="idhm", color="regiao")
   fig_idh_gini.update_layout(title="Relação IDH x GINI")
   st.plotly_chart(fig_idh_gini)
   st.text("Os dados foram capturados em três anos base: 1991, 2000 e 2010.\nEscolha o ano a ser visualizado na barra à esquerda.\nNo gráfico cada esfera representa um município.\nClique no nome da Região para ocultá-la ou visualizá-la.")

with tab4:
   st.markdown("Vários indicadores relacionados à saúde, educação e renda são utilizados no cálculo do idh. Aque escolhemos alguns para ver o grau de relação com o idh final.")
   df = df.loc[df['ano'] == ano_grafico]
   comp = ['idhm', 'espvida', 'mort1', 't_env', 't_analf18m', 'e_anosestudo', 'tmed25m', 'rdpc', 'gini', 'pmpob']
   fig_comp_idh = px.imshow(comp, text_auto=True, aspect="auto")
   fig_comp_idh.update_layout(title="composição do IDH")
   st.plotly_chart(fig_comp_idh)
