import streamlit as st
st.write('DASH BOARD IDH')
import altair as alt
import pandas as pd
from vega_datasets import data

df = pd.read_csv("atlas.csv")
df
