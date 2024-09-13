import streamlit as st
import pandas as pd
import plotly.graph_objects as go

# Load data from CSV
df = pd.read_csv('unifies_metrics.csv')

# Define metrics for each platform
metrics = {
    'youtube': ['views', 'clicks', 'daily_spend'],
    'meta': ['reach', 'clicks', 'per_day_cost'],
    'PCC': ['impressions', 'clicks', 'daily_spend'],
    'shopify_ads': ['daily_installs', 'clicks', 'daily_spend']
}

# Create a list to hold data for plotting
plot_data = []

# Iterate over each product
for product in df['product'].unique():
    product_data = df[df['product'] == product]
    
    # Iterate over each platform and its metrics
    for platform, metric_list in metrics.items():
        platform_data = product_data[product_data['platform'] == platform]
        
        # Iterate over each metric for the current platform
        for metric in metric_list:
            if metric in platform_data.columns:
                # Create a trace for each metric
                trace = go.Bar(
                    x=platform_data['dates'],
                    y=platform_data[metric],
                    name=f'{product} - {platform} - {metric}'
                )
                plot_data.append(trace)

# Create the Plotly figure
fig = go.Figure(data=plot_data)

# Update the layout
fig.update_layout(
    title='Unified Histogram of Metrics by Product and Platform',
    xaxis_title='Date',
    yaxis_title='Value',
    barmode='group',  # Group bars together for each date
    xaxis_tickangle=-45  # Rotate x-axis labels for better readability
)

# Streamlit app
st.title('Unified Histogram of Metrics by Product and Platform')
st.plotly_chart(fig)
