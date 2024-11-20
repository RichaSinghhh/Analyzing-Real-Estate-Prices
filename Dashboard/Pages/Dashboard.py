# Terminal -> cd Dashboard -> Enter
# streamlit run Home.py -> Enter
import streamlit as st
import pandas as pd
import seaborn as sns
import plotly.express as px
import plotly.graph_objects as go

# Load the dataset
df = pd.read_csv('Housing.csv')

# header
st.markdown(
    """
    <style>
    .custom-heading {
        color: #FFFFFF; /* White text */
        font-weight: bolder;
        background-color: #2C3E50; /* Dark Blue background */
        border: 2px solid #1ABC9C; /* Turquoise border */
        text-align: center;
        padding: 10px;
        border-radius: 10px;
        font-size: 26px;
        width: 100%; /* Makes the header wider */
        box-sizing: border-box; /* Ensures padding and border are included in the width */
    }
    </style>
    """,
    unsafe_allow_html=True
)
# Applying the custom heading
st.markdown("<h1 class='custom-heading'>Analyzing Real Estate Prices</h1>", unsafe_allow_html=True)

# Display the dataset
st.dataframe(df)

# for filter title
st.sidebar.image("Assets\logo new.png",width = 200)
st.sidebar.header("Filter Options")

# Price filter
min_price, max_price = st.sidebar.slider("Price",
                                     min_value = int(df['price'].min()),
                                     max_value = int(df['price'].max()),
                                     value = (int(df['price'].min()), int(df['price'].max())))

# sqft_living filter
min_sqft_living, max_sqft_living = st.sidebar.slider("Sqft_living",
                                     min_value = int(df['sqft_living'].min()),
                                     max_value = int(df['sqft_living'].max()),
                                     value = (int(df['sqft_living'].min()), int(df['sqft_living'].max())))

# Floor filter
floors = st.sidebar.multiselect('Floors',
                                   options = df['floors'].unique(),
                                   default = df['floors'].unique())

# Condition filter
waterfront = st.sidebar.multiselect('Waterfront',
                                   options = df['waterfront'].unique(),
                                   default = df['waterfront'].unique())

#filter the data based on the user selection
filtered_df = df[
    (df['price'] >= min_price)& 
    (df['price'] <= max_price)&
    (df['sqft_living'] >= min_sqft_living)&
    (df['sqft_living'] <= max_sqft_living)&
    (df['floors'].isin(floors))&
    (df['waterfront'].isin(waterfront))
]
st.dataframe(filtered_df)

# Create a scatter chart for Relationship between Sqft Lot and Bedrooms.
st.markdown("<h1 style = 'font-size:40px; text-align: center'>Relationship between Sqft Lot and Bedrooms</h1>",unsafe_allow_html=True)
rooms_lot = df.groupby('bedrooms') ['sqft_lot'].count().reset_index()
fig = px.scatter(rooms_lot , x = 'sqft_lot', y = 'bedrooms', title = 'Relationship between Sqft Lot and Bedrooms',color_discrete_sequence=px.colors.sequential.Plasma)
st.plotly_chart(fig)
st.markdown(
    """
    <p style='font-size:25px;'><b>Introduction</b></p> 
    <p style='font-size:18px;'>The scatter plot titled "Relationship between Sqft Lot and Bedrooms" aims to illustrate the correlation between the size of a lot in square feet (sqft_lot) and the number of bedrooms in various properties. This analysis is crucial for understanding how the size of a property lot might influence or correlate with the number of bedrooms it contains.</p> 
    
    <p style='font-size:25px;'><b>Description</b></p> 
    <p style='font-size:18px;'><b>X-Axis (Sqft Lot):</b> The x-axis represents the lot size in square feet, ranging from 0 to 10,000 square feet.</p> 
    <p style='font-size:18px;'><b>Y-Axis (Bedrooms):</b> The y-axis represents the number of bedrooms, ranging from 0 to 35.</p> 
    <p style='font-size:18px;'><b>Data Points:</b> Each point on the scatter plot represents a property, with its position determined by its lot size and number of bedrooms.</p> 
    
    <p style='font-size:25px;'><b>Key Observations</b></p> 
    <ul style='font-size:18px;'>
        <li><b>High Bedroom Count with Small Lot Sizes:</b> Several properties have a high number of bedrooms (up to 35) with relatively small lot sizes (close to 0 sqft).</li> 
        <li><b>Concentration of Data Points:</b> Most data points are clustered around the lower end of the lot size spectrum (0 to 2,000 sqft), with bedroom counts ranging from 0 to 10.</li> 
        <li><b>Sparse Data for Larger Lot Sizes:</b> Properties with larger lot sizes (above 4,000 sqft) are fewer, and these properties tend to have fewer bedrooms (0 to 5).</li> 
        <li><b>Outliers:</b> A few outliers exist, such as a property with around 35 bedrooms and a very small lot size, which might indicate a special type of property or an error in data collection.</li>
    </ul> 
    
    <p style='font-size:25px;'><b>Conclusion</b></p> 
    <p style='font-size:18px;'>The scatter plot reveals that there is no clear linear relationship between the size of a lot and the number of bedrooms. Most properties with a high number of bedrooms tend to have smaller lot sizes, while properties with larger lot sizes generally have fewer bedrooms. This suggests that larger lots are not necessarily used to build homes with more bedrooms, or it could indicate a different use of space in larger lots. Further analysis may be required to understand the underlying factors influencing this distribution.</p>
    """, 
    unsafe_allow_html=True
)

# Create a bar chart for Price Trends to Number of Bedrooms
st.markdown("<h1 style = 'font-size:40px; text-align: center'>Price Trends to Number of Bedrooms</h1>", unsafe_allow_html=True)
# Calculate the average price per number of bedrooms
bedroom_price = df.groupby('bedrooms')['price'].mean().reset_index()
fig = px.bar(bedroom_price, x='bedrooms', y='price', title='Price Trends to Number of Bedrooms', 
             labels={'bedrooms': 'Number of Bedrooms', 'price': 'Average Price (Millions)'}, 
             color='bedrooms', color_continuous_scale=px.colors.sequential.Viridis)
