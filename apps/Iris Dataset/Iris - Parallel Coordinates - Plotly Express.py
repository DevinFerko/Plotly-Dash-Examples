# Imports Libraries
import pandas as pd
import plotly.express as px

# Load the Iris dataset from URL
url = "https://raw.githubusercontent.com/mwaskom/seaborn-data/master/iris.csv"
iris_df = pd.read_csv(url)

# Encode species for color mapping
species_coded = {'setosa': 0, 'versicolor': 1, 'virginica': 2}
iris_df['species_code'] = iris_df['species'].map(species_coded)

# Parallel Coordinates Plot
fig = px.parallel_coordinates(iris_df, 
                            color="species_code", 
                            labels={
                                "species": "Species",
                                'species_code': 'Species Code',
                                'sepal_length': 'Sepal Length',
                                'sepal_width': 'Sepal Width',
                                'petal_length': 'Petal Length',
                                'petal_width': 'Petal Width'
                            },
                            color_continuous_scale=px.colors.diverging.Tealrose,
                            dimensions=['sepal_length', 'sepal_width', 'petal_length', 'petal_width'])

# Update colorbar tick labels to show species names
fig.update_coloraxes(
    colorbar=dict(
        tickvals=[0, 1, 2],
        ticktext=['setosa', 'versicolor', 'virginica']
    )
)


fig.show()