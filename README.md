# ANLY 503 Project Repo

This is the team repository you will be use for your 503 project. All your team's work will happen here. 

Links of interest:
* The project requirements are in the [`instructions.md`](instructions.md) document
* The repository structure is described in the [reposity structure section](#repository-structure) below
* You **will** make changes to this `README.md` file within your repository. These changes are descripned in the [instructions section](#instructions-for-modifying-this-readmemd-file) below.

## Repository structure

You will work within an **organized** repository and apply coding and development best practices. The repository has the following structure:

```.
├── README.md
├── code/
├── data/
├── img/
└── website/
```

* The `code/` directory is where you will develop all your code.  You may add additional sub-directories as needed to modularize your development.

* The `data/` directory should contain your data files and should have multiple sub-directories (i.e. raw, processed, analytical, etc.) as needed.

* The `img/` directory should contain any external images that you need for your site. However, all your viz's should be generated programmatically in your source code.

* The `website/` directory where the website will be deployed. It must be self-contained and accessible via an index.html within this sub-directory.  Any website asset (images, html, css, JavaScript source code) must be added to this directory. 

There is an empty placeholder file in each subdirectory called `placeholder-to-be-deleted.txt`. This file may be deleted **after** you save other files in those subdirectories. This file is needed to be able to keep the empty directory in the repo.

Other files we expect to see at the top level of this repo may include:
- `.gitignore`


## Elements that impact the distributions of restaurants in Florida on different dimensions

### Team section: Group 33: Zijing Cheng (zc233) & Nianqing Chen (nc807) & Zixuan Li (zl483)

### Summary section: 

The internet cyber-star economy has become a significant factor in the restaurant industry, and this research project aims to investigate the correlation between the two in Florida. The study utilizes the Yelp dataset to gain insights into people's preferences, dietary habits, and factors that contribute to positive dining experiences. By analyzing this information, the research aims to provide valuable insights into the link between restaurant operations and customer feedback, which can inform strategies for improving restaurant performance and customer satisfaction.

The research project examines the relationship between a restaurant's location and customer reviews and ratings on Yelp, with a focus on four types of popular locations in Florida - movie theaters, beaches, malls, and museums. These locations are places where people may need to find a nearby restaurant quickly and easily, either because of time constraints or convenience. By examining the relationship between restaurant locations and these destinations, the study can gain insights into customer behavior and preferences, which can inform restaurant operations and marketing strategies.

The study also analyzed changes in ratings and reviews from Yelp reviews between 2005 to 2021 to determine if closures of different types of restaurants could be inferred. American restaurants accounted for almost one-third of all restaurants in Florida but had the lowest average rating since 2009. In contrast, Asian restaurants had the highest average rating since 2017. The review volume for European and Latin American restaurants was high despite their fewer numbers. COVID-19 had a significant impact on closures, but changes in people's preferences also played a role.

Examining the correlations among nine variables such as Business Status, Rating Scores, and nearby locations can provide valuable insights into the success of a restaurant and consumer behavior. This analysis can benefit restaurant owners, marketers, and consumers by helping them make more informed decisions and optimize their dining experiences.

The relationship between comment volume and ratings shows that a high volume of reviews and a high rating usually indicate a good restaurant. However, if a restaurant has a high rating but few reviews, it may indicate fake reviews. The compliment ratio can help identify fake reviews. American and European restaurants are generally of high quality and popularity in Florida, while Asian restaurants may need to improve their quality. Overall, as the number of reviews increases, the restaurant's rating tends to improve.

The focus on geographic location is essential for providing people with diverse, high-quality, and cost-effective food and entertainment options that suit their preferences and save their time and money. Through interactive visualization, the density and distribution of different types of restaurants in the region can be analyzed, and valuable insights can be gained into the relationship between location and restaurant type. American restaurants seem to have a clear advantage in both quantity and rating when compared to other types of restaurants in the region, while Seafood restaurants stand out as the most frequently found type based on food characteristics. Food trucks may not have the highest quantity compared to other restaurant types, but they are the most consistently distributed throughout the region. The consistent distribution of Food trucks suggests that they may offer a more specialized and niche cuisine that attracts a loyal following.

Understanding the relationship between rating score and review count is important when choosing a restaurant. While a high rating score indicates positive experiences, review count shows popularity. A restaurant can have a high rating score but a low review count, indicating newness or location, whereas a restaurant with a lower rating score but a high review count could be a local favorite. By analyzing the distribution of different types of restaurants based on location, review count, and dining mode, we can gain insights into the local restaurant scene.

For example, American restaurants are the most popular in the region, and seafood restaurants have a widespread distribution. Salad restaurants are mainly concentrated in the Saint Petersburg area, indicating preferences for healthier food options. The map also reveals the importance of formal dining experiences and diverse dining options. Overall, these data-driven insights can guide us to the dining

### Data Description section: 
#### Data pre-processing
* We obtained four datasets from the Yelp website: https://www.yelp.com/dataset/download.
* We performed data preprocessing on the Business dataset by removing all rows and columns containing missing values because the sample size was large.
* We applied a subset to the entire dataset and filtered it to include only rows where the "categories" column contains "Restaurants".
* We also dropped the "attributes" and "hours" columns from the DataFrame as we did not need to analyze these variables.
* For the Tips dataset, we organized and cleaned the data.
* We integrated the Tips dataset with the subsetted Business dataset based on the "business_id" column.Finally, we obtained a clean and tidy Business & Tip dataset.
* Afterwards, we corrected the City column in the integrated dataset by rectifying cities that were ambiguous or had potential comprehension risks. This was done to ensure a more intuitive and accurate understanding of the dataset.

#### Data Summary

We conducted a summary analysis of the Business & Tip dataset, which yielded the number, mean, and standard deviation of four attributes.

#### Data merged by Category

After a thorough investigation of the Category attribute in the Business & Tip dataset, we found that the types of restaurants were diverse and complicated, which could hinder our future analysis. Therefore, we chose to classify all restaurants based on three criteria: regional, specialty cuisine, and dining format. The categories included in each classification criteria are as follows:

* Region Category：American， Asian，European，Latin American
* Special Category：Gluten-Free，Salad，Seafood，Vegan，Vegetarian
* Format Category：Bars，Desserts，Events，Food Delivery, Food Stores, Food Trucks, Juice Bars.

Three new columns were added to the dataset: Region Category, Special Category, and Format Category.
A subset analysis was conducted on the dataset to obtain three separate datasets: Business_region, Business_special, and Business_format.
Each of these datasets contained unique restaurants, with no duplicates between them

#### Prepare for visualiztaion data(Bar & line chat)

* Select the top ten cities with the highest number of restaurants in each state for map visualization.
* Filter the dataset to only include data from Florida.
* Perform three classification methods on the dataset: region, format, and special. For each method:
    a. Reclassify the business dataset based on the chosen classification structure.
    b. Remove restaurants that belong to multiple categories.
* Using the region-based classification method:
    a. Summarize the annual reviews based on the region, obtaining the total number of reviews and average ratings for different regions each year.
    b. Identify the top 15 rated restaurants for each region every year as recommended dining options.
    c. Retrieve images of corresponding restaurants from the photo dataset for visualization purposes.

#### Prepare Visualizing Dataset (Map plot)

* We collected 20 geographical locations for 4 representative places: movie theaters, shopping malls, beaches, and museums, in order to gain a deeper understanding of the convenience of restaurants' surroundings and the availability of comprehensive entertainment options.

* We defined equations to calculate the location of each restaurant in relation to these representative places.By setting a threshold, a place was considered to be near a restaurant if the distance was less than the threshold.

* We obtained the number of movie theaters, shopping malls, beaches, and museums near each restaurant as columns.These columns were then merged into three Business datasets: Business_region, Business_special, and Business_format.

* To investigate the relationship between Location and Rating Score as well as Location and Review Count, we adjusted some column names in the three merged Business datasets. This allowed us to create six visual analysis charts to examine the relationships.









### Description: 
#### Code
we divided code part into data_cleaning, data_analysis, eda and data_visualization.
* data_cleaning

clean_merge.ipynb contains how to clean the raw data from Ylep.

data_clean_R.Rmd contains how to prepare the data for visualization, including photos and reviews dataset.

* eda

initial_eda.ipynb contains initial data exploration of the Yelp dataset to provide a overview of the yelp data, and it is the 

start of this project.

* data_analysis

distribution_analysis.ipynb contains analysis of location and reviews, location and ratings

radom_forest_model.Rmd contains random forest modling of business status of the region category dataset.

* data_visualization

Geo_Format_Rating.py contains code to plot Distribution of Restaurants By Format Category in Most Representative Area.

Geo_Format_Reviews.py contains code to plot Distribution of Restaurants' by Count of Reviews & Format Category.

Geo_Region_Rating.py contains code to plot Distribution of Restaurants by Region Category in Most Representative Area.

Geo_Region_Reviews.py contains code to plot Distribution of Restaurants by Count of Reviews & Region Category.

Geo_Special_Rating.py contains code to plot Distribution of Restaurants By Special Category in Most Representative Area.

Geo_Special_Reviews.py contains code to plot Distribution of Restaurants' by Count of Reviews & Special Category.

HeatMap.py contains code to plot Heatmap of  Restaurants' Variables by Region Category.

bar_line_chart_closed.py contains code  to plot Changes in Reviews and Ratings for Closed Restaurants in Florida.

bar_line_chart_open.py  contains code  to plot An Innovative View: Changes in Reviews and Ratings for Open Restaurants in Florida.

bubble_chart.py contains code to plot Bubble Chart of Restaurant Ratings and Reviews by Region Category in Florida.

pie_bar_chart.py contains code to plot Top 10 Cities with the Most Restaurants in Each State on Yelp (U.S.).

#### data 

* raw_data

As the json file is too big to upload, we put the file link here.

You can download the dataset in this website: https://www.yelp.com/dataset/download

The Yelp dataset (https://www.yelp.com/dataset/documentation/main) is a rich and extensive collection of data provided by Yelp, a popular online platform for discovering and reviewing local businesses. The dataset contains information about businesses, users, reviews, tips, and check-ins from Yelp's platform. Specifically, it includes:

Business Data: Basic information about local businesses such as name, address, city, state, postal code, latitude, longitude, stars, review count, and categories.

Review Data: Detailed reviews of businesses, consisting of user_id, business_id, stars, date, text, useful, funny, and cool.

Tip Data: Short tips provided by users for businesses, containing user_id, business_id, text, date, and compliment_count.

Photo Data: Restaurants' Photos 

* clean_data

Business_format_4v.csv, Business_region_4v.csv, Business_special_4v.csv contain locations, ratings, the number of reviews and the number of four nearby facilities for three classification methods.

Business_Format_Category.csv, Business_Region_Category.csv, Business_Special_Category.csv contain locations, ratings, the number of reviews for three classification methods.

Business_Format_Category.csv, Business_Region_Category.csv, Business_Special_Category.csv contain locations, ratings, the number of reviews for three classification methods

TampaBay20Beach.csv, TampaBay20Movie.csv, TampaBay20Museum.csv, TampaBay20ShoppingMall.csv contain longitude, latitude, and names of beaches, cinemas, museums, and shopping malls obtained from Google Maps.

business_top.csv contains the top 10 cities with the most restaurants.

topfig.csv contains photos of the restaurants with high ratings.

outputa.csv.zip is the cleaned Yelp business dataset



