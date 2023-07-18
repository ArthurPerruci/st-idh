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

#carregamento de imagens
idh_composicao = Image.open('assets/idh_composicao.png')
idh_faixas = Image.open('assets/idh_faixas.png')

st.title('Entenda o IDH')
st.markdown("**O que representa o Índice de Desenvolvimento Humano - IDH**")
st.image(idh_composicao)
st.write("O Índice de Desenvolvimento Humano (IDH) compara indicadores de países nos itens riqueza, alfabetização, educação, esperança de vida, natalidade e outros, com o intuito de avaliar o bem-estar de uma população")
st.write("fonte: IPEA / Desafios do Desenvolvimento ( https://encurtador.com.br/eQS35 )")
st.write("O valor do IDH varia de 0 (zero) a 1, e conforme o valor pode ser considerado de muito baixo a muito alto conforme as faxias descritas na figura.")
st.image(idh_faixas)
st.write("Reproduzido de IPEA / O Índice de Desenvolvimento Humano Municipal Brasileiro (disponível para download em: https://repositorio.ipea.gov.br/handle/11058/2375) ")

