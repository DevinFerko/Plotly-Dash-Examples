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

# app layout
app.layout = html.Div([
    html.H4("Iris Dataset - 3D Scatter Plot"),
    dcc.Graph(id='3d-scatter-plot'),
    html.P("Sepal Length:"),
    dcc.RangeSlider(
        id='sepal-length-slider',
        min=iris_df['sepal_length'].min(),
        max=iris_df['sepal_length'].max(),
        step=0.5,
        value=[iris_df['sepal_length'].min(), iris_df['sepal_length'].max()],
        marks={i: str(i) for i in range(int(iris_df['sepal_length'].min()), int(iris_df['sepal_length'].max())+1)}
    )
])

# app callback
@app.callback(
    Output('3d-scatter-plot', 'figure'),
    Input('sepal-length-slider', 'value')
)

# define the callback function
def update_3d_scatter(sepal_length_range):
    iris_df
    low, high = sepal_length_range
    mask = (iris_df['sepal_length'] >= low) & (iris_df['sepal_length'] <= high)
    filtered_df = iris_df[mask]

    fig = px.scatter_3d(
        filtered_df,
        x='sepal_length',
        y='sepal_width',
        z='petal_length',
        color='species',
        symbol='species',
        size='petal_width',
        title='3D Scatter Plot of Iris Dataset'
    )

app.run(debug=True)