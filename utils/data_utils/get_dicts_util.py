import streamlit as st

@st.cache_data
def record_mesgs(messages):
    data = messages
    record_mesgs = []

    for n in data["record_mesgs"]:
        record = n
        record_mesgs.append(record)

    return record_mesgs



def hr_zones(messages):
    data = messages
    hr_zones = []

    for n in data["hr_zone_mesgs"]:
        hr_zone = n
        hr_zones.append(hr_zone)

    return hr_zones


def power_zones(messages):
    data = messages
    power_zones = []

    for n in data["power_zone_mesgs"]:
        power_zone = n
        power_zones.append(power_zone)

    return power_zones


def lap_mesgs(messages):
    data = messages
    lap_mesgs = []

    for n in data["lap_mesgs"]:
        lap_mesg = n
        lap_mesgs.append(lap_mesg)

    return lap_mesgs


def session_mesgs(messages):
    data = messages
    session_mesgs = []

    for n in data["session_mesgs"]:
        session_mesg = n
        session_mesgs.append(session_mesg)

    return session_mesgs
