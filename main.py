import streamlit as st
import pandas as pd
import plotly.express as px
import matplotlib.pyplot as plt
import time
import random
from functions import get_platform_data, get_zeniva_platform_stats, histogram_data, get_comparison_stats, filtering_data_for_graph_exarta, filtering_data_for_graph_odyessey, filtering_data_for_graph_zeniva, plot_histograms_zeniva
st.set_page_config(layout='wide')

df = pd.read_csv('./data/graph_data_final.csv')
data = df.fillna(0)

# youtube_data, meta_data, ppc_data = get_platform_data()
# youtube_data_zeniva, meta_data_zeniva, ppc_data_zeniva, linkedin_data_zeniva, x_data_zeniva, shopify_data_zeniva = filtering_data_for_graph_zeniva(data_for_graph)
# youtube_data_ody, meta_data_ody, ppc_data_ody, linkedin_data_ody, x_data_ody, shopify_data_ody = filtering_data_for_graph_odyessey(data_for_graph)
# youtube_data_exarta, meta_data_exarta, ppc_data_exarta, linkedin_data_exarta, x_data_exarta, shopify_data_exarta = filtering_data_for_graph_exarta(data_for_graph)

zen_col, ody_col, exa_col, comp_col = st.columns(4)
with zen_col:
    zen_btn = st.button("Zeniva")
    
with ody_col:
    ody_btn = st.button("Odyessey")
    
with exa_col:
    exa_btn = st.button("Exarta")
    
with comp_col:
    comp_btn = st.button("Comparison")

if zen_btn:
    placeholder = st.empty()
    with placeholder.container():
        col1, col2, col3 = st.columns(3)
        col4, col5, col6 = st.columns(3)
        with col1:
            st.header("Youtube")
            df = pd.read_csv("./data/zeniva_social.csv")
            total_followers_youtube = df[df["platform"] == "youtube"]["total_followers"].sum()
            today_followers_youtube = df[df["platform"] == "youtube"]["today_followers"].sum()
            yesterday_followers_youtube = df[df["platform"] == "youtube"]["yesterday_follwers"].sum()
            
            
            st.write(f"Total followers : {total_followers_youtube}")
            st.write(f"Today followers : {today_followers_youtube}")
            st.write(f"Yesterday followers : {yesterday_followers_youtube}")
        
        with col2:
            st.header("Meta")
            df = pd.read_csv("./data/zeniva_social.csv")
            total_followers_meta = df[df["platform"] == "meta"]["total_followers"].sum()
            today_followers_meta = df[df["platform"] == "meta"]["today_followers"].sum()
            yesterday_followers_meta = df[df["platform"] == "youtube"]["yesterday_follwers"].sum()
            
            st.write(f"Total followers : {total_followers_meta}")
            st.write(f"Today followers : {today_followers_meta}")
            st.write(f"Yesterday followers : {yesterday_followers_meta}")
        
        with col3:
            st.header("LinkedIn")
            df = pd.read_csv("./data/zeniva_social.csv")
            total_followers_link = df[df["platform"] == "meta"]["total_followers"].sum()
            today_followers_link = df[df["platform"] == "meta"]["today_followers"].sum()
            yesterday_followers_link = df[df["platform"] == "youtube"]["yesterday_follwers"].sum()
            
            st.write(f"Total followers : {total_followers_link}")
            st.write(f"Today followers : {today_followers_link}")
            st.write(f"Yesterday followers : {yesterday_followers_link}")
            
        with col4:
            st.header("PPC")
            df = pd.read_csv("./data/zeniva_social.csv")
            total_followers_pcc = df[df["platform"] == "meta"]["total_followers"].sum()
            today_followers_pcc = df[df["platform"] == "meta"]["today_followers"].sum()
            yesterday_followers_pcc = df[df["platform"] == "youtube"]["yesterday_follwers"].sum()
            
            st.write(f"Total followers : {total_followers_pcc}")
            st.write(f"Today followers : {today_followers_pcc}")
            st.write(f"Yesterday followers : {yesterday_followers_pcc}")
            
        with col5:
            st.header("Shopify Ads")
            df = pd.read_csv("./data/zeniva_social.csv")
            total_followers_shop = df[df["platform"] == "meta"]["total_followers"].sum()
            today_followers_shop = df[df["platform"] == "meta"]["today_followers"].sum()
            yesterday_followers_shop = df[df["platform"] == "youtube"]["yesterday_follwers"].sum()
            
            st.write(f"Total followers : {total_followers_shop}")
            st.write(f"Today followers : {today_followers_shop}")
            st.write(f"Yesterday followers : {yesterday_followers_shop}")
        with col6:
            st.header("X")
            df = pd.read_csv("./data/zeniva_social.csv")
            total_followers_x = df[df["platform"] == "meta"]["total_followers"].sum()
            today_followers_x = df[df["platform"] == "meta"]["today_followers"].sum()
            yesterday_followers_x = df[df["platform"] == "youtube"]["yesterday_follwers"].sum()
            
            st.write(f"Total followers : {total_followers_x}")
            st.write(f"Today followers : {today_followers_x}")
            st.write(f"Yesterday followers : {yesterday_followers_x}")

    time.sleep(1)
    placeholder.empty()
    col7, col8, col9 = st.columns(3)
    col10, col11 = st.columns(2)
    
    with col7:
        plot_histograms_zeniva('zeniva', 'youtube', data)
    with col8:
        plot_histograms_zeniva('zeniva', 'meta', data)
    with col9:
        plot_histograms_zeniva('zeniva', 'shopify', data)

        
