import streamlit as st
import pandas as pd
import plotly.express as px
import matplotlib.pyplot as plt
import PIL
from PIL import Image
import plotly.graph_objects as go

fig_cesar = Image.open('assets/marca_cesar_school.png')
fig_idh_composicao = Image.open('assets/idh_composicao.png')

st.title('IDH')
st.write('Cesar School - Curso de Especialização em Engenharia e Análise de Dados')
st.write('Projeto Final da Disciplina Análise e Visualização de Dados')
st.write('Equipe 12: Arthur Perruci, Daniel Duarte, Enio Kilder')

col1, col2 = st.columns(2)
with col1:
  st.image(fig_cesar)
with col2:
  st.image(fig_idh_composicao)
