import streamlit as st
import pandas as pd
import plotly.express as px
import PIL
from PIL import Image

df = pd.read_csv("atlas.csv")
idh_composicao = Image.open('idh_composicao.png')
idh_faixas = Image.open('idh_faixas.png')
fig_gini_esc = px.box(df, x='gini', y='i_escolaridade')


st.title('IDH')
texto1 = 'Cesar School - Curso de Especialização em Engenharia e Análise de Dados\nProjeto Final da Disciplina Análise e Visualização de Dados\nEquipe 12: Arthur Perruci, Daniel Duarte, Enio Kilder'
st.text(texto1)

tab1, tab2, tab3, tab4 = st.tabs(["Entenda IDH","ou","Gini e Escolaridade","Tabela de dados"])

with tab1:
   st.markdown("**O que representa o Índice de Desenvolvimento Humano - IDH**")
   st.text("O Índice de Desenvolvimento Humano (IDH) compara indicadores de países\nnos itens riqueza, alfabetização, educação, esperança de vida, natalidade e outros,\ncom o intuito de avaliar o bem-estar de uma população")
   st.write("fonte: IPEA / Desafios do Desenvolvimento ( https://encurtador.com.br/eQS35 )")
   st.image(idh_composicao)
   st.write("O valor do IDH varia de 0 (zero) a 1, e conforme o valor pode ser considerado de muito baixo a muito alto conforme as faxias descritas na figura.")
   st.image(idh_faixas)
   st.write("Reproduzido de IPEA / O Índice de Desenvolvimento Humano Municipal Brasileiro (disponível para download em: https://repositorio.ipea.gov.br/handle/11058/2375) ")

with tab2:
   st.markdown("**ou**")
   st.sidebar.markdown('## Filtro para o gráfico')

   def plot_estoque(dataframe, categoria):
      df = df[(df["ano"] == categoria)]
      fig = df.plot(kind="scatter", figsize=(15, 8), x='corte9', y='i_escolaridade', c='idhm')
      return fig
    #fig, ax = plt.subplots(figsize=(8,6))
    #ax = sns.barplot(x = 'Produto', y = 'Quantidade', data = dados_plot)
    #ax.set_title(f'Quantidade em estoque dos produtos de {categoria}', f

   categoria_grafico = st.sidebar.selectbox('Selecione o ano para apresentar no gráfico', options = df['ano'].unique())
   df = df[(df["ano"] == categoria_grafico)]
   df.plot(kind="scatter", figsize=(15, 8), x='corte9', y='i_escolaridade', c='idhm')
   
#figura = plot_estoque(df, categoria_grafico)
   #st.pyplot(figura)


with tab3:
   st.markdown("**GINI e escolaridade**")
   st.plotly_chart(fig_gini_esc)

with tab4:
   st.markdown("**Tabela base**")   
   df
