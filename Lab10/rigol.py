import csv
import pandas as pd


def read_rigol_csv(csv_file_name):
    """
    Read the weird Rigol scope CSV format into something more easily parasable

    Args:
        csv_file_name: filepath to Rigol csv export

    Returns:
        data: a pandas dataframe with time & channel output variables
        t0: float representing starting time
        dT: float represetning
    """
    with open(csv_file_name) as f:
        rows = list(csv.reader(f))
        i = 0
        while rows[0][i] != "":
            i = i + 1
        numcols = i - 2
        t0 = float(rows[1][numcols])
        dT = float(rows[1][numcols + 1])
        data = pd.read_csv(csv_file_name, usecols=range(0, numcols), skiprows=[1])
        data["X"] = t0 + data["X"] * dT
    return data, t0, dT
