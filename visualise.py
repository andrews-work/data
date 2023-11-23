#
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

def visualise_data(data):
    # Step 8: Identify outliers
    # Example: Using pair plot for selected numerical columns
    selected_columns = ['PTS', 'Total Minutes', 'TOV', 'Salary']
    sns.pairplot(data[selected_columns])
    plt.suptitle('Pair Plot of Points, Total Minutes, Turnovers, and Salary', y=1.02)
    plt.show()

    # Example: Performance index calculation
    data['PerformanceIndex'] = (
        0.4 * data['PTS'] +
        0.3 * data['Total Minutes'] +
        0.2 * (1 / data['TOV']) +  # Inverse of turnovers to penalize high turnovers
        0.1 * data['Salary']
    )
    
    # Example: Rank players based on PerformanceIndex
    data['Rank'] = data['PerformanceIndex'].rank(ascending=False)

    return data

if __name__ == "__main__":
    # Load data from a CSV file
    file_path = 'nba_stats.csv'
    nba_data = pd.read_csv(file_path)

    # Perform data visualization
    visualise_data(nba_data)
