import pandas as pd

# read in data
r1sum1 = pd.read_csv("../..data/clean_data/Reviews_Rating_Region_Close.csv")

# import altair library
import altair as alt

# create bar chart
bar = alt.Chart(r1sum1).mark_bar(
    cornerRadiusTopLeft=5,
    cornerRadiusTopRight=5,
    size = 20
).encode(
    x=alt.X('Year:Q', axis=alt.Axis(format='.0f')),
    y=alt.Y('sum(n)', title='The Number of Reviews'),
    color=alt.Color('Region Category:N', scale= alt.Scale(scheme='dark2')),
    opacity=alt.value(0.8)
)

# create line chart
line = alt.Chart(r1sum1).mark_line(point=True).encode(
    x='Year',
    y = alt.Y('Rating:Q', scale = alt.Scale(domain=(3.0, 5.0))),
    color=alt.Color('Region Category:N', scale= alt.Scale(scheme='dark2'))
).properties(
    title={
        "text": "Changes in Reviews and Ratings for Closed Restaurants in Florida",
        "fontWeight": "bold",
        "fontSize": 20
    }
)

# set the x-axis domain for both charts
bar.encoding.x.scale.domain = [2005, 2021]
line.encoding.x.scale.domain = [2005, 2021]

# combine the two charts and set y-axis scales to be independent
linkchart2 = (bar+line).resolve_scale(y='independent').properties(width=600)

# save chart as an html file
linkchart2.save('bar_line_chart1.html')
