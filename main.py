import streamlit as st

import utils

def main():
    st.title("Fit File Analysis")

    file = st.file_uploader("Upload a .fit file", type=["fit"])

    contents = file.read()

    messages = utils.messages(contents)

    df = utils.fit_df(messages)

    st.dataframe(df)
    st.line_chart(
        df,
        x="timestamp",
        y=["heart_rate", "power", "cadence"],
        color=["#FF0000","#0000FF", "#00FF00"]
        )


if __name__ == "__main__":
    main()