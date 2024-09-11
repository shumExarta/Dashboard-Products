import streamlit as st
import pandas as pd
import plotly.express as px
import time
import random
from functions import zeniva_shopify_stats
st.set_page_config(layout='centered')

col1, col2, col3 = st.columns(3)
with col1:
    zeniva_btn = st.button("Zeniva")
with col2:
    odyessey_btn = st.button("Odyssey")
with col3:
    exarta_btn = st.button("Exarta")

if zeniva_btn:
    st.write("Zeniva")
    zeniva_data = pd.read_csv('./data/zeniva_social.csv')
    placeholder = st.empty()
    
    zeniva_shopify, zeniva_youtube, zeniva_meta, zeniva_pcc = zeniva_shopify_stats(zeniva_data)
    
    fig1 = px.histogram(zeniva_shopify, x='platform', y=['daily_installs', 'clicks', 'daily_spend', ], barmode='group', title="Zeniva Data on Shopify")
    placeholder.plotly_chart(fig1)
    time.sleep(2)

    fig2 = px.histogram(zeniva_youtube, x='platform', y=['clicks', 'daily_spend', 'views', ], barmode='group', title="Zeniva Data Youtube")
    placeholder.plotly_chart(fig2)
    time.sleep(2)
    
    fig3 = px.histogram(zeniva_meta, x='platform', y=['clicks','reach', 'per_day_cost'], barmode='group', title="Zeniva Data on Meta")
    placeholder.plotly_chart(fig3)
    time.sleep(2)
    
    fig4 = px.histogram(zeniva_pcc, x='platform', y=['clicks', 'daily_spend', 'impressions'], barmode='group', title="Zeniva Data on PCC")
    placeholder.plotly_chart(fig4)
    time.sleep(2)
    
# # Load the data into a pandas DataFrame
# zeniva_data = pd.read_csv('./data/zeniva_social.csv')
# placeholder = st.empty()

# zeniva_shopify, zeniva_youtube = zeniva_shopify_stats(zeniva_data)

# fig1 = px.histogram(zeniva_shopify, x='platform', y=['daily_installs', 'clicks', 'daily_spend', ], barmode='group', title="Histogram of Zeniva Data by Platform")
# placeholder.plotly_chart(fig1)
# time.sleep(2)

# fig2 = px.histogram(zeniva_youtube, x='platform', y=['clicks', 'daily_spend', 'views', ], barmode='group', title="Histogram of Zeniva Data by Platform")
# placeholder.plotly_chart(fig2)
# time.sleep(2)

# placeholder.write(zeniva_shopify)
# time.sleep(3)

# placeholder.write(zeniva_youtube)
# time.sleep(3)

# placeholder.write(zeniva_meta)
# time.sleep(3)

# placeholder.write(zeniva_pcc)
# time.sleep(3)