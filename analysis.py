# analysis.py
import pandas as pd

def perform_data_analysis(data):
    # Step 1: Inspect data
    print("Data Overview:")
    print(data.head())

    # Step 2: Check for missing values
    print("\nMissing Values:")
    print(data.isnull().sum())

    # Step 3: Handle missing values (if any)
    data = data.dropna()

    # Step 4: Check for duplicates
    print("\nDuplicate Records:")
    print(data.duplicated().sum())

    # Step 5: Remove duplicates (if any)
    data = data.drop_duplicates()

    # Step 6: Basic statistics for numerical columns
    print("\nBasic Statistics:")
    print(data.describe())

    # Step 7: Explore categorical data
    print("\nCategorical Data Overview:")
    print(data['Position'].value_counts())
    print(data['Team'].value_counts())

    # Example: Performance index calculation
    data['PerformanceIndex'] = (
        0.4 * data['PTS'] +
        0.3 * data['Total Minutes'] +
        0.2 * (1 / data['TOV']) +
        0.1 * data['Salary']
    )

    # Example: Rank players based on PerformanceIndex
    data['Rank'] = data['PerformanceIndex'].rank(ascending=False)

    return data

# Load data from a CSV file
file_path = 'nba_stats.csv'
nba_data = pd.read_csv(file_path)

# Perform data analysis
anal_data = perform_data_analysis(nba_data)

# Optionally, you can print or save the final data with analysis modifications
print("Final Data with Analysis:")
print(anal_data)
