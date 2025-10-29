# Imports Libraries
import pandas as pd
import plotly.express as px

# Load the Wind dataset from URL
url = "https://raw.githubusercontent.com/datasets/wind/master/data/wind.csv"
wind_df = pd.read_csv(url)
wind_df.head()