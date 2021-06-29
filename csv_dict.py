import pandas as pd
import csv
from pathlib import Path
def path(csv_file):
    if Path(csv_file).is_file():
        return True
    else:
        return False


def empty(csv_file):
    df = pd.read_csv(csv_file)
    return df.empty
def csv_as_dict(csv_file):
    dict_from_csv = pd.read_csv(csv_file, header=None, index_col=0, squeeze=True).to_dict()
    print(dict_from_csv)