if ody_btn:
    placeholder = st.empty()
    with placeholder.container():
        st.title("Odyessey stats accross all platforms")
        col1, col2, col3 = st.columns(3)
        col4, col5, col6 = st.columns(3)

        with col1:
            st.header("Youtube")
            df = pd.read_csv("./data/zeniva_social.csv")
            total_followers_youtube1 = df[df["platform"] == "youtube"]["total_followers"].sum()
            today_followers_youtube1 = df[df["platform"] == "youtube"]["today_followers"].sum()
            yesterday_followers_youtube1 = df[df["platform"] == "youtube"]["yesterday_follwers"].sum()
            
            st.write(f"Total followers : {total_followers_youtube1}")
            st.write(f"Today followers : {today_followers_youtube1}")
            st.write(f"Yesterday followers : {yesterday_followers_youtube1}")
            
        with col2:
            st.header("Meta")
            df = pd.read_csv("./data/zeniva_social.csv")
            total_followers_meta1 = df[df["platform"] == "meta"]["total_followers"].sum()
            today_followers_meta1 = df[df["platform"] == "meta"]["today_followers"].sum()
            yesterday_followers_meta1 = df[df["platform"] == "youtube"]["yesterday_follwers"].sum()
            
            st.write(f"Total followers : {total_followers_meta1}")
            st.write(f"Today followers : {today_followers_meta1}")
            st.write(f"Yesterday followers : {yesterday_followers_meta1}")

        with col3:
            st.header("PPC")
            df = pd.read_csv("./data/zeniva_social.csv")
            total_followers_ppc1 = df[df["platform"] == "meta"]["total_followers"].sum()
            today_followers_ppc1 = df[df["platform"] == "meta"]["today_followers"].sum()
            yesterday_followers_ppc1 = df[df["platform"] == "youtube"]["yesterday_follwers"].sum()

            st.write(f"Total followers : {total_followers_ppc1}")
            st.write(f"Today followers : {today_followers_ppc1}")
            st.write(f"Yesterday followers : {yesterday_followers_ppc1}")
            
        with col4:
            st.header("Shopify Ads")
            df = pd.read_csv("./data/zeniva_social.csv")
            total_followers_shop1 = df[df["platform"] == "meta"]["total_followers"].sum()
            today_followers_shop1 = df[df["platform"] == "meta"]["today_followers"].sum()
            yesterday_followers_shop1 = df[df["platform"] == "youtube"]["yesterday_follwers"].sum()

            st.write(f"Total followers : {total_followers_shop1}")
            st.write(f"Today followers : {today_followers_shop1}")
            st.write(f"Yesterday followers : {yesterday_followers_shop1}")

        with col5:
            st.header("X")
            df = pd.read_csv("./data/zeniva_social.csv")
            total_followers_x1 = df[df["platform"] == "meta"]["total_followers"].sum()
            today_followers_x1 = df[df["platform"] == "meta"]["today_followers"].sum()
            yesterday_followers_x1 = df[df["platform"] == "youtube"]["yesterday_follwers"].sum()
            
            st.write(f"Total followers : {total_followers_x1}")
            st.write(f"Today followers : {today_followers_x1}")
            st.write(f"Today followers : {yesterday_followers_x1}")
            
        with col6:
            pass
    time.sleep(10)
    placeholder.empty()
    
    col7, col8, col9 = st.columns(3)
    col10, col11, col12 = st.columns(3)
    with col7:
        plot_histograms('odyessey', 'youtube', data)
    with col8:
        plot_histograms('odyessey', 'meta', data)
    with col9:
        plot_histograms('odyessey', 'linkedin', data)
    with col10:
       plot_histograms('odyessey', 'ppc', data)
    with col11:
       plot_histograms('odyessey', 'shopify', data)
    with col12:
       plot_histograms('odyessey', 'x', data)
    
    time.sleep(1)
    placeholder.empty()
    
    