st.plotly_chart(fig)
st.markdown(
    """
    <p style='font-size:25px;'><b>Introduction</b></p> 
    <p style='font-size:18px;'>The bar chart titled 'Price Trends to Number of Bedrooms' illustrates the relationship between the number of bedrooms in a property and its average price. This analysis is crucial for understanding how property values fluctuate with the addition of bedrooms, which can be valuable for real estate investors, home buyers, and market analysts.</p>
    
    <p style='font-size:25px;'><b>Description of the Chart</b></p> 
    <p style='font-size:18px;'>The x-axis of the chart represents the number of bedrooms. The y-axis represents the price in millions. The chart shows bars that highlight the average price for properties with different numbers of bedrooms.</p> 
    
    <p style='font-size:25px;'><b>Key Observations</b></p> 
    <ul style='font-size:18px;'>
        <li><b>Initial Increase:</b> The price starts at approximately 0.4M for properties with no bedrooms and shows a steady increase as the number of bedrooms increases up to around 5 bedrooms.</li> 
        <li><b>Peak:</b> The price reaches its peak at around 1M for properties with approximately 7 bedrooms.</li> 
        <li><b>Decline:</b> After reaching the peak, the price sharply declines for properties with more than 7 bedrooms, dropping to around 0.6M for properties with 10 bedrooms.</li> 
        <li><b>Stabilization and Gradual Increase:</b> Beyond 10 bedrooms, the price stabilizes and then shows a gradual increase.</li> 
    </ul> 
    
    <p style='font-size:25px;'><b>Conclusion</b></p> 
    <p style='font-size:18px;'>The bar chart effectively demonstrates that property prices generally increase with the number of bedrooms up to a certain point (around 7 bedrooms), after which the prices decline sharply. However, for properties with more than 10 bedrooms, the prices stabilize and gradually increase again. This trend suggests that while adding bedrooms can increase property value, there is a threshold beyond which additional bedrooms may not significantly enhance the property's value. This information can be instrumental for stakeholders in making informed decisions regarding property investments and developments.</p>
    """, 
    unsafe_allow_html=True
)

# Create a histogram for price distribution
st.markdown("<h1 style = 'font-size:40px; text-align: center'>Price Distribution</h1>", unsafe_allow_html=True)
# Create a histogram for price distribution
fig = px.histogram(df, x='price', nbins=50, title='Price Distribution', 
                   labels={'price': 'Property Prices (Millions)'}, 
                   color_discrete_sequence=px.colors.sequential.Plasma)
st.plotly_chart(fig)
st.markdown(
    """
    <p style='font-size:25px;'><b>Introduction</b></p> 
    <p style='font-size:18px;'>The histogram titled 'Price Distribution' illustrates the spread of property prices. This visualization is crucial for understanding the diversity and range of property prices in the market. The histogram helps identify patterns, clusters, and outliers in property prices, providing valuable insights for market analysis.</p> 
    
    <p style='font-size:25px;'><b>Description</b></p> 
    <p style='font-size:18px;'><b>X-Axis (Price):</b> The x-axis represents the property prices, ranging from 0 to 8 million (M).</p> 
    <p style='font-size:18px;'><b>Y-Axis (Count):</b> The y-axis represents the number of properties within each price range.</p> 
    <p style='font-size:18px;'><b>Bars:</b> Each bar represents the count of properties within a specific price range, color-coded for clarity.</p> 
    
    <p style='font-size:25px;'><b>Key Observations:</b></p> 
    <ul style='font-size:18px;'>
        <li><b>Concentration of Properties:</b> The majority of properties are concentrated at lower price points, particularly between 0 and 1 million. This suggests that most properties in the market are priced within this range.</li> 
        <li><b>Spread of Prices:</b> As the price increases, the number of properties decreases, indicating fewer properties at higher price points.</li> 
        <li><b>High-Value Outliers:</b> There are some high-value outliers, with property prices extending up to 8 million. These outliers reflect the presence of luxury properties in the market.</li> 
        <li><b>Market Diversity:</b> The wide range of property prices, from low to high, highlights the diversity in the market, catering to different segments of buyers.</li>
    </ul> 
    
    <p style='font-size:25px;'><b>Conclusion:</b></p> 
    <p style='font-size:18px;'>The histogram effectively displays the distribution of property prices, revealing a market with a high concentration of lower-priced properties and a few high-value outliers. This information is essential for stakeholders, including buyers, sellers, and investors, to make informed decisions based on market trends and property price diversity.</p>
    """, 
    unsafe_allow_html=True
)


# Creating the line chart for Date vs Price
st.markdown("<h1 style = 'font-size:40px; text-align: center'>Date vs Price</h1>", unsafe_allow_html=True)
# Preparing data
df['date'] = pd.to_datetime(df['date'])
date_price = df.groupby('date')['price'].mean().reset_index()
fig = px.line(date_price, x='date', y='price', title='Date vs Price', labels={'date': 'Date', 'price': 'Average Price (Millions)'}, color_discrete_sequence=px.colors.sequential.Plasma)
st.plotly_chart(fig)
st.markdown(
    """
    <p style='font-size:25px;'><b>Introduction</b></p>
    <p style='font-size:18px;'>The line chart titled 'Date vs Price' illustrates the fluctuations in property prices over a specified period. This analysis is crucial for understanding how property prices have changed over time, providing valuable insights for market analysts, investors, and stakeholders.</p>
    
    <p style='font-size:25px;'><b>Description</b></p>
    <p style='font-size:18px;'><b>X-Axis (Date):</b> The x-axis represents the dates, ranging from 2014-05-02 to 2015-05-15.</p>
    <p style='font-size:18px;'><b>Y-Axis (Price):</b> The y-axis represents the property prices.</p>
    
    <p style='font-size:25px;'><b>Key Observations</b></p>
    <ul style='font-size:18px;'>
        <li><b>Trends:</b> Noticeable trends in property prices over time, with certain periods showing higher activity.</li>
        <li><b>Fluctuations:</b> Significant fluctuations throughout the period, indicating varying market activity.</li>
        <li><b>Peaks and Troughs:</b> High market activity at certain points and declines at others, reflecting seasonal trends.</li>
    </ul>
    
    <p style='font-size:25px;'><b>Conclusion</b></p>
    <p style='font-size:18px;'>The 'Date vs Price' line chart highlights the trends and fluctuations in market activity over the specified period. These insights are valuable for making informed decisions in the housing market.</p>
    """, 
    unsafe_allow_html=True
)


