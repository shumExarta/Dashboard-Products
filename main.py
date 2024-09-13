import streamlit as st
import pandas as pd
import plotly.express as px
# import matplotlib.pyplot as plt
import time
import random
from functions import get_platform_data, render_custom_metric, get_comparison_stats, render_follower_metric, render_follower_metric_for_odd, render_centered_heading
st.set_page_config(layout='wide')

youtube_data, meta_data, ppc_data = get_platform_data()
data = pd.read_csv('./data/cleaned_sample_random.csv')

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
    
    return fig

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
    # Read the data once
    df = pd.read_csv("./data/zeniva_social.csv")
    
    st.title("Zeniva stats accross all platforms")

    # Define platform names and headers
    platforms = {
        "youtube": "YouTube",
        "meta": "Meta",
        "linkedin": "LinkedIn",
        "PCC": "PPC",
        "shopify_ads": "Shopify Ads",
        "x": "X"
    }

    placeholder = st.empty()
    with placeholder.container():
        cols = st.columns(len(platforms))

        # Loop through platforms and columns
        for idx, (platform, header) in enumerate(platforms.items()):
            with cols[idx]:
                st.header(header)

                # Filter data for the current platform
                metrics = {
                    "Total Followers": df[df["platform"] == platform]["total_followers"].sum(),
                    "Today's Followers": df[df["platform"] == platform]["today_followers"].sum(),
                    "Yesterdays Followers": df[df["platform"] == platform]["yesterday_follwers"].sum()
                }

                # Render metrics
                for label, value in metrics.items():
                    render_follower_metric(label, value)

    time.sleep(60)
    placeholder.empty()
    
    # Metrics available in the dataset
    metrics = data['Metric'].unique()

    # Create columns in the Streamlit app
    col1, col2 = st.columns(2)
    col3, col4 = st.columns(2)

    # Display the plots in the respective columns
    with col1:
        st.plotly_chart(plot_platform_metrics('YouTube'))  # Plot metrics for YouTube

    with col2:
        st.plotly_chart(plot_platform_metrics('Meta'))  # Plot metrics for Meta

    with col3:
        st.plotly_chart(plot_platform_metrics('PPC'))  # Plot metrics for PPC

    with col4:
        st.plotly_chart(plot_platform_metrics('Shopify'))  # Plot metrics for Shopify Ads
    placeholder.empty()
        
if ody_btn:

    placeholder = st.empty()
    st.title("Odyssey Stats Across All Platforms")

    # Load the data once
    df = pd.read_csv("./data/odd_social.csv")

    # Define the platforms
    platforms = ["youtube", "meta", "PPC", "shopify_ads", "x"]

    # Create columns
    col1, col2, col3 = st.columns(3)
    col4, col5, col6 = st.columns(3)

    columns = [col1, col2, col3, col4, col5, col6]

    for i, platform in enumerate(platforms):
        with columns[i]:
            st.header(platform.capitalize())
            
            # Filter data for the current platform
            platform_data = df[df["platform"] == platform]
            
            # Calculate metrics
            total_followers = platform_data["total_followers"].sum()
            today_followers = platform_data["today_followers"].sum()
            yesterday_followers = platform_data["yesterday_follwers"].sum()
            
            # Render metrics
            followers_metrics = {
                "Total Followers": total_followers,
                "Today's Followers": today_followers,
                "Yesterday's Followers": yesterday_followers
            }

            for label, value in followers_metrics.items():
                render_follower_metric_for_odd(label, value)

        # Placeholder for the last column if needed
        with col6:
            pass
   
    placeholder = st.empty()

