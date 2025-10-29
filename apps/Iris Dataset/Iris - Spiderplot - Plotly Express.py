# Imports Libraries
import pandas as pd
import plotly.express as px

# Load the Iris dataset from URL
url = "https://raw.githubusercontent.com/mwaskom/seaborn-data/master/iris.csv"
iris_df = pd.read_csv(url)

# Spider Plot (Radar Chart) using Plotly Express

mean_vals = iris_df.groupby('species').mean().reset_index()
fig = px.line_polar(mean_vals, 
                    r='sepal_length', 
                    theta='species', 
                    line_close=True,
                    )
fig.show()