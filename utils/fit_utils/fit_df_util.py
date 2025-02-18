import pandas as pd
import streamlit as st


def df_head(data):
    header = []
    head_data = data["record_mesgs"][-1].keys()
    for i in head_data:
        header.append(i)

    print(header)
    return header


def df_body(data, header):
    body = []

    for n in data["record_mesgs"]:
        record = {key: n.get(key, None) for key in header}
        body.append(record)

    #body.append(data)
    return body


@st.cache_data
def fit_df(messages):
    data = messages

    head = df_head(data)
    body = df_body(data)    

    df = pd.DataFrame(data=body, columns=head)

    return df