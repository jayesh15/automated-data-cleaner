# automated-data-cleaner
This algorithm is designed to clean and preprocess a large dataset in order to prepare it for further analysis. The algorithm is written in Python.

## Author:
- [Jayesh Jain](https://github.com/jayesh15)

## Inputs
The algorithm takes a single input, which is a CSV file containing the raw data to be cleaned. The file must be formatted correctly and should not contain any missing values. The path to the input file is specified using the input_file variable at the top of the script.

## Outputs
The algorithm produces two output files:

### cleaned_data.csv:
This file contains the cleaned data, with missing values, outliers, and duplicated rows removed.

### cleaning_summary.txt:
This file contains a summary of the cleaning operations performed on the data.

## Cleaning Operations
The algorithm performs the following cleaning operations on the input data:

### Handling Missing Values
Missing values are handled using the following strategy:

- For categorical columns, missing values are filled with the mode of the column.
- For numerical columns that are highly left-skewed, missing values are filled with the median of the column.
- For numerical columns that are highly right-skewed, missing values are filled with the median of the column.
- For numerical columns that are approximately symmetrical, missing values are filled with the mode of the column.

The cleaning summary file (cleaning_summary.txt) contains a log of which columns had missing values and how they were handled.

### Handling Outliers
Outliers are handled using the following strategy:

- For each numerical column, outliers are identified using the interquartile range (IQR) method.
- Outliers are replaced with NaN values.
- Missing values are filled using the mean of the column.

The cleaning summary file (cleaning_summary.txt) contains a log of which columns had outliers and how they were handled.

### Handling Duplicated Rows
Duplicated rows are handled as follows:

- Duplicated rows are identified and removed from the dataset.

The cleaning summary file (cleaning_summary.txt) contains a log indicating whether duplicated rows were found and removed.

## Running the Algorithm
To run the algorithm, execute the script in a Python environment. The required dependencies are specified at the top of the script. The input file path can be adjusted using the input_file variable.

## Note: If the input file is very large, the chunk_size variable can be adjusted to process the data in smaller chunks and reduce memory usage. Alternatively try dask

## Conclusion
This algorithm provides a reliable and consistent way to clean and preprocess large datasets, ensuring that the data is ready for further analysis.
