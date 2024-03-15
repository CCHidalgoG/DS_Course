import numpy as np
import pandas as pd

GLOBAL_PATH = '/home/chidalgo/git/DS_Course'
DATA_PATH = f'{GLOBAL_PATH}/data/'

def get_numeric_all(data):
    return [x for x in data.columns if pd.Series(data.dtypes[x]).isin([np.float64, np.int64]).all()]

def get_numeric(data):
    return [x for x in data.columns if data[x].dtype == np.float64]


def get_numeric_2(data):
    numericas = list()
    for col in data.columns:
        if data.dtypes[col] == np.float64:
            numericas.append(col)
    return numericas