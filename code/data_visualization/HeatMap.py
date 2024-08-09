

# %%
import pandas as pd
import altair as at
import plotly.graph_objects as go
import numpy as np
at.data_transformers.disable_max_rows()

df=pd.read_csv("../..data/clean_data/correlation_matrix.csv") ##### correlation_matrix.csv is the dataset of correlation matrix, you can refer to the data branch to find it.




# Define the colorscale for the heatmap
colors = [[0, 'pink'], [0.25, 'purple'], [0.5, 'lightgreen'], [0.75, 'orange'], [1, 'lightblue']]

# Create a heatmap using the correlation matrix dataset
fig = go.Figure(data=go.Heatmap(
        z=df["correlation"], # Set the correlation values as the heatmap's z-axis
        x=df["column_x"], # Set the first variable names as the heatmap's x-axis
        y=df["column_y"], # Set the second variable names as the heatmap's y-axis
        colorscale=colors, # Use the defined colorscale for the heatmap
    ))

# Customize the layout of the heatmap
fig.update_layout(
    title={
        'text': "Heatmap of  Restaurants' Variables by Region Category",
        'font': {'size': 22},
    },
    height=600,
    width=800,
    xaxis={
        'title_font': {'size': 18},
        'tickfont': {'size': 14},
        'tickangle': 45, # Set the angle of the x-axis labels to -45 degrees
    },
    yaxis={
        'title_font': {'size': 18},
        'tickfont': {'size': 14},
        'tickangle': 0, # Set the angle of the y-axis labels to 0 degrees
    }
)




# Customize the tooltip format
fig.update_traces(hovertemplate='Variable1: %{x}<br>Variable2: %{y}<br>Correlation Value: %{z}<extra></extra>')

# Show the heatmap
fig.show()

# Save the heatmap as an HTML file
fig.write_html("../..website/img/heatMap.html")
