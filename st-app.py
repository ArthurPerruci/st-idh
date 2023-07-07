import streamlit as st
import pandas as pd

st.title('DASHBOARD IDH - EQUIPE 12')
st.write('DASH BOARD IDH')
tab1, tab2, tab3 = st.tabs(["Cat", "Dog", "Tabela de dados"])

with tab1:
   st.header("A cat")
   st.image("https://static.streamlit.io/examples/cat.jpg", width=200)

with tab2:
   st.header("A dog")
   st.image("https://static.streamlit.io/examples/dog.jpg", width=200)

with tab3:
   st.header("An owl")
   st.image("https://static.streamlit.io/examples/owl.jpg", width=200)
   df = pd.read_csv("atlas.csv")
   df
