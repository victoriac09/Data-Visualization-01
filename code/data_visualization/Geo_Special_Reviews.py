
# %%
import pandas as pd
import pandas as pd # import the pandas library for data manipulation
import chart_studio.plotly as py # import plotly's chart studio for hosting and sharing plots online
import plotly.offline as po # import plotly's offline mode for displaying plots within a Jupyter notebook
import plotly.graph_objs as pg # import plotly's graph objects for creating complex visualizations
import matplotlib.pyplot as plt # import the matplotlib library for data visualization
import pandas as pd # import the pandas library for data manipulation (again)
import altair as alt # import the Altair library for creating interactive visualizations
import plotly.express as px # import Plotly's express module for creating simple visualizations quickly
import numpy as np # import numpy for numerical operations
from collections import Counter # import collections to count occurrences of items in a list
import math
import plotly.express as px



Business_special=pd.read_csv("../..data/clean_data/Business_special_4V.csv")


color_set = ['deepskyblue', 'darkorange','darkcyan', 'purple',"lime"]

#review_norm = (Business_special['review_count'] - Business_special['review_count'].min()) / (Business_special['review_count'].max() - Business_special['review_count'].min())

fig = px.scatter_mapbox(Business_special, lat="latitude", lon="longitude", hover_name="Special Category", hover_data=[ "stars","review_count","Business Status","City",'Number of Museum nearby ',
                                                                                                                    ' Number of Cinemas nearby',' Number of Beach nearby','Number of ShoppingMall nearby']
                    ,
                        zoom=8.5, height=300, color="Special Category", size_max=20,
                        center=dict(lat=27.964157, lon=-82.452606),
                         size="review_count", 
                        color_discrete_sequence=color_set)


fig.update_layout(mapbox_style="open-street-map")
fig.update_layout(title="<b>Distribution of Restaurants' by Count of Reviews & Special Category</b> ",title_font=dict(size=14))
fig.update_layout(width=600, height=500)
fig.update_layout(legend=dict(font=dict(size=10)))
fig.update_traces(hovertemplate="<b>Special Category:</b> %{hovertext}<br>" +
                                 "<b>Stars:</b> %{customdata[0]:.2f}<br>" +
                                 "<b>Review Count:</b> %{customdata[1]}<br>" +
                                 "<b>Business Status:</b> %{customdata[2]}<br>" +
                                 "<b>City:</b> %{customdata[3]}<br>"+
                                 "<b>Museums Nearby:</b> %{customdata[4]}<br>"+
                                 "<b>Cinemas Nearby:</b> %{customdata[5]}<br>"+
                                 "<b>Beaches Nearby:</b> %{customdata[6]}<br>"+
                                 "<b>Shopping Malls Nearby:</b> %{customdata[7]}<extra></extra>")

fig.write_html("../../website/img/Geo_Special_Reviews.html")



