
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



Business_region=pd.read_csv("../..data/clean_data/Business_region_4V.csv")
colors = ['darkviolet', 'orangered', 'deepskyblue', 'darkgreen']

# Normalize the values in the stars column to the range [0, 1]
stars_norm = (Business_region['stars'] - Business_region['stars'].min()) / (Business_region['stars'].max() - Business_region['stars'].min())

fig = px.scatter_mapbox(Business_region, lat="latitude", lon="longitude", hover_name="Region Category", hover_data=[ "stars","review_count","Business Status","City",'Number of Museum nearby ',
                                                                                                                    ' Number of Cinemas nearby',' Number of Beach nearby','Number of ShoppingMall nearby'],
                         zoom=11, height=100,width=100,color="Region Category",size_max=5,center=dict(lat=27.9489, lon=-82.45882),
                         size="stars", color_discrete_sequence=colors,opacity=stars_norm)
fig.update_layout(mapbox_style="open-street-map")
fig.update_layout(legend=dict(font=dict(size=10)))
fig.update_layout(title="<b>Distribution of Restaurants by Region Category in Most Representative Area</b>", title_font=dict(size=13))
fig.update_layout(width=600, height=500)
fig.update_traces(hovertemplate="<b>Region Category:</b> %{hovertext}<br>" +
                                 "<b>Stars:</b> %{customdata[0]:.2f}<br>" +
                                 "<b>Review Count:</b> %{customdata[1]}<br>" +
                                 "<b>Business Status:</b> %{customdata[2]}<br>" +
                                 "<b>City:</b> %{customdata[3]}<br>"+
                                 "<b>Museums Nearby:</b> %{customdata[4]}<br>"+
                                 "<b>Cinemas Nearby:</b> %{customdata[5]}<br>"+
                                 "<b>Beaches Nearby:</b> %{customdata[6]}<br>"+
                                 "<b>Shopping Malls Nearby:</b> %{customdata[7]}<extra></extra>")

# add the first annotation
#fig.add_annotation(text="This graph shows the most representative regions where restaurants are concentrated ",
                   #xref="paper", yref="paper",
                   #x=0, y=-0.08,
                   #showarrow=False, font=dict(family="Times New Roman", size=12, color="black"))

# add the second annotation
# fig.add_annotation(text="under the region classification criteria ",
#                    xref="paper", yref="paper",
#                    x=0, y=-0.12,
#                    showarrow=False, font=dict(family="Times New Roman", size=12, color="black"))

# # add the third annotation
# fig.add_annotation(text="",
#                    xref="paper", yref="paper",
#                    x=0, y=-0.16,
#                    showarrow=False, font=dict(family="Times New Roman", size=12, color="black"))

# fig.add_annotation(text="Click American circle in right size to see distribution of resturants in this category",
#                    xref="paper", yref="paper",
#                    x=0, y=-0.16,
#                    showarrow=False, font=dict(family="Times New Roman", size=12, color="black"))
fig.show()

fig.write_html("../../website/img/Geo_Region_Rating.html")



