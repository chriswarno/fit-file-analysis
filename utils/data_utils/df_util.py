import pandas as pd

from .get_dicts_util import record_mesgs, hr_zones, power_zones, lap_mesgs, session_mesgs

def records_df(messages):
    data = record_mesgs(messages)

    head = []
    body = []

    head_data = data[-1].keys()
    for n in head_data:
        head.append(n)

    for value in data:
        body.append(value)

    df = pd.DataFrame(data=body, columns=head)

    return df

