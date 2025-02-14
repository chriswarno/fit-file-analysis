import pandas as pd
import numpy as np
from pandas import DataFrame

header = []
body = []

df = pd.DataFrame(np.array([body]),
                  columns=[header])

def df_head(record_fields):
    header.append(record_fields)
    return header


def csv_body(record_data):
    body.append(record_data)
    return body