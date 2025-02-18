import pandas as pd
import streamlit as st

from .get_dicts_util import record_mesgs, hr_zones, power_zones, lap_mesgs, session_mesgs

@st.cache_data
def records_df(messages): # function to create a dataframe from the record messages
    data = record_mesgs(messages) # data = list of record messages

    head = [] # empty list to hold the column names
    body = [] # empty list to hold the data

    head_data = data[-1].keys()
    for n in head_data:
        head.append(n)

    for value in data:
        body.append(value)

    df = pd.DataFrame(data=body, columns=head)

    return df # return dataframe of record messages