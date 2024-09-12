import pandas as pd
import streamlit as st
import plotly.express as px
from functions import plot_histograms

data = pd.read_csv('./data/graph_data.csv')

col1, col2, col3 = st.columns(3)
with col1:
    plot_histograms('exarta','linkedin', data)
with col2:
    plot_histograms('exarta', 'x', data)