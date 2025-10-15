# Imports Libraries
import pandas as pd
import plotly.express as px

# Load the Iris dataset from URL
url = "https://raw.githubusercontent.com/mwaskom/seaborn-data/master/iris.csv"
iris_df = pd.read_csv(url)

# Check dataset - comment/uncomment when needed
print(iris_df.head())

fig = px.scatter_3d(iris_df, x='sepal_length', y='sepal_width', z='petal_length', color='species')
fig.show()