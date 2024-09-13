import pandas as pd
import plotly.express as px
import streamlit as st

def histogram_data():
    data = pd.read_csv('./data/cleaned_sample_random.csv')
    data.dropna(inplace=True)
    
    # Separate data for each platform
    youtube_data = data[data['Platform'] == 'youtube'].reset_index(drop=True)
    meta_data = data[data['Platform'] == 'meta'].reset_index(drop=True)
    ppc_data = data[data['Platform'] == 'ppc'].reset_index(drop=True)
    shopify_ads_data = data[data['Platform'] == 'shopify_ads'].reset_index(drop=True)
    
    return youtube_data, meta_data, ppc_data, shopify_ads_data


def get_stats():
    dataframe = pd.read_csv('./data/cleaned_sample_random.csv')
    zen_dat = dataframe[dataframe['Product'] == "Zeniva"]
    zeniva_summed_metrics = zen_dat.sum(numeric_only=True)
    
    ody_dat = dataframe[dataframe['Product'] == "Odassay"]
    ody_summed_metrics = ody_dat.sum(numeric_only=True)
    
    return zeniva_summed_metrics, ody_summed_metrics


def zeniva_shopify_stats(dataframe):
    zeniva_shopify = dataframe[dataframe['platform'] == 'shopify_ads']
    zeniva_shopify = zeniva_shopify.loc[:, (zeniva_shopify != 0).any(axis=0)]
    
    zeniva_youtube = dataframe[dataframe['platform'] == 'youtube']
    zeniva_youtube = zeniva_youtube.loc[:, (zeniva_youtube != 0).any(axis=0)]
    
    zeniva_meta = dataframe[dataframe['platform'] == 'meta']
    zeniva_meta = zeniva_meta.loc[:, (zeniva_meta != 0).any(axis=0)]
    
    zeniva_pcc = dataframe[dataframe['platform'] == 'PCC']
    zeniva_pcc = zeniva_pcc.loc[:, (zeniva_pcc != 0).any(axis=0)]

    return zeniva_shopify, zeniva_youtube, zeniva_meta, zeniva_pcc


def get_platform_data():
    dataframe = pd.read_csv('./data/cleaned_sample_random.csv')
    youtube_df = dataframe[dataframe['Platform'] == 'youtube'][['Platform', 'Metric', 'YouTube']]
    youtube_df.columns = ['platform', 'metric', 'value']
    meta_df = dataframe[dataframe['Platform'] == 'meta'][['Platform', 'Metric', 'Meta']]
    meta_df.columns = ['platform', 'metric', 'value']
    ppc_df = dataframe[dataframe['Platform'] == 'ppc'][['Platform', 'Metric', 'PPC']]
    ppc_df.columns = ['platform', 'metric', 'value']
        
    return youtube_df, meta_df, ppc_df


def get_zeniva_platform_stats():
    dataframe = pd.read_csv('./data/zeniva_social.csv')
    total_followers_youtube = dataframe[dataframe["platform"] == "youtube"]["total_followers"].sum()
    today_followers_youtube = dataframe[dataframe["platform"] == "youtube"]["today_followers"].sum()
    yesterday_followers_youtube = dataframe[dataframe["platform"] == "youtube"]["yesterday_follwers"].sum()
    
    total_followers_meta = dataframe[dataframe["platform"] == "meta"]["total_followers"].sum()
    today_followers_meta = dataframe[dataframe["platform"] == "meta"]["today_followers"].sum()
    yesterday_followers_meta = dataframe[dataframe["platform"] == "youtube"]["yesterday_follwers"].sum()
    
    return total_followers_youtube, today_followers_youtube, yesterday_followers_youtube, total_followers_meta, today_followers_meta, yesterday_followers_meta


def get_comparison_stats(dataframe):
    zeniva_data = dataframe[dataframe['Product'] == "Zeniva"]
    zeniva_summed_metrics = zeniva_data.sum(numeric_only=True)
    
    ody_data = dataframe[dataframe['Product'] == "Odassay"]
    ody_summed_metrics = ody_data.sum(numeric_only=True)
    
    return zeniva_summed_metrics, ody_summed_metrics


