# Terminal -> cd Dashboard -> Enter
# streamlit run Home.py -> Enter
import streamlit as st
import pandas as pd
import seaborn as sns
import plotly.express as px
import plotly.graph_objects as go
import datetime
from PIL import Image

st.title("Housing Price Dataset Analysis")

# Load the dataset from Kaggle
df = pd.read_csv('Housing.csv')

# Display the dataset
st.dataframe(df)

st.sidebar.header("Filter Options")

