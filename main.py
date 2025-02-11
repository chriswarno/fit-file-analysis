import streamlit as st

import utils

st.title("Fit File Analysis")

file = st.file_uploader("Upload a .fit file", type=["fit"])

record_fields = utils.constr(file)

csv_head = utils.csv_head(record_fields)

st.write(csv_head)