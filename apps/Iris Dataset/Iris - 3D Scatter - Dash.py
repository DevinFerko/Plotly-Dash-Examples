# Libraries and dependencies
from dash import Dash, dcc, html, Input, Output
import plotly.express as px
import pandas as pd

app = Dash(__name__)

# Load the Iris dataset from URL
url = "https://raw.githubusercontent.com/mwaskom/seaborn-data/master/iris.csv"
iris_df = pd.read_csv(url)

# Check dataset - comment/uncomment when needed
#print(iris_df.head())