# Create a bar chart for Price Trends to Number of Floors
st.markdown("<h1 style='font-size:40px; text-align: center'>Price Trends to Number of Floors</h1>", unsafe_allow_html=True)
# Calculate the average price per number of floors
floors_price = df.groupby('floors')['price'].mean().reset_index()
fig = px.bar(floors_price, x='floors', y='price', title='Price Trends to Number of Floors', 
             labels={'floors': 'Number of Floors', 'price': 'Average Price (Millions)'}, 
             color='floors', color_discrete_sequence=px.colors.sequential.Plasma)
st.plotly_chart(fig)
st.markdown(
    """
    <p style='font-size:25px;'><b>Introduction</b></p>
    <p style='font-size:18px;'>The graph titled 'Price Trends to Number of Floors' illustrates the relationship between the number of floors in a property and its average price. This analysis helps understand how the number of floors impacts property values, providing insights useful for real estate investors, home buyers, and market analysts.</p>
    
    <p style='font-size:25px;'><b>Description</b></p>
    <p style='font-size:18px;'><b>X-Axis (Floors):</b> The x-axis represents the number of floors.</p>
    <p style='font-size:18px;'><b>Y-Axis (Price):</b> The y-axis represents the average price in millions.</p>
    <p style='font-size:18px;'><b>Bars:</b> Each bar represents the average price for properties with the respective number of floors, color-coded for clarity.</p>
    
    <p style='font-size:25px;'><b>Key Observations</b></p>
    <ul style='font-size:18px;'>
        <li><b>Initial Increase:</b> The average price starts at around 0.6 million for properties with 1 floor.</li>
        <li><b>Peak at 2 Floors:</b> The price increases steadily, peaking at around 1 million for properties with 2 floors.</li>
        <li><b>Decline:</b> After reaching the peak, the average price drops to around 0.5 million for properties with 3 floors.</li>
    </ul>
    
    <p style='font-size:25px;'><b>Conclusion</b></p>
    <p style='font-size:18px;'>The graph indicates that properties with 2 floors have the highest average price, while those with 1 or 3 floors have lower average prices. This trend suggests that 2-floor properties may be the most desirable, possibly due to a balance of space and layout efficiency. Understanding these trends can help stakeholders make informed decisions in the real estate market.</p>
    """, 
    unsafe_allow_html=True
)


# Waterfront and View.
st.markdown("<h1 style = 'font-size:40px; text-align: center'>Waterfront and View</h1>", unsafe_allow_html=True)
# Creating the heatmap.
waterfront_view = pd.crosstab(df['waterfront'], df['view'])
fig = px.imshow(waterfront_view, labels = dict(x = 'View', y = 'Waterfront', color = 'Count'),
          x = waterfront_view.columns,
          y = waterfront_view.index,
          color_continuous_scale = 'viridis')
st.plotly_chart(fig)
st.markdown(
    """
    <p style='font-size:25px;'><b>Introduction</b></p>
    <p style='font-size:18px;'>The graph titled "Waterfront and View" presents a cross-tabulation analysis of waterfront properties and their view ratings. The purpose of this analysis is to explore the relationship between the presence of a waterfront and the quality of the view, which may influence buyer preferences and property values.</p>
    
    <p style='font-size:25px;'><b>Description</b></p>
    <p style='font-size:18px;'>The graph is a heatmap that visualizes the count of properties based on two variables: "Waterfront" and "View."</p>
    <p style='font-size:18px;'><b>Y-Axis (Waterfront):</b> The y-axis represents whether a property is a waterfront property (1) or not (0), ranging from -0.5 to 1.5.</p>
    <p style='font-size:18px;'><b>X-Axis (View):</b> The x-axis represents different view ratings, ranging from 0 to 4.</p>
    <p style='font-size:18px;'><b>Color Intensity:</b> The color intensity in the heatmap indicates the count of properties, with a color scale ranging from purple (low count) to yellow (high count).</p>
    
    <p style='font-size:25px;'><b>Key Observations</b></p>
    <ul style='font-size:18px;'>
        <li><b>High Count of Non-Waterfront Properties with Low View Ratings:</b> The yellow section in the heatmap indicates a high count of non-waterfront properties (Waterfront = 0) with the lowest view rating (View = 0).</li>
        <li><b>Low Count of Waterfront Properties:</b> The purple sections indicate a relatively low count of waterfront properties (Waterfront = 1) across all view ratings.</li>
        <li><b>Correlation Between Waterfront and View:</b> The heatmap suggests that waterfront properties are more likely to have higher view ratings, as indicated by the distribution of colors.</li>
    </ul>
    
    <p style='font-size:25px;'><b>Conclusion</b></p>
    <p style='font-size:18px;'>The analysis reveals a correlation between waterfront location and scenic views. Waterfront properties tend to have higher view ratings, which may influence buyer preferences and property values. This insight can be valuable for real estate developers and investors when assessing the potential value of properties based on their location and view quality.</p>
    """, 
    unsafe_allow_html=True
)


