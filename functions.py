import pandas as pd

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