def filtering_data_for_graph_zeniva(dataframe):
    # FOR ZENIVA
    filter_product_exarta = dataframe[dataframe['product'] == 'zeniva']
    
    # FOR ZENIVA YOUTUBE
    filter_youtube_zeniva = filter_product_exarta[filter_product_exarta['platform'] == 'youtube']
    youtube_melted = filter_youtube_zeniva.melt(id_vars=['date'], value_vars=['views', 'clicks', 'daily_spend'], var_name='metric', value_name='value')
    # FOR ZENIVA META
    filter_meta_zeniva = filter_product_exarta[filter_product_exarta['platform'] == 'meta']
    meta_melted = filter_meta_zeniva.melt(id_vars=['date'], value_vars=['views', 'clicks', 'daily_spend'], var_name='metric', value_name='value')
    # FOR ZENIVA PPC
    filter_ppc_zeniva = filter_product_exarta[filter_product_exarta['platform'] == 'ppc']
    ppc_melted = filter_ppc_zeniva.melt(id_vars=['date'], value_vars=['views', 'clicks', 'daily_spend'], var_name='metric', value_name='value')
    # FOR ZENIVA LINKEDIN
    filter_linkedin_zeniva = filter_product_exarta[filter_product_exarta['platform'] == 'linkedin']
    linkedin_melted = filter_linkedin_zeniva.melt(id_vars=['date'], value_vars=['views', 'clicks', 'daily_spend'], var_name='metric', value_name='value')
    # FOR ZENVIA X
    filter_X_zeniva = filter_product_exarta[filter_product_exarta['platform'] == 'x']
    x_melted = filter_X_zeniva.melt(id_vars=['date'], value_vars=['views', 'clicks', 'daily_spend'], var_name='metric', value_name='value')
    # FOR ZENIVA SHOPIFY
    filter_shopify_zeniva = filter_product_exarta[filter_product_exarta['platform'] == 'shopify']
    shopify_melted = filter_shopify_zeniva.melt(id_vars=['date'], value_vars=['views', 'clicks', 'daily_spend'], var_name='metric', value_name='value')
    
    return youtube_melted, meta_melted, ppc_melted, linkedin_melted, x_melted, shopify_melted


def filtering_data_for_graph_odyessey(dataframe):
    # FOR EXARTA
    filter_product_exarta = dataframe[dataframe['product'] == 'odyessey']
    
    # FOR ODY YOUTUBE
    filter_youtube_ody = filter_product_exarta[filter_product_exarta['platform'] == 'youtube']
    youtube_melted = filter_youtube_ody.melt(id_vars=['date'], value_vars=['views', 'clicks', 'daily_spend'], var_name='metric', value_name='value')
    # FOR ODY META
    filter_meta_ody = filter_product_exarta[filter_product_exarta['platform'] == 'meta']
    meta_melted = filter_meta_ody.melt(id_vars=['date'], value_vars=['views', 'clicks', 'daily_spend'], var_name='metric', value_name='value')
    # FOR ODY PPC
    filter_ppc_ody = filter_product_exarta[filter_product_exarta['platform'] == 'ppc']
    ppc_melted = filter_ppc_ody.melt(id_vars=['date'], value_vars=['views', 'clicks', 'daily_spend'], var_name='metric', value_name='value')
    # FOR ODY LINKEDIN
    filter_linkedin_ody = filter_product_exarta[filter_product_exarta['platform'] == 'linkedin']
    linkedin_melted = filter_linkedin_ody.melt(id_vars=['date'], value_vars=['views', 'clicks', 'daily_spend'], var_name='metric', value_name='value')
    # FOR ODY X
    filter_X_ody = filter_product_exarta[filter_product_exarta['platform'] == 'x']
    x_melted = filter_X_ody.melt(id_vars=['date'], value_vars=['views', 'clicks', 'daily_spend'], var_name='metric', value_name='value')
    # FOR ODY SHOPIFY
    filter_shopify_ody = filter_product_exarta[filter_product_exarta['platform'] == 'shopify']
    shopify_melted = filter_shopify_ody.melt(id_vars=['date'], value_vars=['views', 'clicks', 'daily_spend'], var_name='metric', value_name='value')
    
    return youtube_melted, meta_melted, ppc_melted, linkedin_melted, shopify_melted, x_melted


