# Project name is ism2411-data-cleaning-copilot
#The purpose of this code is to clean a given data set by handling the missing values,
# integrating colum names, removing white spaces, and finally saving the processed data to a new file. 
import pandas as pd

# Step #1 is to load the data function
def load_data(file_path: str) -> pd.DataFrame:
#Here I am loading the sales data from the CSV file.
    df = pd.read_csv(file_path)
    return df

# Step #2 is to implement the fuctions using Copilot. 
#Here I am using Copilot AI to give me suggestions
#on different functions the code will use. 
# The first function I will create is to clean the column names. The purpose of this is to change column headers into the standardized form.
#White space at the front or back of column names will also be removed. 
def clean_column_names(df: pd.DataFrame) -> pd.DataFrame:
# Convert the column names to lowercase and replace spaces with underscores.
#Copilot suggested: df.columns.str.lower().str.replace(' ', '_').str.strip()
    new_cols = df.columns.str.lower().str.strip().str.replace(' ', '_')
    df.columns = new_cols
    return df 
#The first modification to copilots suggestion was to introduce a temporary variable called "new_cols" which holds the changed column names. 


# the next step is to handle missing values, and clean up the text. 
def handle_missing_values(df: pd.DataFrame) -> pd.DataFrame:
# I need a function that fills a missing price or quantity with 0.0 and strips white space from the front or back of the data, as well as quotations
#handle missing values:
    df['price'].fillna(0.0, inplace=True)
    df['qty'].fillna(0, inplace=True)

    #convert columns to numeric
    df['price'] = pd.to_numeric(df['price'], errors='coerce') 
    df['qty'] = pd.to_numeric(df['qty'], errors='coerce').astype('Int64')

#now I strip white space 
    df['prodname'] = df['prodname'].str.lower().str.strip()
    df['category'] = df['category'].str.strip().str.lower().str.replace('"', '')
    return df

#The next function will be to remove any invalid rows. 
def remove_invalid_rows(df: pd.DataFrame) -> pd.DataFrame:
# any rows that have a price which is negative will be removed, and qty must be positive. 
# copilot's suggestion: df = df[(df['price'] >= 0) & (df['qty'] > 0)]
# I will modify this function to change the structure from boolean, to the query method. 
    df = df.query('price >= 0 and qty > 0').dropna(subset=['price', 'qty'])
    return df 
#my second change was to add the dropna method to remove any rows that have missing values in the price or qty columns.


#now I have to make the code give the finalized, cleaned data output and then save it as its own file. 
#this is the block given on the canvas assignment:

if __name__ == "__main__":
    raw_path = "data/raw/sales_data_raw.csv"
    cleaned_path = "data/processed/sales_data_clean.csv"

    df_raw = load_data(raw_path)
    df_clean = clean_column_names(df_raw)
    df_clean = handle_missing_values(df_clean)
    df_clean = remove_invalid_rows(df_clean)
    df_clean.to_csv(cleaned_path, index=False)
    print("Cleaning complete. First few rows:")
    print(df_clean.head())



