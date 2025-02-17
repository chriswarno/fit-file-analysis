import streamlit as st

import utils

st.title("Fit File Analysis")

file = st.file_uploader("Upload a .fit file", type=["fit"])

contents = file.read()

record_fields = utils.fields(contents)
record_data = utils.data(contents)

messages = utils.messages(contents)

st.write("Record Fields:", record_fields)
st.write("Record Data:", record_data)
st.write("Messages:", messages)

df = utils.fit_df(record_fields, record_data)

st.dataframe(df)
st.write(df)