def filtering_data_for_graph_exarta(dataframe):
    # FOR EXARTA
    filter_product_exarta = dataframe[dataframe['product'] == 'exarta']
    
    # FOR EXARTA YOUTUBE
    filter_youtube_exarta = filter_product_exarta[filter_product_exarta['platform'] == 'youtube']
    youtube_melted = filter_youtube_exarta.melt(id_vars=['date'], value_vars=['views', 'clicks', 'daily_spend'], var_name='metric', value_name='value')
    # FOR EXARTA META
    filter_meta_exarta = filter_product_exarta[filter_product_exarta['platform'] == 'meta']
    meta_melted = filter_meta_exarta.melt(id_vars=['date'], value_vars=['views', 'clicks', 'daily_spend'], var_name='metric', value_name='value')
    # FOR EXARTA PPC
    filter_ppc_exarta = filter_product_exarta[filter_product_exarta['platform'] == 'ppc']
    ppc_melted = filter_ppc_exarta.melt(id_vars=['date'], value_vars=['views', 'clicks', 'daily_spend'], var_name='metric', value_name='value')
    # FOR EXARTA LINKEDIN
    filter_linkedin_exarta = filter_product_exarta[filter_product_exarta['platform'] == 'linkedin']
    linkedin_melted = filter_linkedin_exarta.melt(id_vars=['date'], value_vars=['views', 'clicks', 'daily_spend'], var_name='metric', value_name='value')
    # FOR EXARTA X
    filter_X_exarta = filter_product_exarta[filter_product_exarta['platform'] == 'x']
    x_melted = filter_X_exarta.melt(id_vars=['date'], value_vars=['views', 'clicks', 'daily_spend'], var_name='metric', value_name='value')
    # FOR EXARTA SHOPIFY
    filter_shopify_exarta = filter_product_exarta[filter_product_exarta['platform'] == 'shopify']
    shopify_melted = filter_shopify_exarta.melt(id_vars=['date'], value_vars=['views', 'clicks', 'daily_spend'], var_name='metric', value_name='value')
    
    return youtube_melted, meta_melted, ppc_melted, linkedin_melted, x_melted, shopify_melted


def plot_histograms_zeniva(product_name, platform_name, df):
    df = df[df['product'] == product_name]
    
    platform_metrics = {
        'youtube': ['clicks', 'views', 'daily_spend'],
        'meta': ['clicks', 'reach', 'daily_spend'],
        'shopify': ['clicks', 'daily_spend']
    }
    
    if platform_name in platform_metrics:
        selected_metrics = platform_metrics[platform_name]
    else:
        st.error(f"Platform {platform_name} not recognised.")
        return
    
    df_platform = df[df['platform'] == platform_name] 
    # df_grouped = df_platform[['date', 'clicks', 'views', 'daily_spend']].melt(id_vars='date', var_name='Metric', value_name='Value')
    df_grouped = df_platform[['date'] + selected_metrics].melt(id_vars='date', var_name='Metric', value_name='Value')
    
    color_discrete_map = {
        'clicks': 'red',
        'views': 'orange',
        'daily_spend': 'green',
        'reach': 'blue'
    }
 
    fig = px.histogram(
        df_grouped, 
        x='date', 
        y='Value', 
        color='Metric', 
        barmode='group', 
        title=f'{platform_name.capitalize()} Metrics',
        height=450,
        width=450,
        color_discrete_map=color_discrete_map,
        )
 
    # Display the figure in Streamlit
    st.plotly_chart(fig)