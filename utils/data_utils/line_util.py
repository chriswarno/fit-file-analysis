import pandas as pd

def graph_subset(rdf):
    df = rdf # dataframe of record messages

    df_subset = df.iloc[::50] # dataframe with every 50th record message

    return df_subset