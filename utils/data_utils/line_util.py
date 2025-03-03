import pandas as pd

def graph_subset(rdf):
    df = rdf # dataframe of record messages

    #df_subset = df.iloc[::50] # dataframe with every 50th record message
    df_cols = df[['timestamp', 'heart_rate', 'speed', 'cadence', 'power']]
    df_subset = df_cols[::10]

    return df_subset