#Cross-tabulation between Grade and Condition.
st.markdown("<h1 style = 'font-size:40px; text-align: center'>Cross-tabulation between Grade and Condition</h1>", unsafe_allow_html=True)
# Creating the heatmap
grade_condition = pd.crosstab(df['grade'], df['condition'])
fig = px.imshow(grade_condition,
          labels = dict(x = 'Grade', y = 'Condition', color = 'count'),
          x = grade_condition.columns,
          y = grade_condition.index,
          color_continuous_scale= 'viridis',
          title = 'Cross-tabulation between Grade and Condition')        
st.plotly_chart(fig)
st.markdown(
    """
    <p style='font-size:25px;'><b>Introduction</b></p>
    <p style='font-size:18px;'>The heatmap titled "Cross-tabulation between Grade and Condition" visualizes the relationship between the grade (quality of construction) and the condition of properties. This analysis is crucial for understanding how the quality of construction influences the overall condition of properties, which can impact market valuations.</p>
    
    <p style='font-size:25px;'><b>Description</b></p>
    <p style='font-size:18px;'>The heatmap is a graphical representation where:</p>
    <p style='font-size:18px;'><b>X-Axis (Grade):</b> The x-axis represents the grade of the property, ranging from 1 to 4.</p>
    <p style='font-size:18px;'><b>Y-Axis (Condition):</b> The y-axis represents the condition of the property, ranging from 0 to 12.</p>
    <p style='font-size:18px;'><b>Color Intensity:</b> The color intensity in the heatmap indicates the count of properties that fall into each grade-condition combination. The color scale ranges from purple (indicating a count of 0) to yellow (indicating a count of 4,000 or more).</p>
    
    <p style='font-size:25px;'><b>Key Observations</b></p>
    <ul style='font-size:18px;'>
        <li><b>Concentration of Data:</b> The majority of the data points are concentrated in the middle of the heatmap, particularly around grade 3 and condition 7.</li>
        <li><b>High Counts:</b> The highest counts (yellow regions) are observed in the grade 3 and condition 7 area, indicating that most properties fall into this category.</li>
        <li><b>Grade and Condition Correlation:</b> There is a noticeable trend where higher grades (3 and 4) are associated with better conditions (6 to 8), suggesting a positive correlation between grade and condition.</li>
        <li><b>Low Counts:</b> Lower counts (purple regions) are observed at the extremes of the grade and condition scales, indicating fewer properties with very low or very high grades and conditions.</li>
    </ul>
    
    <p style='font-size:25px;'><b>Conclusion</b></p>
    <p style='font-size:18px;'>The heatmap effectively illustrates the relationship between the grade and condition of properties. The concentration of data points around grade 3 and condition 7 suggests that most properties are of moderate quality and condition. The positive correlation between higher grades and better conditions highlights the importance of construction quality in determining property condition and, consequently, market valuation. This visualization provides valuable insights for real estate analysts and investors in assessing property quality and making informed decisions.</p>
    """, 
    unsafe_allow_html=True
)


# House Price by Zipcode
st.markdown("<h1 style='font-size:40px; text-align: center'>House Price by Zipcode</h1>", unsafe_allow_html= True)
# Calculating median price by zipcode
zipcode_price = df.groupby('zipcode')['price'].median().reset_index()
# Creating the bar chart
fig = px.bar(zipcode_price, x='zipcode', y='price', title='House Price by Zipcode',
             labels={'zipcode': 'Zipcode', 'price': 'Median Price (Millions)'},
             color='zipcode', color_continuous_scale=px.colors.sequential.Viridis)
st.plotly_chart(fig)
st.markdown(
    """
    <p style='font-size:25px;'><b>Introduction</b></p>
    <p style='font-size:18px;'>The bar chart titled 'House Price by Zipcode' illustrates the median house prices across various zip codes. This chart is significant as it highlights how location influences property values. Certain zip codes exhibit notably higher median prices, likely due to factors such as proximity to amenities, neighborhood desirability, and local demand.</p>
    
    <p style='font-size:25px;'><b>Description</b></p>
    <p style='font-size:18px;'><b>Y-Axis (Median House Prices):</b> The y-axis represents the median house prices, ranging from 0 to 1.5 million dollars.</p>
    <p style='font-size:18px;'><b>X-Axis (Zip Codes):</b> The x-axis represents different zip codes.</p>
    <p style='font-size:18px;'><b>Bars:</b> Each bar represents the median house price for a specific zip code.</p>
    
    <p style='font-size:25px;'><b>Key Observations</b></p>
    <ul style='font-size:18px;'>
        <li><b>Price Variation:</b> There is a noticeable variation in house prices across different zip codes. Some zip codes have median prices below $500,000, while others exceed $1 million.</li>
        <li><b>High-Price Zip Codes:</b> Certain zip codes stand out with exceptionally high median house prices, reaching up to 1.5 million dollars.</li>
        <li><b>Clustered Prices:</b> There are clusters of zip codes where the median house prices are relatively similar, indicating areas with comparable property values.</li>
        <li><b>Outliers:</b> A few zip codes have significantly higher prices compared to the rest, which could be due to unique local factors such as exclusive neighborhoods or high demand.</li>
    </ul>
    
    <p style='font-size:25px;'><b>Conclusion</b></p>
    <p style='font-size:18px;'>The bar chart effectively demonstrates the impact of location on house prices. The significant variation in median house prices across different zip codes underscores the importance of location in real estate valuation. Areas with higher prices are likely influenced by factors such as proximity to amenities, neighborhood desirability, and local demand. This information is crucial for potential homebuyers, real estate investors, and policymakers to understand the dynamics of the housing market in different regions.</p>
    """, 
    unsafe_allow_html=True
)


