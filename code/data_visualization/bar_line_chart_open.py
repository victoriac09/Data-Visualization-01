import pandas as pd
import altair as alt

# In this plot, we use both R and Python. But we saved the data so it can run directly
# df = pd.read_json("../..data/yelp_photos/photos.json",lines = True, chunksize=100000)
# df1 = pd.DataFrame()
# for chunk in df:
    # df1 = pd.concat([df1, chunk])
# fig1 = pd.read_csv("../..data/fig1.csv")
# fig_df = pd.merge(fig1, df1, on=['business_id'])
# fig_df.to_csv('topfig.csv')

# read in the cleaned data for open restaurants
r1sum2 = pd.read_csv("../..data/clean_data/Reviews_Rating_Region_Open.csv")

# read in the data for the top photos
fig11 = pd.read_csv("../..data/clean_data/topfig2.csv")

# create a new DataFrame to store the image data
df1 = pd.DataFrame()

# define a function to format the image data as a base64 string
def image_formatter2(im):
    with BytesIO() as buffer:
        im.save(buffer, 'png')
        data = base64.encodebytes(buffer.getvalue()).decode('utf-8')
    
    return f"data:image/png;base64,{data}"

# iterate through each row of the top photos DataFrame to add image data to the new DataFrame
for i in range(70):
    temp = fig11["photo_id"][i]
    # As the file is very huge, zip file with 6G, we can not upload it to Github, link is  https://www.yelp.com/dataset
    path = "../..data/yelp_photos/photos/"+temp+".jpg"
    im = PIL.Image.open(path) 
    im = im.resize((150, 150))
    imglink = image_formatter2(im)
    df_img = pd.DataFrame.from_records([{'image': imglink}])
    df1 = df1.append(df_img)

# reset the index of the new DataFrame
df1.reset_index(inplace=True, drop=True)

# concatenate the top photos DataFrame with the new DataFrame containing image data
df3 = pd.concat([fig11, df1], axis=1)

# create new columns with cleaned column names
df3["Region Category"] = df3["Region.Category"]
df3["Restaurant Name"] = df3["name"]
df3["Reviews Count"] = df3['n']

# filter the DataFrame to include only data up to 2021
df4 = df3[df3['Year'] < 2022]

# create a bar chart of the number of reviews by year and region category
bar = alt.Chart(df4).mark_bar(
    cornerRadiusTopLeft=5,
    cornerRadiusTopRight=5,
    size = 20
).encode(
    x=alt.X('Year:Q', axis=alt.Axis(format='.0f')),
    y=alt.Y('sum(n)', title='The Number of Reviews'),
    color='Region Category',
    opacity=alt.value(0.8),
    tooltip=['Restaurant Name','Reviews Count','image'] # add tooltips for the restaurant name, review count, and image
)

# create a line chart of the rating by year and region category
line = alt.Chart(r1sum2).mark_line(point=True).encode(
    x='Year',
    y = alt.Y('Rating:Q', scale = alt.Scale(domain=(3.0, 5.0))),
    color=alt.Color('Region Category:N', scale= alt.Scale(scheme='dark2'))
).properties(
    title={
        "text": "An Innovative View: Changes in Reviews and Ratings for Open Restaurants in Florida",
        "fontWeight": "bold",
        "fontSize": 20
    })

# combine the bar and line charts into a single chart
linkchart3=(bar+line).resolve_scale(y='independent').properties(width=600)

# save the chart as an HTML file
linkchart3.save('bar_line_chart2.html')