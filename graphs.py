import streamlit as st
import pandas as pd
import plotly.express as px
from functions import plot_zeniva_youtube_metrics,plot_zeniva_meta_metrics

df = pd.read_csv("./data/graph_data_fri.csv")
filled_df = df.fillna(0)

st.write(filled_df)



col1,col2,co3 = st.columns(3)
with col1:
    plot_zeniva_youtube_metrics(filled_df)
with col2:
    plot_zeniva_meta_metrics(filled_df)

