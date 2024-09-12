# Load the data
import streamlit as st
import pandas as pd
import plotly.express as px

file_path = './data/cleaned_sample_random.xlsx'
data = pd.read_excel(file_path)
 
# Clean and restructure the data
data.columns = ['Platform', 'Metric', 'YouTube', 'Meta', 'PPC', 'Shopify']
data.dropna(inplace=True)  # Remove rows with NaN values
 
# Separate data for each platform
platform1_data = data.iloc[0:3, 2:6].reset_index(drop=True)
platform2_data = data.iloc[3:6, 2:6].reset_index(drop=True)
platform3_data = data.iloc[6:9, 2:6].reset_index(drop=True)
 
# Streamlit app
st.title("Social Media Platform Metrics")
 
# Function to plot metrics for each platform using Plotly
def plot_metrics(platform_data, platform_number):
    # Prepare the data for Plotly
    metrics = ['views', 'clicks', 'daily spend']
    social_media_platforms = ['YouTube', 'Meta', 'PPC', 'Shopify']
   
    # Create a new dataframe for plotting
    plot_data = []
    for i, metric in enumerate(metrics):
        for sm_platform in social_media_platforms:
            plot_data.append({
                'Metric': metric,
                'Social Media Platform': sm_platform,
                'Value': platform_data.iloc[i][sm_platform]
            })
   
    plot_df = pd.DataFrame(plot_data)
   
    # Create a bar plot using Plotly Express
    fig = px.bar(plot_df,
                 x='Metric',
                 y='Value',
                 color='Social Media Platform',
                 barmode='group',
                 title=f'Platform {platform_number} Metrics')
   
    return fig
 
# Create two rows, each row with two columns
col1, col2 = st.columns(2)
col3, col4 = st.columns(2)
 
# Display the plots in the respective columns
with col1:
    st.plotly_chart(plot_metrics(platform1_data, 1))
 
with col2:
    st.plotly_chart(plot_metrics(platform2_data, 2))
 
with col3:
    st.plotly_chart(plot_metrics(platform3_data, 3))
 
with col4:
    st.write("More visualizations can be added here")