if exa_btn:
    df = pd.read_csv("./data/exarta_social.csv")
    st.title("Zeniva stats accross all platforms")

    # Define platform names and headers
    platforms = {
        "youtube": "YouTube",
        "meta": "Meta",
        "linkedin": "LinkedIn",
        "PCC": "PPC",
        "shopify_ads": "Shopify Ads",
        "x": "X"
    }

    placeholder = st.empty()
    with placeholder.container():
        cols = st.columns(len(platforms))

        # Loop through platforms and columns
        for idx, (platform, header) in enumerate(platforms.items()):
            with cols[idx]:
                st.header(header)

                # Filter data for the current platform
                metrics = {
                    "Total Followers": df[df["platform"] == platform]["total_followers"].sum(),
                    "Today's Followers": df[df["platform"] == platform]["today_followers"].sum(),
                    "Yesterdays Followers": df[df["platform"] == platform]["yesterday_follwers"].sum()
                }

                # Render metrics
                for label, value in metrics.items():
                    render_follower_metric(label, value)

    time.sleep(60)
    placeholder.empty()
    
    # Metrics available in the dataset
    metrics = data['Metric'].unique()

    # Create columns in the Streamlit app
    col1, col2 = st.columns(2)
    col3, col4 = st.columns(2)

    # Display the plots in the respective columns
    with col1:
        st.plotly_chart(plot_platform_metrics('YouTube'))  # Plot metrics for YouTube

    with col2:
        st.plotly_chart(plot_platform_metrics('Meta'))  # Plot metrics for Meta

    with col3:
        st.plotly_chart(plot_platform_metrics('PPC'))  # Plot metrics for PPC

    with col4:
        st.plotly_chart(plot_platform_metrics('Shopify'))  # Plot metrics for Shopify Ads
    placeholder.empty()
        

   
    # st.title("Exarta stats accross all platforms")
    # col11, col12, col6 = st.columns(3)
    # col13, col14 , col7= st.columns(3)
    
    
    # with col11:
    #     st.header("Youtube")
    #     df = pd.read_csv("./data/zeniva_social.csv")
    #     total_followers_youtube2 = df[df["platform"] == "youtube"]["total_followers"].sum()
    #     today_followers_youtube2 = df[df["platform"] == "youtube"]["today_followers"].sum()
    #     yesterday_followers_youtube2 = df[df["platform"] == "youtube"]["yesterday_follwers"].sum()
        
        
    #     st.write(f"Total follwers : {total_followers_youtube2}")
    #     st.write(f"Today follwers : {today_followers_youtube2}")
    #     st.write(f"Yesterday follwers : {yesterday_followers_youtube2}")
        
    # with col12:
    #     st.header("Meta")
    #     df = pd.read_csv("./data/zeniva_social.csv")
    #     total_followers_meta2 = df[df["platform"] == "meta"]["total_followers"].sum()
    #     today_followers_meta2 = df[df["platform"] == "meta"]["today_followers"].sum()
    #     yesterday_followers_meta2 = df[df["platform"] == "youtube"]["yesterday_follwers"].sum()
        
    #     st.write(f"Total follwers : {total_followers_meta2}")
    #     st.write(f"Today follwers : {today_followers_meta2}")
    #     st.write(f"Yesterday follwers : {yesterday_followers_meta2}")
        
        

    # with col6:
    #     st.header("X")
    #     df = pd.read_csv("./data/zeniva_social.csv")
    #     total_followers_x2 = df[df["platform"] == "meta"]["total_followers"].sum()
    #     today_followers_x2 = df[df["platform"] == "meta"]["today_followers"].sum()
    #     yesterday_followers_x2 = df[df["platform"] == "youtube"]["yesterday_follwers"].sum()
        
    #     st.write(f"Total followers : {total_followers_x2}")
    #     st.write(f"Today followers : {today_followers_x2}")
    #     st.write(f"Yesterday follwers : {yesterday_followers_x2}")    
        
    # with col13:
    #     st.header("PPC")
    #     df = pd.read_csv("./data/zeniva_social.csv")
    #     total_followers_ppc2 = df[df["platform"] == "meta"]["total_followers"].sum()
    #     today_followers_ppc2 = df[df["platform"] == "meta"]["today_followers"].sum()
    #     yesterday_followers_ppc2 = df[df["platform"] == "youtube"]["yesterday_follwers"].sum()
       
    #     st.write(f"Total follwers : {total_followers_ppc2}")
    #     st.write(f"Today follwers : {today_followers_ppc2}")
    #     st.write(f"Yesterday follwers : {yesterday_followers_ppc2}")
        
    # with col14:
    #     st.header("Shopify Ads")
    #     df = pd.read_csv("./data/zeniva_social.csv")
    #     total_followers_shop2 = df[df["platform"] == "meta"]["total_followers"].sum()
    #     today_followers_shop2 = df[df["platform"] == "meta"]["today_followers"].sum()
    #     yesterday_followers_shop2 = df[df["platform"] == "youtube"]["yesterday_follwers"].sum()
      
        
    #     st.write(f"Total follwers : {total_followers_shop2}")
    #     st.write(f"Today follwers : {today_followers_shop2}")
    #     st.write(f"Today follwers : {yesterday_followers_shop2}")
        
    # with col7:
    #     st.header("LinkedIn")
    #     df = pd.read_csv("./data/zeniva_social.csv")
    #     total_followers_link2 = df[df["platform"] == "meta"]["total_followers"].sum()
    #     today_followers_link2 = df[df["platform"] == "meta"]["today_followers"].sum()
    #     yesterday_followers_link2 = df[df["platform"] == "youtube"]["yesterday_follwers"].sum()
      
        
    #     st.write(f"Total followers : {total_followers_link2}")
    #     st.write(f"Today followers : {today_followers_link2}")
    #     st.write(f"Yesterday followers : {yesterday_followers_link2}")
    # placeholder = st.empty()    

# if comp_btn:

