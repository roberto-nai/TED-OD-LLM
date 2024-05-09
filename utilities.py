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


def read_csv_data_to_df(path: str, col_type: dict, csv_sep: str = ",") -> pd.DataFrame:
    """
    Reads data from a CSV file into a pandas DataFrame with specified columns and data types.

    Parameters:
        path (str): the file path to the CSV file to be read.
        col_type (dict): a dictionary of column names and type.
        sep (str): the delimiter string used in the CSV file. Defaults to ';'.

    Returns:
        pd.DataFrame: a pandas DataFrame containing the data read from the CSV file.
    """
    df = None
    if col_type is None:
        df = pd.read_csv(path, sep=csv_sep, low_memory=False)
    else:
        df = pd.read_csv(path, dtype=col_type, sep=csv_sep, low_memory=False)
    df = df.drop_duplicates()
    return df

