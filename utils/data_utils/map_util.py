from .df_util import records_df

def ride_map(messages):
    df = records_df(messages).filter(["position_lat", "position_long"])

    df_dropna = df.dropna()
    ndf = df_dropna.astype(float)
    
    return ndf