if exa_btn:
    placeholder = st.empty()
    with placeholder.container():
        st.title("Odyessey stats accross all platforms")
        col1, col2, col3 = st.columns(3)
        col4, col5, col6 = st.columns(3)

        with col1:
            st.header("Youtube")
            df = pd.read_csv("./data/zeniva_social.csv")
            total_followers_youtube1 = df[df["platform"] == "youtube"]["total_followers"].sum()
            today_followers_youtube1 = df[df["platform"] == "youtube"]["today_followers"].sum()
            yesterday_followers_youtube1 = df[df["platform"] == "youtube"]["yesterday_follwers"].sum()
            
            st.write(f"Total followers : {total_followers_youtube1}")
            st.write(f"Today followers : {today_followers_youtube1}")
            st.write(f"Yesterday followers : {yesterday_followers_youtube1}")
            
        with col2:
            st.header("Meta")
            df = pd.read_csv("./data/zeniva_social.csv")
            total_followers_meta1 = df[df["platform"] == "meta"]["total_followers"].sum()
            today_followers_meta1 = df[df["platform"] == "meta"]["today_followers"].sum()
            yesterday_followers_meta1 = df[df["platform"] == "youtube"]["yesterday_follwers"].sum()
            
            st.write(f"Total followers : {total_followers_meta1}")
            st.write(f"Today followers : {today_followers_meta1}")
            st.write(f"Yesterday followers : {yesterday_followers_meta1}")

        with col3:
            st.header("PPC")
            df = pd.read_csv("./data/zeniva_social.csv")
            total_followers_ppc1 = df[df["platform"] == "meta"]["total_followers"].sum()
            today_followers_ppc1 = df[df["platform"] == "meta"]["today_followers"].sum()
            yesterday_followers_ppc1 = df[df["platform"] == "youtube"]["yesterday_follwers"].sum()

            st.write(f"Total followers : {total_followers_ppc1}")
            st.write(f"Today followers : {today_followers_ppc1}")
            st.write(f"Yesterday followers : {yesterday_followers_ppc1}")
            
        with col4:
            st.header("Shopify Ads")
            df = pd.read_csv("./data/zeniva_social.csv")
            total_followers_shop1 = df[df["platform"] == "meta"]["total_followers"].sum()
            today_followers_shop1 = df[df["platform"] == "meta"]["today_followers"].sum()
            yesterday_followers_shop1 = df[df["platform"] == "youtube"]["yesterday_follwers"].sum()

            st.write(f"Total follwers : {total_followers_shop1}")
            st.write(f"Today follwers : {today_followers_shop1}")
            st.write(f"Yesterday follwers : {yesterday_followers_shop1}")

        with col5:
            st.header("X")
            df = pd.read_csv("./data/zeniva_social.csv")
            total_followers_x1 = df[df["platform"] == "meta"]["total_followers"].sum()
            today_followers_x1 = df[df["platform"] == "meta"]["today_followers"].sum()
            yesterday_followers_x1 = df[df["platform"] == "youtube"]["yesterday_follwers"].sum()
            
            st.write(f"Total followers : {total_followers_x1}")
            st.write(f"Today followers : {today_followers_x1}")
            st.write(f"Today followers : {yesterday_followers_x1}")
            
        with col6:
            pass
        
    time.sleep(10)
    placeholder.empty()
    
    col7, col8, col9 = st.columns(3)
    col10, col11, col12 = st.columns(3)
    with col7:
        plot_histograms('exarta', 'youtube', data)
    with col8:
        plot_histograms('exarta', 'meta', data)
    with col9:
        plot_histograms('exarta', 'linkedin', data)
    with col10:
       plot_histograms('exarta', 'ppc', data)
    with col11:
       plot_histograms('exarta', 'shopify', data)
    with col12:
       plot_histograms('exarta', 'x', data)
    
    time.sleep(1)
    placeholder.empty()


if comp_btn:
    placeholder = st.empty()
    st.title("Overall stats")
    comparison_df = pd.read_csv("./data/comparisons.csv")
    zeniva_stats, ody_stats = get_comparison_stats(comparison_df)
    zen_col, ody_col = st.columns(2)
    with zen_col:
        st.metric("New Installs", zeniva_stats['new_installs'])
        st.metric("Total Installs", zeniva_stats['total_installs'])
        st.metric("Free Users", zeniva_stats['free_users'])
        st.metric("Paid Users", zeniva_stats['paid_users'])
        st.metric("Today Uninstalls", zeniva_stats['today_uninstalls'])
        st.metric("Total Uninstalls", zeniva_stats['total_uninstalls'])
    with ody_col:
        st.metric("New Installs", ody_stats['new_installs'])
        st.metric("Total Installs", ody_stats['total_installs'])
        st.metric("Free Users", ody_stats['free_users'])
        st.metric("Paid Users", ody_stats['paid_users'])
        st.metric("Today Uninstalls", ody_stats['today_uninstalls'])
        st.metric("Total Uninstalls", ody_stats['total_uninstalls'])