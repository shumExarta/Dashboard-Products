import pandas as pd
import plotly.express as px

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


# Function to plot metrics for each platform using Plotly
def plot_platform_metrics(platform_name):
    # Extract relevant data for the given platform
    plot_data = data[['Metric', platform_name]].copy()
    
    # Rename the columns for ease of use
    plot_data.columns = ['Metric', 'Value']
    
    # Create a bar plot using Plotly Express
    fig = px.bar(plot_data,
                 x='Metric',
                 y='Value',
                 title=f'{platform_name} Metrics',
                 labels={'Value': 'Metric Value', 'Metric': 'Metric Type'})
    
    return figg