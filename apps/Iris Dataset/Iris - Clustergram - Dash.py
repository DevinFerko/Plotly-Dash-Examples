# Imports Libraries and Dependencies
import pandas as pd
from dash import Dash, dcc, html, Input, Output, callback
import dash_bio as dashbio

# Initializes the Dash app
app = Dash()

# Reads in the Iris Dataset from a URL
iris_df = pd.read_csv("https://raw.githubusercontent.com/mwaskom/seaborn-data/master/iris.csv").set_index("species")

# Extracts the column and row names from the dataframe
columns = list(iris_df.columns.values)
rows = list(iris_df.index)

# Creates clustergram with data and customizations
clustergram = dashbio.Clustergram(
    data=iris_df.loc[rows].values,
    row_labels=rows,
    column_labels=columns,
    color_threshold={
        "row": 250, 
        "col":7000
    },
    height=750,
    width=750,
    color_map='RdBu'
)

# Defines the layout of the app
dcc.Graph(figure=clustergram.figure)