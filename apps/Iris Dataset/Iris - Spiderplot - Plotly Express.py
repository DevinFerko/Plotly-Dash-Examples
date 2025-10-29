# Imports Libraries
import pandas as pd
import plotly.express as px

# Load the Iris dataset from URL
url = "https://raw.githubusercontent.com/mwaskom/seaborn-data/master/iris.csv"
iris_df = pd.read_csv(url)

# Spider Plot (Radar Chart) using Plotly Express
fig = px.line_polar(iris_df, 
                    r='sepal_length', 
                    theta='species', 
                    line_close=True,
                    color='species',
                    template='plotly_dark',
                    title='Iris Dataset - Spider Plot (Sepal Length by Species)')
fig.show()