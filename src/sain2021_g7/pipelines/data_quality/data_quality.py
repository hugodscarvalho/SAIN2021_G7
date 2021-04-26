import pandas as pd
import numpy as np

def data_quality(prodsales: pd.DataFrame) -> pd.DataFrame:
    """Node to create a data quality report. The parts of the report will include the 
    following analysis: Data type, Row Count, Missing Values, Unique Values and then 
    use the describe() function to find mean, standard deviation (std), minimum value, 
    maximum value, 25% (percentile), 50% (percentile) and  75% (percentile).

    Args:
        prodsales (pd.DataFrame): production and Sales data

    Returns:
        pd.DataFrame: Data quality report
    """
    #Create a DataFrame containing the data type of each column
    data_types = pd.DataFrame(prodsales.dtypes,columns=['Data Type'])
    #Create a DataFrame with the row count of each column
    row_count = pd.DataFrame(prodsales.count(),columns=['Row Count'])
    #Create a DataFrame with the count of missing values in each column
    missing_data_counts = pd.DataFrame(prodsales.isnull().sum(),columns=['Missing Values'])
    #Create a DataFrame with the count of unique values in each column
    unique_value_counts = pd.DataFrame(columns=['Unique Values'])
    for v in list(prodsales.columns.values):
        unique_value_counts.loc[v] = [prodsales[v].nunique()]
    unique_value_counts
    #Join DataFrames created above 
    data_quality_report = data_types.join(row_count).join(missing_data_counts).join(unique_value_counts)
    #Transpose the results provided by describe() to make the results more readable and store it in DataFrame sum_stats
    sum_stats = prodsales.describe().transpose()
    #Round sum_stats with 3 decimals.
    sum_stats = sum_stats.round(3)
    #Concatenate data_quality_report and sum_stats
    quality_report = pd.concat([data_quality_report, sum_stats], axis=1)
    #Replace all NaN to an empty string
    quality_report = quality_report.replace(np.nan, '', regex=True)
    #Drop 'count' column since it represents a duplication of 'Row Count' column
    quality_report.drop('count', axis=1, inplace=True)

    return quality_report