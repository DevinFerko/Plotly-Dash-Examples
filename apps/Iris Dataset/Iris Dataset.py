# Imports Libraries
import pandas as pd

# Load the Iris dataset from URL
url = "https://raw.githubusercontent.com/mwaskom/seaborn-data/master/iris.csv"
iris_df = pd.read_csv(url)

# Check uncomment when needed
print(iris_df.head())