# House Price by year Built.
st.markdown("<h1 style='font-size:40px; text-align: center'>House Price by Year Built</h1>", unsafe_allow_html=True)
# Calculating median price by year built
yr_built_price = df.groupby('yr_built')['price'].median().reset_index()
# Creating the scatter chart with a regression line
fig = px.scatter(yr_built_price, x='yr_built', y='price', trendline='ols', 
                 title='House Price by Year Built',
                 labels={'yr_built': 'Year Built', 'price': 'Median Price (Millions)'}, 
                 color_discrete_sequence=['#1f77b4'])
st.plotly_chart(fig)
st.markdown(
    """
    <p style='font-size:25px;'><b>Introduction</b></p>
    <p style='font-size:18px;'>The chart titled "House Price by Year Built" shows the relationship between the year a house was built and its median price. By visualizing this relationship, we can observe trends over time and identify how the age of a property influences its market value.</p>
    
    <p style='font-size:25px;'><b>Description</b></p>
    <p style='font-size:18px;'>The chart is a scatter plot with the x-axis labeled "Year Built" and the y-axis labeled "Median Price (Millions)." Each point represents the median price of houses built in a specific year. The regression line (OLS) adds a trendline to highlight the overall trend in the data. The color scheme chosen provides a clear and professional look.</p>
    
    <p style='font-size:25px;'><b>Key Observations</b></p>
    <ul style='font-size:18px;'>
        <li><b>Historical Trends:</b> Older houses tend to have different pricing trends compared to newer ones.</li>
        <li><b>Price Variability:</b> There is variability in house prices across different years, which can be influenced by various factors such as construction quality and market conditions at the time.</li>
        <li><b>Trend Analysis:</b> The regression line shows the overall trend in house prices over the years, helping to identify any consistent increase or decrease in prices.</li>
    </ul>
    
    <p style='font-size:25px;'><b>Conclusion</b></p>
    <p style='font-size:18px;'>The scatter plot with a regression line provides a comprehensive view of how house prices have evolved based on the year they were built. This information is valuable for real estate analysts and investors to make informed decisions regarding property investments and pricing strategies.</p>
    """, 
    unsafe_allow_html=True
)


# Relationship between Sqft Living and Price
st.markdown("<h1 style='font-size:40px; text-align: center'>Relationship between Sqft Living and Price</h1>",unsafe_allow_html=True)
# Creating the scatter plot with a trend line
fig = px.scatter(df, x='sqft_living', y='price', trendline='ols', title='Relationship between Sqft Living and Price',
                 labels={'sqft_living': 'Square Footage of Living Space', 'price': 'Price (Millions)'}, color_discrete_sequence=['#1f77b4'])
st.plotly_chart(fig)
st.markdown(
    """
    <p style='font-size:25px;'><b>Introduction</b></p>
    <p style='font-size:18px;'>The graph titled 'Relationship between Sqft Living and Price' illustrates the correlation between the square footage of living space (sqft_living) and the price of properties. This scatter plot is a visual representation of how property prices tend to vary with the size of the living area, providing valuable insights for real estate analysis.</p>
    
    <p style='font-size:25px;'><b>Description</b></p>
    <p style='font-size:18px;'>The scatter plot displays data points representing individual properties:</p>
    <p style='font-size:18px;'><b>X-Axis (Sqft Living):</b> The x-axis is labeled as 'sqft_living' and ranges from 0 to 14,000 square feet.</p>
    <p style='font-size:18px;'><b>Y-Axis (Price):</b> The y-axis is labeled as 'price' and ranges from 0 to 8 million dollars.</p>
    <p style='font-size:18px;'><b>Data Points:</b> Each point on the graph corresponds to a property, showing its living space in square feet and its price.</p>
    
    <p style='font-size:25px;'><b>Key Observations</b></p>
    <ul style='font-size:18px;'>
        <li><b>Positive Correlation:</b> There is a clear positive correlation between square footage and price. As the living space increases, the price of the property generally increases.</li>
        <li><b>Clustered Data:</b> Most data points are clustered between 0 to 6,000 square feet and 0 to 2 million dollars, indicating that the majority of properties fall within this range.</li>
        <li><b>Outliers:</b> There are a few outliers with significantly higher prices and larger living spaces, extending up to 14,000 square feet and 8 million dollars.</li>
        <li><b>Price Variation:</b> While larger living spaces typically command higher prices, there is still considerable variation in prices for properties with similar square footage, suggesting other factors also influence property value.</li>
    </ul>
    
    <p style='font-size:25px;'><b>Conclusion</b></p>
    <p style='font-size:18px;'>The scatter plot effectively demonstrates the importance of square footage in determining property value. Larger living spaces are generally associated with higher prices, emphasizing the role of size in real estate pricing. However, the variation in prices for similar square footage indicates that other factors also play a significant role in property valuation. This analysis can be useful for real estate professionals and potential buyers in understanding market trends and making informed decisions.</p>
    """, 
    unsafe_allow_html=True
)


# Relationship between Sqft Lot and Price.
st.markdown("<h1 style='font-size:40px; text-align: center'>Relationship between Sqft Lot and Price</h1>",unsafe_allow_html=True)
# Creating the scatter plot with a trend line
fig = px.scatter(df, x='sqft_lot', y='price', trendline='ols', title='Relationship between Sqft Lot and Price',
                 labels={'sqft_lot': 'Square Footage of Lot', 'price': 'Price (Millions)'}, color_discrete_sequence=['#1f77b4'])
