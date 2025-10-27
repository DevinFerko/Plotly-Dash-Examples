# Imports Libraries
import pandas as pd
import plotly.express as px

# Load the Iris dataset from URL
url = "https://raw.githubusercontent.com/mwaskom/seaborn-data/master/iris.csv"
iris_df = pd.read_csv(url)

# Parallel Coordinates Plot
fig - px.parallel_coordinates(iris_df, color='species_id', labels={"species_id": "Species"},
                            color_continuous_scale=px.colors.diverging.Tealrose,
                            dimensions=['sepal_length', 'sepal_width', 'petal_length', 'petal_width'])
fig.show()