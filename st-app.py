import streamlit as st
import pandas as pd

st.title('DASHBOARD IDH - EQUIPE 12')
st.write('DASH BOARD IDH')

df = pd.read_csv("atlas.csv")
df
