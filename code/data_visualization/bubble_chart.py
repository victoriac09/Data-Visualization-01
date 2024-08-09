import plotly.graph_objects as go
import plotly.express as px
import pandas as pd
import math
import plotly.express as px

# load the dataset into a Pandas DataFrame
region_category =pd.read_csv("../..data/clean_data/Business_Region_Category.csv")

# add new columns to the DataFrame
region_category['Compliment Ratio'] = round(region_category['compliment_count'] / region_category['review_count'],4)
region_category['Stars'] = region_category['stars'] 
region_category['Name'] = region_category['name'] 
region_category['Review Count'] = region_category['review_count'] 

# select only rows where Compliment Ratio is not 0
region_category1 = region_category[region_category['Compliment Ratio'] != 0]

# create a scatter plot using Plotly Express
fig = px.scatter(region_category1, y="Stars", x="Review Count",
          size="Compliment Ratio", color="Region Category",
                 hover_name="Name", log_x=True, size_max=60,color_discrete_sequence=px.colors.qualitative.Dark2,
                 category_orders={"Region Category": ["American", "Asian", "European", "Latin American"]})

# update the layout of the plot
fig.update_layout(
    xaxis=dict(
        title='Number of Reviews',
        gridcolor='white',
        type='log',
        gridwidth=3,
    ),
    yaxis=dict(
        title='Rating stars',
        gridcolor='white',
        gridwidth=3,
        dtick = 1
    ),
    paper_bgcolor='rgb(255,250,250)',
    plot_bgcolor='rgb(250,240,230)',
    title=dict(text="<b>Bubble Chart of Restaurant Ratings and Reviews by Region Category in Florida</b>", font=dict(size=20)),
    legend=dict(
        title="Region Category",
        traceorder="normal",
        bgcolor='rgba(255,255,255,0)',
        bordercolor='rgba(255,255,255,0)'
    ),
)

# update the traces of the plot
fig.update_traces(marker=dict(line=dict(width=2)))

# show the plot and save it as an HTML file
fig.show()
fig.write_html("bubble_chart.html")
