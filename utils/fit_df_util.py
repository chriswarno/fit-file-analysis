import pandas as pd
import numpy as np
from pandas import DataFrame

def df_head(fields):
    header = []
    header.append(fields)
    return header


def df_body(data):
    body = []
    body.append(data)
    return body


def fit_df(record_fields, record_data):
    fields = record_fields
    data = record_data

    header = df_head(fields)
    body = df_body(data)
    

    df = pd.DataFrame(data=body, columns=header)

    return df