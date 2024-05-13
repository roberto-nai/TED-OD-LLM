### IMPORT ###
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
        print("Reading CSV without col_type...")
        df = pd.read_csv(filepath_or_buffer = path_csv, sep=csv_sep, low_memory=False)
    else:
        print("Reading CSV with col_type...")
        df = pd.read_csv(filepath_or_buffer = path_csv, sep=csv_sep, dtype=col_type, low_memory=False)
    df = df.drop_duplicates()
    return df

