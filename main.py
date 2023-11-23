# main.py
import pandas as pd
from analysis import perform_data_analysis
from visualise import visualise_data

# Load data
nba_data = pd.read_csv('nba_stats.csv')

# Perform data analysis
anal_data = perform_data_analysis(nba_data)

# Visualize the analyzed data
visualised_data = visualise_data(anal_data)

# Optionally, you can print or save the final data with analysis and visualization modifications
print("Final Data with Analysis and Visualisation:")
print(visualised_data)
