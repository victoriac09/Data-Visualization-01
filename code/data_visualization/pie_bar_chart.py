# Import libraries
import pandas as pd
import altair as alt

# Set altair default data type to enable large data sets
alt.data_transformers.enable('default',max_rows=None)

# Read in cleaned Yelp business data for analysis
business1 = pd.read_csv("../..data/clean_data/business.csv")
business_top = pd.read_csv("../..data/clean_data/business_top.csv")

# Define a selection for the bar chart to link to the pie chart
selection = alt.selection_single(fields=['State'],name='Random')

# Define the color encoding for the bar chart based on the selection
color1 = alt.condition(selection,
                      alt.Color("State:N",scale = alt.Scale(scheme="category20")),
                      alt.value('lightgray'))

# Define a selection for the pie chart to link to the bar chart
selection2 = alt.selection_single(fields=['State',"City"],name='Random')

# Define the color encoding for the pie chart based on the selection
color2 = alt.condition(selection2,
                      alt.Color("City:N",scale = alt.Scale(scheme="paired")),alt.value('lightgray'))

# Define the bar chart with the number of restaurants sorted by state
bar=(alt.Chart(business1)
 .mark_bar()
 .encode(alt.X('State:N',sort=alt.EncodingSortField(field="business_id", op="count", order='descending')),
  alt.Y('count(business_id)', axis=alt.Axis(grid=False)), 
  color = color1)
).add_selection(selection)  # Add the selection defined earlier to the chart

# Add titles and axis labels for the bar chart
bar.title ="Number of Yelp Restaurants Sorted by State in the U.S."
bar.encoding.x.title = 'State'
bar.encoding.y.title = 'Number of Restaurants'

# Define the pie chart showing the top 10 cities with the most restaurants in each state
pie = (alt.Chart(business_top)
       .mark_arc(innerRadius=50)
       .encode(theta="n",
               color=color2)
      ).transform_filter(selection)  # Filter the data based on the selection defined earlier

# Add titles for the pie chart
pie.title="Top 10 Cities with the Most Restaurants in Each State on Yelp (U.S.)"

# Concatenate the bar chart and pie chart horizontally, linking them by color
linked1 = alt.hconcat(
    bar, pie
).resolve_scale(
    color='independent'  # Set color to be independent between the two charts
).configure_view(
    stroke=None  # Remove borders from the concatenated chart
)

# Save the concatenated chart as an HTML file
linked1.save('bar_pie_chart.html')