st.plotly_chart(fig)
st.markdown(
    """
    <p style='font-size:25px;'><b>Introduction</b></p>
    <p style='font-size:18px;'>The graph titled 'Relationship between Sqft Lot and Price' aims to explore the correlation between the size of a lot (measured in square feet) and the price of the property. This analysis is crucial for understanding how lot size impacts property values, which can be beneficial for real estate investors, homebuyers, and urban planners.</p>
    
    <p style='font-size:25px;'><b>Description</b></p>
    <p style='font-size:18px;'>The scatter plot in the graph displays data points representing individual properties:</p>
    <p style='font-size:18px;'><b>X-Axis (Sqft Lot):</b> The x-axis measures the lot size in square feet, ranging from 0 to approximately 1.5 million square feet.</p>
    <p style='font-size:18px;'><b>Y-Axis (Price):</b> The y-axis measures the property price in dollars, ranging from 0 to 8 million dollars.</p>
    <p style='font-size:18px;'><b>Data Points:</b> Each point on the scatter plot represents a property, showing its lot size and corresponding price.</p>
    
    <p style='font-size:25px;'><b>Key Observations</b></p>
    <ul style='font-size:18px;'>
        <li><b>General Trend:</b> There is a general trend indicating that larger lot sizes tend to be associated with higher property prices. However, this trend is not strictly linear.</li>
        <li><b>High Density of Data Points:</b> A significant concentration of data points is observed in the lower range of both lot size and price, particularly below 500,000 square feet and 2 million dollars.</li>
        <li><b>Outliers:</b> There are several outliers where properties with relatively small lot sizes have very high prices, and vice versa.</li>
        <li><b>Variation:</b> The variation in property prices for similar lot sizes suggests that other factors, such as location or zoning laws, might also play a significant role in determining property value.</li>
    </ul>
    
    <p style='font-size:25px;'><b>Conclusion</b></p>
    <p style='font-size:18px;'>The scatter plot reveals that while larger lot sizes generally correlate with higher property prices, the relationship is influenced by other factors. The high variation in prices for similar lot sizes indicates that elements like location, zoning laws, and possibly other amenities significantly impact property values. This analysis underscores the complexity of real estate pricing and the need to consider multiple variables when evaluating property investments.</p>
    """, 
    unsafe_allow_html=True
)


# Relationship between Floors and Price.
st.markdown("<h1 style='font-size:40px; text-align: center'>Relationship between Floors and Price</h1>",unsafe_allow_html=True)
# Calculating median and standard deviation of price by floors
floors_price = df.groupby('floors')['price'].agg(['median', 'std']).reset_index()
# Creating the bar chart with error bars
fig = px.bar(floors_price, x='floors', y='median', error_y='std', title='Relationship between Floors and Price',
             labels={'floors': 'Number of Floors', 'median': 'Median Price (Thousands)', 'std': 'Standard Deviation'},
             color='floors', color_continuous_scale=px.colors.sequential.Inferno)
st.plotly_chart(fig)
st.markdown(
    """
    <p style='font-size:25px;'><b>Introduction</b></p>
    <p style='font-size:18px;'>The graph titled 'Relationship between Floors and Price' illustrates the correlation between the number of floors in a building and its corresponding price. This analysis is crucial for understanding how the number of floors impacts property prices, which can be valuable for real estate investors, developers, and buyers.</p>
    
    <p style='font-size:25px;'><b>Description</b></p>
    <p style='font-size:18px;'>The bar chart displays the relationship between the number of floors and the price in thousands of dollars:</p>
    <p style='font-size:18px;'><b>X-Axis (Floors):</b> The x-axis is labeled 'floors' and includes the categories 1, 1.5, 2, 2.5, 3, and 3.5 floors.</p>
    <p style='font-size:18px;'><b>Y-Axis (Price):</b> The y-axis is labeled 'price' and ranges from 0 to 800k, with increments of 200k.</p>
    <p style='font-size:18px;'><b>Bars:</b> Each bar represents the price for properties with the respective number of floors, with error bars indicating the standard deviation of prices.</p>
    
    <p style='font-size:25px;'><b>Key Observations</b></p>
    <ul style='font-size:18px;'>
        <li><b>1 Floor:</b> The price is approximately 300k.</li>
        <li><b>1.5 Floors:</b> The price increases to around 450k.</li>
        <li><b>2 Floors:</b> The price remains steady at about 450k.</li>
        <li><b>2.5 Floors:</b> The price peaks at around 700k, the highest among all categories.</li>
        <li><b>3 Floors:</b> The price drops to approximately 400k.</li>
        <li><b>3.5 Floors:</b> The price slightly increases to around 450k.</li>
    </ul>
    
    <p style='font-size:25px;'><b>Conclusion</b></p>
    <p style='font-size:18px;'>The graph indicates that the price of properties generally increases with the number of floors up to 2.5 floors, where it reaches its peak. Beyond 2.5 floors, the price tends to decrease. This suggests that while adding more floors can increase property value, there is a threshold (2.5 floors) beyond which additional floors may not contribute to higher prices and may even reduce the value. This insight can help stakeholders make informed decisions regarding property investments and developments.</p>
    """, 
    unsafe_allow_html=True
)

# Relationship between View and Price.
st.markdown("<h1 style='font-size:40px; text-align: center'>Relationship between View and Price</h1>",unsafe_allow_html=True)
# Calculating median view and price
view_price = df.groupby('view')['price'].median().reset_index()
# Creating the box plot
fig = px.box(df, x='view', y='price', title='Relationship between View and Price',
             labels={'view': 'View Quality', 'price': 'Price (Millions)'},
             color='view', color_discrete_sequence=px.colors.sequential.Teal)
