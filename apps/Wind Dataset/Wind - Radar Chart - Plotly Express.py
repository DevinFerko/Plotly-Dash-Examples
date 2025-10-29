# Imports libraries
import mlcroissant as mlc
import pandas as pd
import plotly.express as px

# Fetch the Croissant JSON-LD
croissant_dataset = mlc.Dataset('https://www.kaggle.com/datasets/mubashirrahim/wind-power-generation-data-forecasting/croissant/download')

# Check what record sets are in the dataset
record_sets = croissant_dataset.metadata.record_sets
print(record_sets)

# Fetch the records and put them in a DataFrame
wind_df = pd.DataFrame(croissant_dataset.records(record_set=record_sets[0].uuid))

# Cleans up column names
wind_df.columns = wind_df.columns.str.replace(r'^.*?/', '', regex=True)

# creates csv file - uncomment if needed
#wind_df.to_csv('wind_data.csv', index=False)