import streamlit as st

import utils

def main():
    st.title("Fit File Analysis")

    file = st.file_uploader("Upload a .fit file", type=["fit"]) # Variable to hold the .fit file

    if file is None:
        st.info("Please upload a .fit file")
        return

    contents = file.read() # Variable to hold the contents of the .fit file

    messages = utils.messages(contents) # nested dictionary of all .fit file messages
    st.write(messages) # messages for debugging

    expander = st.expander("Ride Data") # expander to hold all ride data

    record_mesgs = utils.record_mesgs(messages) # dictionary of record messages
    expander.header("Record Messages")
    expander.write(record_mesgs)

    hr_zones = utils.hr_zones(messages) # dictionary of heart rate zones
    if hr_zones:
        expander.header("Heart Rate Zones")
        expander.write(hr_zones)

    power_zones = utils.power_zones(messages) # dictionary of power zones
    if power_zones:
        expander.header("Power Zones")
        expander.write(power_zones)

    lap_mesgs = utils.lap_mesgs(messages) # dictionary of lap messages
    expander.header("Lap Messages")
    expander.write(lap_mesgs)

    session_mesgs = utils.session_mesgs(messages) # dictionary of session messages
    expander.header("Session Messages")
    expander.write(session_mesgs)

    rdf = utils.records_df(messages) # dataframe of record messages
    rdf_subset = utils.graph_subset(rdf) # subset of record messages for graphing
    #ride_data = utils.ride_data(session_mesgs)

    st.dataframe(rdf_subset) # dataframe for debugging the graphing subset

    st.dataframe(rdf)
    st.line_chart( # line chart of heart rate, power, and cadence
        rdf_subset,
        x="timestamp",
        y=["heart_rate", "power", "cadence"],
        color=["#FF0000","#0000FF", "#00FF00"]
        )
    #st.bar_chart(
        #data= 
    #)
    
    '''
    map_data = utils.ride_map(messages)
    st.map(
        map_data,
        latitude="position_lat",
        longitude="position_long",
        zoom=12
        )
    '''


if __name__ == "__main__":
    main()