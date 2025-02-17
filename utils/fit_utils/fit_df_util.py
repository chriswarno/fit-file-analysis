import pandas as pd


def df_head(data):
    header = []
    head_data = data["record_mesgs"][0].keys()
    for i in head_data:
        header.append(i)
    return header


def df_body(data):
    body = []

    for n in data["record_mesgs"]:
        body.append(n)

    body.append(data)
    return body


def fit_df(messages):
    data = messages

    head = df_head(data)
    body = df_body(data)    

    df = pd.DataFrame(data=body, columns=head)

    return df