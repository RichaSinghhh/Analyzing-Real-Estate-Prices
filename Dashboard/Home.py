# Terminal -> cd Dashboard -> Enter
# streamlit run Home.py -> Enter
import streamlit as st
import pandas as pd
import seaborn as sns
import plotly.express as ps
import plotly.graph_objects as go

#logo
st.sidebar.image("2D logo.png",width = 200)

# header
st.markdown(
    """
    <style>
    .custom-heading {
        color: white; /* GhostWhite text */
        font-weight: bolder;
        background-color: #666600; /* DarkSlateGray background */
        border: 2px solid #98FB98; /* black border */
        text-align: center;
        padding: 15px;
        border-radius: 10px;
        font-size: 40px;
        width: 100%;
        box-sizing: border-box; /* Ensures padding and border are included in the width */
    }
    </style>
    """,
    unsafe_allow_html=True
)
# Applying the custom heading
st.markdown("<h1 class='custom-heading'>Analyzing Real Estate Prices</h1>", unsafe_allow_html=True)

#Banner
st.image("Assets\Banner.png", use_column_width=True)


st.sidebar.title("Insights & Findings")
st.sidebar.markdown("""
### Price Trends
- Insights on the overall real estate market and trends over time.

### Area-Specific Analysis
- Breakdown of average prices by zip code or neighborhood.

### Impact of Features
- Influence of features like waterfront, views, and renovations on property prices.
""")


st.sidebar.title("Dataset Details")
st.sidebar.markdown("""
**Total Records:** 21,613 properties

**Key Columns:**
- **Date:** Sale date
- **Price:** Property price (target variable)
- **Bedrooms, Bathrooms:** Number of bedrooms and bathrooms
- **sqft_living & sqft_lot:** Square footage of the living space and lot
- **Floors, Waterfront, View:** Additional property details including whether it has waterfront access or a scenic view
- **Year Built, Year Renovated:** Property's construction year and renovation history
- **Zipcode, Latitude, Longitude:** Location details, enabling geographic analysis
""")


st.title("Welcome to the Real Estate Price Analysis Dashboard")
st.markdown("""
<p style='font-size:18px;'>This interactive dashboard is your gateway to uncovering hidden patterns, trends, and investment insights in the real estate market. Through powerful visualizations and data-driven insights, our tool transforms raw property data into valuable information. Dive into a comprehensive exploration of real estate prices across various regions and property types, helping you make informed decisions backed by data.</p>

<p style='font-size:25px;'><b>About This Project</b></p>
<p style='font-size:18px;'>Real estate pricing is influenced by multiple factors: location, property size, condition, and unique features such as scenic views or renovations. Our project breaks down these dynamics, providing a clear and actionable overview of what drives market value. By combining essential property details with regional data, we deliver a nuanced understanding of how each factor contributes to a property's overall worth.</p>

<p style='font-size:25px;'><b>Key Dataset Features</b></p>
<p style='font-size:18px;'>To uncover the complexities of property valuation, our dataset offers a rich array of features, including:</p>

<p style='font-size:20px;'><b>Property Size and Layout:</b></p>
<ul style='font-size:18px;'>
    <li><b>Living Area and Lot Size:</b> From the spaciousness of living areas (sqft_living) to expansive lot sizes (sqft_lot), these metrics reveal a property’s spatial appeal.</li>
    <li><b>Bedrooms and Bathrooms:</b> The number of bedrooms and bathrooms offers insights into a property’s layout and family-friendliness.</li>
</ul>

<p style='font-size:20px;'><b>Design and Condition:</b></p>
<ul style='font-size:18px;'>
    <li><b>Floors:</b> The number of levels can influence layout preferences and accessibility.</li>
    <li><b>Condition and Grade:</b> Ratings on property maintenance (condition) and construction quality (grade) help identify premium or value properties.</li>
</ul>

<p style='font-size:20px;'><b>Location-Specific Details:</b></p>
<ul style='font-size:18px;'>
    <li><b>Zipcode and Geographic Coordinates:</b> Zipcode gives a neighborhood context, while latitude and longitude allow for precise mapping, enabling a regional comparison of prices and demand.</li>
    <li><b>Waterfront and View Quality:</b> Properties with scenic views or waterfront locations often fetch higher prices due to their unique appeal.</li>
</ul>

<p style='font-size:20px;'><b>Construction and Renovation History:</b></p>
<ul style='font-size:18px;'>
    <li><b>Year Built and Year Renovated:</b> These features highlight a property’s age and any modernization efforts, key factors in assessing its market appeal.</li>
</ul>

<p style='font-size:25px;'><b>Project Objectives</b></p>
<p style='font-size:18px;'>Through this analysis, our dashboard enables you to:</p>
<ul style='font-size:18px;'>
    <li><b>Spot High-Value Characteristics:</b> Identify the most valuable property features and understand how they impact pricing.</li>
    <li><b>Explore Neighborhood Trends:</b> View pricing patterns and trends within different regions to understand neighborhood dynamics.</li>
    <li><b>Find Investment Opportunities:</b> Discover property types and locations with high growth potential and appreciation trends.</li>
    <li><b>Reveal Market Drivers:</b> Gain insights into the factors driving demand and market prices, supporting informed decision-making.</li>
</ul>

<p style='font-size:25px;'><b>Getting Started</b></p>
<p style='font-size:18px;'>Ready to dive in? Start by exploring data visualizations that bring each feature to life, allowing you to analyze pricing trends, compare property attributes, and understand the regional impact on real estate values. You can also upload your own real estate dataset to personalize the analysis and gain insights tailored to your specific interests or region.</p>

<p style='font-size:25px;'><b>Uncover Real Estate Insights Like Never Before</b></p>
<p style='font-size:18px;'>With our Real Estate Price Analysis Dashboard, data turns into strategy. Whether you're a real estate professional, investor, or enthusiast, this tool provides the knowledge you need to make data-backed decisions and spot new opportunities in the market.</p>
""", unsafe_allow_html=True)
