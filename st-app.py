import streamlit as st
import pandas as pd
import plotly.express as px
import matplotlib.pyplot as plt
import PIL
from PIL import Image
import plotly.graph_objects as go
from st_pages import Page, show_pages, add_page_title

fig_cesar = Image.open('assets/marca_cesar_school.png')
fig_idh_composicao = Image.open('assets/idh_composicao.png')

show_pages([
    Page("st-app.py", "Início", ":home:"),
    Page("pages/1_Entenda_o_Idh.py", "Entenda o IDH", ":curious:"),
    Page("pages/2_Evolução_do_Idh_nas_regioes.py", "Evolução do IDH nas Regiões", ":plot:"),
    Page("pages/3_IDH_Longevidade.py", "IDH - Longevidade", ":old_man:"),
    Page("pages/4_IDH_Educação.py", "IDH - Educação", ":books:"),
    Page("pages/5_IDH_Renda.py", "IDH - Renda", ":coin:"),
  ])

#st.set_page_config(page_title="Início", page_icon=":home:")
st.title('IDH')
st.write('Cesar School - Curso de Especialização em Engenharia e Análise de Dados')
st.write('Projeto Final da Disciplina Análise e Visualização de Dados')
st.write('Equipe 12: Arthur Perruci, Daniel Duarte, Enio Kilder')

col1, col2 = st.columns(2)
with col1:
  st.image(fig_cesar)
with col2:
  st.image(fig_idh_composicao)
