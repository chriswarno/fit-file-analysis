import pandas as pd
import streamlit as st

from datetime import timedelta

class RideData:
    def __init__(self, total_time, ride_time, avg_speed, max_speed, avg_cadence, max_cadence, min_hr, max_hr, avg_hr, time_in_hr_zone, time_in_pwr_zone, avg_pwr, max_pwr):
        pass

def ride_data(session_mesgs):
    session_mesgs = session_mesgs

    data = {
        "total_time": ""
        "ride_time"
    }

    #total_time_seconds = data[0]["total_elapsed_time"]
    total_time = str(timedelta(seconds=session_mesgs[0]["total_elapsed_time"]))
    data.append(total_time)
    st.write(total_time)

    #ride