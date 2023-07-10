import pandas as pd
import numpy as np
from scipy.stats import skew

# load the CSV file
input_file = "/kaggle/input/datacleaner/input.csv"
chunk_size = 1000000  # adjust this based on available memory
reader = pd.read_csv(input_file, chunksize=chunk_size)
data = pd.concat([chunk for chunk in reader])


# Write the cleaning summary to a text file
with open('cleaning_summary.txt', 'w') as f:
    f.write("Data cleaning summary:\n\n")

# handling missing values
skewness = skew(data.select_dtypes(include=np.number), axis=0, nan_policy='omit')
for i, col in enumerate(data.columns):
    if data[col].isnull().sum() > 0:
        if data[col].dtype == 'object':
            data[col].fillna(data[col].mode()[0], inplace=True)  # if categorical, fill with mode
            with open('cleaning_summary.txt', 'a') as f:
                f.write(f"Missing data filled with mode for column {col}.\n")
        elif skewness[i] < -1:
            data[col].fillna(data[col].median(), inplace=True)  # if highly left-skewed, fill with median
            with open('cleaning_summary.txt', 'a') as f:
                f.write(f"Missing data filled with median for highly left-skewed column {col}.\n")
        elif skewness[i] > 1:
            data[col].fillna(data[col].median(), inplace=True)  # if highly right-skewed, fill with median
            with open('cleaning_summary.txt', 'a') as f:
                f.write(f"Missing data filled with median for highly right-skewed column {col}.\n")
        else:
            data[col].fillna(data[col].mode()[0], inplace=True)  # if approximately symmetrical, fill with mode
            with open('cleaning_summary.txt', 'a') as f:
                f.write(f"Missing data filled with mode for approximately symmetrical column {col}.\n")
    else:
        with open('cleaning_summary.txt', 'a') as f:
            f.write(f"No missing data in column {col}.\n")


# handling outliers
for col in data.select_dtypes(include=np.number).columns:
    Q1 = data[col].quantile(0.25)
    Q3 = data[col].quantile(0.75)
    IQR = Q3 - Q1
    outliers = ((data[col] < (Q1 - 1.5 * IQR)) | (data[col] > (Q3 + 1.5 * IQR)))
    if outliers.any():
            data.loc[outliers, col] = np.nan
            fill_value = data[col].mean()  # use mean to fill in missing values after outlier treatment
            data[col].fillna(fill_value, inplace=True)
            with open('cleaning_summary.txt', 'a') as f:
                f.write(f"Outliers removed and missing data filled with mean for column {col}.\n")
    else:
            with open('cleaning_summary.txt', 'a') as f:
                f.write(f"No outliers and no missing data in column {col}.\n")

# handling duplicated data
duplicated_rows = data.duplicated()
if duplicated_rows.any():
    data = data[~duplicated_rows]
    with open('cleaning_summary.txt', 'a') as f:
        f.write("Duplicate rows removed.\n")
else:
    with open('cleaning_summary.txt', 'a') as f:
        f.write("No duplicated rows found.\n")

# save the cleaned data as a CSV file
output_file = "output_file.csv"
data.to_csv(output_file, index=False)

