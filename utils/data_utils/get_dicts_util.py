import streamlit as st

@st.cache_data
def record_mesgs(messages): # function to get record messages from the decoded file
    data = messages # data = messages from the decoded file
    record_mesgs = [] # empty list to hold record messages

    for n in data["record_mesgs"]: # loop to iterate through the record messages, and append them to record_mesgs list
        record = n
        record_mesgs.append(record)

    return record_mesgs # return record_mesgs list



def hr_zones(messages): # function to get heart rate zones from the decoded file
    data = messages # data = messages from the decoded file
    hr_zones = []

    for n in data["hr_zone_mesgs"]: # loop to iterate through the heart rate zone messages, and append them to hr_zones list
        hr_zone = n
        hr_zones.append(hr_zone)

    return hr_zones # return hr_zones list


def power_zones(messages): # function to get power zones from the decoded file
    data = messages # data = messages from the decoded file
    power_zones = []

    for n in data["power_zone_mesgs"]: # loop to iterate through the power zone messages, and append them to power_zones list
        power_zone = n
        power_zones.append(power_zone)

    return power_zones # return power_zones list


def lap_mesgs(messages): # function to get lap messages from the decoded file
    data = messages # data = messages from the decoded file
    lap_mesgs = []

    for n in data["lap_mesgs"]: # loop to iterate through the lap messages, and append them to lap_mesgs list
        lap_mesg = n
        lap_mesgs.append(lap_mesg)

    return lap_mesgs # return lap_mesgs list


def session_mesgs(messages): # function to get session messages from the decoded file
    data = messages # data = messages from the decoded file
    session_mesgs = []

    for n in data["session_mesgs"]: # loop to iterate through the session messages, and append them to session_mesgs list
        session_mesg = n
        session_mesgs.append(session_mesg)

    return session_mesgs # return session_mesgs list