#     placeholder = st.empty()
#     st.title("Overall stats")
#     comparison_df = pd.read_csv("./data/comparisons.csv")
#     zeniva_stats, ody_stats = get_comparison_stats(comparison_df)
#     zen_col, ody_col = st.columns(2)
#     with zen_col:
#         st.metric("New Installs", zeniva_stats['new_installs'])
#         st.metric("Total Installs", zeniva_stats['total_installs'])
#         st.metric("Free Users", zeniva_stats['free_users'])
#         st.metric("Paid Users", zeniva_stats['paid_users'])
#         st.metric("Today Uninstalls", zeniva_stats['today_uninstalls'])
#         st.metric("Total Uninstalls", zeniva_stats['total_uninstalls'])
#     with ody_col:
#         st.metric("New Installs", ody_stats['new_installs'])
#         st.metric("Total Installs", ody_stats['total_installs'])
#         st.metric("Free Users", ody_stats['free_users'])
#         st.metric("Paid Users", ody_stats['paid_users'])
#         st.metric("Today Uninstalls", ody_stats['today_uninstalls'])
#         st.metric("Total Uninstalls", ody_stats['total_uninstalls'])





if comp_btn:
    placeholder = st.empty()
    st.title("Overall Stats")

    # Load the data
    comparison_df = pd.read_csv("./data/comparisons.csv")
    zeniva_stats, ody_stats = get_comparison_stats(comparison_df)

    # Create columns for side-by-side layout
    col1, col2 = st.columns(2)

    with col1:
        render_centered_heading("Zeniva Stats")
        metrics = ["New Installs", "Total Installs", "Free Users", "Paid Users", "Today Uninstalls", "Total Uninstalls"]
        for metric in metrics:
            render_custom_metric(metric, zeniva_stats[metric.lower().replace(" ", "_")], "Zeniva")

    with col2:
        render_centered_heading("Odassay Stats")
        for metric in metrics:
            render_custom_metric(metric, ody_stats[metric.lower().replace(" ", "_")], "Odassay")





























    st.title("Comparison - line chart")

    df_populated = pd.read_csv('./data/populated_product_data_for_lc.csv')

    df_melted = df_populated.melt(id_vars=['Date', 'Product'], 
                                value_vars=['new_installs', 'total_installs', 'free_users', 'paid_users', 'today_uninstalls', 'total_uninstalls'],
                                var_name='Metric', value_name='Value')

    fig = px.line(df_melted, x='Date', y='Value', color='Product', 
                line_group='Metric', markers=True,
                facet_col='Metric', facet_col_wrap=2,
                labels={"Date": "Date", "Value": "Metric Value"},
                title='Comparison of Zeniva and Odassay across multiple metrics')

    st.plotly_chart(fig)
    
    # st.title("Comparison - Piechart")
    # # Pie chart: comparing total installs between Zeniva and Odassay
    # total_installs_data = df_populated.groupby('Product')['total_installs'].sum().reset_index()

    # pie_fig = px.pie(total_installs_data, values='total_installs', names='Product',
    #              title='Total Installs Comparison between Zeniva and Odassay')
    # st.plotly_chart(pie_fig)
    # st.title("Comparison - Histogram")
    # hist_fig = px.histogram(df_populated, x='new_installs', color='Product', 
    #                     nbins=20, title='Distribution of New Installs for Zeniva and Odassay')

    # # Display both charts in Streamlit
    
    # st.plotly_chart(hist_fig)

# odd -
# zin - purple

    

















 
# # Load the data
# file_path = 'cleaned_sample_random.xlsx'
# data = pd.read_excel(file_path)
 
# # Clean and restructure the data
# data.columns = ['Platform', 'Metric', 'YouTube', 'Meta', 'PPC', 'Shopify']
# data.dropna(inplace=True)  # Remove rows with NaN values
 
# # Separate data for each platform
# platform1_data = data.iloc[0:3, 2:6].reset_index(drop=True)
# platform2_data = data.iloc[3:6, 2:6].reset_index(drop=True)
# platform3_data = data.iloc[6:9, 2:6].reset_index(drop=True)
 
# # Streamlit app
# st.title("Social Media Platform Metrics")
 
# # Function to plot metrics for each platform using Plotly
# def plot_metrics(platform_data, platform_number):
#     # Prepare the data for Plotly
#     metrics = ['views', 'clicks', 'daily spend']
#     social_media_platforms = ['YouTube', 'Meta', 'PPC', 'Shopify']
   
#     # Create a new dataframe for plotting
#     plot_data = []
#     for i, metric in enumerate(metrics):
#         for sm_platform in social_media_platforms:
#             plot_data.append({
#                 'Metric': metric,
#                 'Social Media Platform': sm_platform,
#                 'Value': platform_data.iloc[i][sm_platform]
#             })
   
#     plot_df = pd.DataFrame(plot_data)
   
#     # Create a bar plot using Plotly Express
#     fig = px.bar(plot_df,
#                  x='Metric',
#                  y='Value',
#                  color='Social Media Platform',
#                  barmode='group',
#                  title=f'Platform {platform_number} Metrics')
   
#     return fig
 
# # Create two rows, each row with two columns
# col1, col2 = st.columns(2)
# col3, col4 = st.columns(2)
 
# # Display the plots in the respective columns
# with col1:
#     st.plotly_chart(plot_metrics(platform1_data, 1))
 
# with col2:
#     st.plotly_chart(plot_metrics(platform2_data, 2))
 
# with col3:
#     st.plotly_chart(plot_metrics(platform3_data, 3))
 
# with col4:
#     st.write("More visualizations can be added here")