### IMPORT ###
import pathlib
from pathlib import Path
import pandas as pd

### FUNCTIONS ###

def list_files_by_type(directory: str, extension: str) -> list:
    """
    Returns a list of files with a given extension (case sensitive) in a specified directory, excluding temporary files.
    
    Args:
        directory (str): The path to the directory where to search for files.
        extension (str): The extension of the files to be searched for, including the dot (e.g., '.txt').
    
    Returns:
        list: List of Path objects for the found files, excluding temporary and hidden files.
    """

    file_list = []
    # Create a Path object from the directory
    dir_path = Path(directory)
    # Use the glob method to find all files with the given extension and filter out temporary files
    file_list = [file for file in dir_path.glob(f'*{extension}') if not file.name.startswith('.') and not file.name.startswith('~$')]
    return file_list

def list_subdirectories(directory: pathlib.PosixPath) -> list:
    """
    Returns a list of subdirectories contained within the specified directory, excluding hidden directories or system temporary directories.

    Parameters:
        directory (pathlib.PosixPath): The path to the directory to be scanned.

    Returns:
        list: A list of subdirectory names contained within the given directory, excluding hidden and system temporary directories.
    """

    # Force the type to PosixPath
    dir_path = Path(directory)

    # Check if the provided path is indeed a directory
    if not dir_path.is_dir():
        print(f"The provided path '{directory}' is not a valid directory.")
        return []

    # Define a set of common system temporary directory names to exclude
    system_temp_dirs = {'$RECYCLE.BIN', 'System Volume Information', 'Temporary Items', 'Trash', '.Trashes', 'tmp', 'Temp'}

    # Use a list comprehension to gather all directories, excluding hidden and system temporary ones
    subdirectories = [
        subdir.name for subdir in dir_path.iterdir() 
        if subdir.is_dir() and not subdir.name.startswith('.') and subdir.name not in system_temp_dirs
    ]

    return subdirectories

def read_csv_data_to_df(path_csv: str, col_type: dict, csv_sep: str = ",") -> pd.DataFrame:
    """
    Reads data from a CSV file into a pandas DataFrame with specified columns and data types.

    Parameters:
        path_csv (str): the file path to the CSV file to be read.
        col_type (dict): a dictionary of column names and type.
        csv_sep (str): the delimiter string used in the CSV file. Defaults to ';'.

    Returns:
        pd.DataFrame: a pandas DataFrame containing the data read from the CSV file.
    """
    df = None
    if col_type is None:
        print("Reading CSV without input without col_type...")
        df = pd.read_csv(filepath_or_buffer = path_csv, sep=csv_sep, low_memory=False)
    else:
        print(f"Reading CSV with input col_type: {col_type}")
        df = pd.read_csv(filepath_or_buffer = path_csv, sep=csv_sep, dtype=col_type, low_memory=False)
    df = df.drop_duplicates()
    return df

def convert_dmy_to_ymd(date_str:str) -> str:
    """
    Converts a date in the format dd/mm/yyyy to yyyyy-mm-dd.

    Args:
        date_str (str): Date in dd/mm/yyyy.

    Returns:
        str: date in yyyyy-mm-dd.
    """
    if date_str == "-1":
        return None
    else:
        # print("Converting:", date_str) # debug
        dt = pd.to_datetime(date_str, format='%d/%m/%Y').strftime('%Y-%m-%d')
        return dt

def left_join_df(df1: pd.DataFrame, df2: pd.DataFrame, key_column:str, columns_to_remove:list) -> pd.DataFrame:
    """
    Perform a left join on two dataframes based on the 'file_name' column,
    and remove the 'text' columns from both dataframes before joining.

    Parameters:
        df1 (pd.DataFrame): The first dataframe with columns 'file_name', 'case_id', 'text', and 'date'.
        df2 (pd.DataFrame): The second dataframe with columns 'file_name', 'text', and 'label'.
        key_column (str): The join column name.
        columns_to_remove (list): A list of column names to remove from both dataframes if they are present.

    Returns:
        pd.DataFrame: A new dataframe resulting from the left join on 'file_name', with the 'text' columns removed from both input dataframes.
    """
    # Drop 'columns_to_remove' columns from both dataframes
    df1 = df1.drop(columns=[col for col in columns_to_remove if col in df1], errors='ignore')
    df2 = df2.drop(columns=[col for col in columns_to_remove if col in df2], errors='ignore')

    # Perform left join on 'file_name'
    merged_df = pd.merge(df1, df2, on=key_column, how="left")

    return merged_df


def calculate_accuracy(df: pd.DataFrame, col1: str, col2: str) -> float:
    """
    Calculate the accuracy of matching 'col1' and 'col2' columns in a dataframe.

    Parameters:
        df (pd.DataFrame): The dataframe containing 'date' and 'label' columns.
        col1 (str): The name of the first column to compare.
        col2 (str): The name of the second column to compare.

    Returns:
        float: The accuracy as the proportion of rows where 'date' equals 'label'.
    """
    
    # print(f"Column type: {df[col1].dtype},{df[col2].dtype}") # debug (check colum type)

    # Calculate the number of matches
    matches = (df[col1] == df[col2]).sum()
    
    # Calculate the accuracy
    accuracy = matches / len(df)
    
    return accuracy