st.plotly_chart(fig)
st.markdown(
    """
    <p style='font-size:25px;'><b>Introduction</b></p>
    <p style='font-size:18px;'>The chart titled "Relationship between View and Price" illustrates the correlation between the view quality of homes and their corresponding prices. The view quality is a measure of the visual appeal of the surroundings, with higher values indicating better views. This chart is relevant as it provides insights into how view quality affects the market value of homes, which is crucial for real estate analysts, investors, and potential homebuyers.</p>
    
    <p style='font-size:25px;'><b>Description</b></p>
    <p style='font-size:18px;'>The chart is a box plot with the x-axis labeled "view" and the y-axis labeled "price." The view quality ranges from 0 to 4, and the prices are measured in millions (M). The boxes represent the interquartile range of prices for each view quality, with the whiskers indicating the range and the dots representing outliers. The plot shows that higher view quality tends to correlate with higher prices.</p>
    
    <p style='font-size:25px;'><b>Key Observations</b></p>
    <ul style='font-size:18px;'>
        <li><b>Poor View (0-1):</b> Homes with lower view quality have a wider price range but generally lower median prices.</li>
        <li><b>Average View (2-3):</b> As the view quality improves, there is a noticeable increase in median prices and a tighter price range.</li>
        <li><b>Excellent View (4):</b> The highest view quality shows significantly higher prices with some variability, indicating a premium for scenic surroundings.</li>
    </ul>
    
    <p style='font-size:25px;'><b>Conclusion</b></p>
    <p style='font-size:18px;'>The chart demonstrates a positive correlation between view quality and home prices. Higher view quality adds significant value to properties, likely due to the aesthetic and lifestyle appeal of scenic surroundings. This information is valuable for stakeholders in the real estate market to make informed decisions regarding property investments and pricing strategies.</p>
    """, 
    unsafe_allow_html=True
)


# Relationship between Condition and Price.
st.markdown("<h1 style = 'font-size:40px; text-align: center'>Relationship between Condition and Price</h1>", unsafe_allow_html=True)
# Calculating median condition and price.
condition_price = df.groupby('condition')['price'].median().reset_index()
fig = px.bar(condition_price, x='condition', y='price', title='Relationship between Condition and Price', 
             labels={'condition': 'Property Condition', 'price': 'Median Price (Thousands)'}, 
             color='condition', color_discrete_sequence=px.colors.sequential.Plasma)
st.plotly_chart(fig)
st.markdown(
    """
    <p style='font-size:25px;'><b>Introduction</b></p>
    <p style='font-size:18px;'>The graph titled "Relationship between Condition and Price" illustrates the correlation between the condition of properties and their respective prices. This bar chart is significant as it highlights how the condition of a property can impact its market value, emphasizing the importance of property maintenance and upkeep in enhancing property value.</p>
    
    <p style='font-size:25px;'><b>Description</b></p>
    <p style='font-size:18px;'>The bar chart displays the average price of properties across five different condition levels, ranging from 1 to 5:</p>
    <p style='font-size:18px;'><b>X-Axis (Condition):</b> The x-axis represents the condition of the properties, with 1 being the lowest condition and 5 being the highest.</p>
    <p style='font-size:18px;'><b>Y-Axis (Price):</b> The y-axis represents the price of the properties, measured in thousands of dollars (k).</p>
    
    <p style='font-size:25px;'><b>Key Observations</b></p>
    <ul style='font-size:18px;'>
        <li><b>Condition 1:</b> Properties in the lowest condition (1) have an average price of approximately 200k.</li>
        <li><b>Condition 2:</b> Properties in condition 2 also have an average price around 200k, indicating no significant price difference from condition 1.</li>
        <li><b>Condition 3:</b> Properties in condition 3 show a noticeable increase in price, averaging around 350k.</li>
        <li><b>Condition 4:</b> Properties in condition 4 maintain a similar price to condition 3, averaging slightly below 400k.</li>
        <li><b>Condition 5:</b> Properties in the highest condition (5) have the highest average price, reaching approximately 450k.</li>
    </ul>
    
    <p style='font-size:25px;'><b>Conclusion</b></p>
    <p style='font-size:18px;'>The bar chart clearly demonstrates that properties in better condition tend to have higher prices. This trend underscores the importance of maintaining and improving property conditions to enhance market value. Property owners and investors should consider investing in property upkeep and maintenance to achieve higher returns on their investments.</p>
    """, 
    unsafe_allow_html=True
)


# Relationship between Grade and Price.
st.markdown("<h1 style = 'font-size:40px; text-align: center'>Relationship between Grade and Price</h1>", unsafe_allow_html=True)
# Calculating median Grade and price.
grade_price = df.groupby('grade')['price'].median().reset_index()
fig = px.bar(grade_price, x='grade', y='price', title='Relationship between Grade and Price', 
             labels={'grade': 'Grade', 'price': 'Median Price (Millions)'}, 
             color='grade', color_discrete_sequence=px.colors.sequential.Teal)
st.plotly_chart(fig)
st.markdown(
    """
    <p style='font-size:25px;'><b>Introduction</b></p>
    <p style='font-size:18px;'>The chart titled "Relationship between Grade and Price" illustrates the correlation between the grade of homes and their corresponding prices. The grade is a measure of the quality of the homes, with higher grades indicating better quality. This chart is relevant as it provides insights into how the quality of homes affects their market value, which is crucial for real estate analysts, investors, and potential homebuyers.</p>
    
    <p style='font-size:25px;'><b>Description</b></p>
    <p style='font-size:18px;'>The chart is a bar graph with the x-axis labeled "grade" and the y-axis labeled "price." The grades range from 1 to 13, and the prices are measured in millions (M). The bars represent the average price of homes for each grade. The chart shows a clear upward trend, indicating that higher-grade homes tend to have higher prices.</p>
    
    <p style='font-size:25px;'><b>Key Observations</b></p>
    <ul style='font-size:18px;'>
        <li><b>Low-Grade Homes (Grades 1-4):</b> The prices for homes with grades between 1 and 4 are relatively low, generally below 0.5M.</li>
        <li><b>Mid-Grade Homes (Grades 5-8):</b> There is a slight increase in prices for homes with grades between 5 and 8, with prices ranging from 0.5M to 1M.</li>
        <li><b>High-Grade Homes (Grades 9-12):</b> A significant increase in prices is observed for homes with grades between 9 and 12, with prices ranging from 1M to 2.5M.</li>
        <li><b>Top-Grade Homes (Grade 13):</b> The highest grade, 13, shows a substantial price jump, with prices reaching up to 3M.</li>
    </ul>
    
    <p style='font-size:25px;'><b>Conclusion</b></p>
    <p style='font-size:18px;'>The chart clearly demonstrates a positive correlation between the grade of homes and their prices. Higher-grade homes command a premium price, likely due to their perceived durability, aesthetic appeal, and added features. This information is valuable for stakeholders in the real estate market to make informed decisions regarding property investments and pricing strategies.</p>
    """, 
    unsafe_allow_html=True
)


# Relationship between Waterfront and Price.
st.markdown("<h1 style = 'font-size:40px; text-align: center'>Relationship between Waterfront and Price</h1>",unsafe_allow_html=True)
# Creating the violin plot with a color palette
fig = px.violin(df, x='waterfront', y='price', title='Relationship between Waterfront and Price', 
                labels={'waterfront': 'Waterfront Status', 'price': 'Price (Millions)'}, 
                color='waterfront', color_discrete_sequence=px.colors.sequential.Inferno)
st.plotly_chart(fig)
st.markdown(
    """
    <p style='font-size:25px;'><b>Introduction</b></p>
    <p style='font-size:18px;'>The graph titled "Relationship between Waterfront and Price" illustrates the impact of waterfront status on property prices. This analysis is essential for understanding how proximity to water bodies affects the market value of properties, providing valuable insights for real estate investors, developers, and buyers.</p>
    
    <p style='font-size:25px;'><b>Description</b></p>
    <p style='font-size:18px;'>The violin plot compares the distribution of property prices based on their waterfront status:</p>
    <p style='font-size:18px;'><b>X-Axis (Waterfront Status):</b> The x-axis represents the waterfront status, with 0 indicating non-waterfront properties and 1 indicating waterfront properties.</p>
    <p style='font-size:18px;'><b>Y-Axis (Price):</b> The y-axis represents the price of properties in millions of dollars.</p>
    <p style='font-size:18px;'><b>Data Distribution:</b> Each violin plot shows the distribution of prices for the respective waterfront status, including the median and range of the data.</p>
    
    <p style='font-size:25px;'><b>Key Observations</b></p>
    <ul style='font-size:18px;'>
        <li><b>Non-Waterfront Properties:</b> The distribution of prices for non-waterfront properties (waterfront status = 0) is centered around $0.4 million.</li>
        <li><b>Waterfront Properties:</b> The distribution of prices for waterfront properties (waterfront status = 1) shows a wider range and higher median price, around $1.2 million.</li>
        <li><b>Price Premium:</b> The plot shows that waterfront properties command a substantial price premium compared to non-waterfront properties.</li>
    </ul>
    
    <p style='font-size:25px;'><b>Conclusion</b></p>
    <p style='font-size:18px;'>The violin plot effectively highlights the considerable value added by a property's proximity to water. Waterfront properties are significantly more expensive than non-waterfront properties, underscoring the luxury and desirability associated with being near water. This information is crucial for real estate investors and buyers, as it demonstrates the significant impact of location on property value.</p>
    """, 
    unsafe_allow_html=True
)
# header
st.markdown(
    """
    <style>
    .custom-heading {
        color: #FFFFFF; /* White text */
        font-weight: bolder;
        background-color: #2C3E50; /* Dark Blue background */
        border: 2px solid #1ABC9C; /* Turquoise border */
        text-align: center;
        padding: 10px;
        border-radius: 10px;
        font-size: 26px;
        width: 100%; /* Makes the header wider */
        box-sizing: border-box; /* Ensures padding and border are included in the width */
    }
    </style>
    """,
    unsafe_allow_html=True
)
# Applying the custom heading
st.markdown("<h1 class='custom-heading'>Overall Summary and Key Takeaways</h1>", unsafe_allow_html=True)

#summary
st.markdown("""

<p style='font-size:20px;'><b>Aggregate Price Patterns</b></p>
<ul style='font-size:18px;'>
    <li><b>Price Distribution:</b> The data shows that prices vary significantly, with location and property size being primary drivers. High-demand areas, particularly those near water, show marked increases in property values. This suggests a strong market premium for location.</li>
</ul>

<p style='font-size:20px;'><b>Characteristics of High-Value Properties</b></p>
<ul style='font-size:18px;'>
    <li><b>Size and Layout:</b> Properties with larger living spaces, more bedrooms, and additional features like extra floors tend to command higher prices, confirming that these are desirable characteristics for buyers.</li>
    <li><b>Renovations and Quality Ratings:</b> Properties with high grades or recent renovations have consistently higher prices, emphasizing the importance of quality and modernity in property valuation.</li>
</ul>

<p style='font-size:20px;'><b>Impact of Neighborhood and Location Factors</b></p>
<ul style='font-size:18px;'>
    <li><b>Neighborhood Influence:</b> Properties in areas with higher average square footage (sqft_living15) and larger lot sizes (sqft_lot15) tend to have higher prices, reflecting neighborhood demand and property quality.</li>
    <li><b>Latitude and Longitude:</b> There’s a clear price correlation with specific geographic regions, suggesting that certain areas are more desirable, likely due to amenities or geographic desirability.</li>
</ul>

<p style='font-size:25px;'><b>Final Observations and Recommendations</b></p>
<ul style='font-size:18px;'>
    <li><b>Investment Opportunities:</b> Based on the observed data, properties in certain zip codes or near water appear to have strong value retention and appreciation potential, making them ideal for long-term investment.</li>
    <li><b>Renovation and Upgrades:</b> For properties in middle-value ranges, strategic renovations (e.g., increasing living area, upgrading condition) can enhance value significantly, making them more competitive in the market.</li>
    <li><b>Market Demand:</b> The dataset suggests a clear preference for properties with larger living areas and desirable views, reinforcing the importance of these factors in real estate decisions.</li>
</ul>
""", unsafe_allow_html=True)



