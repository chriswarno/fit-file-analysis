from garmin_fit_sdk import Decoder, Stream
import streamlit as st

from io import BufferedReader


@st.cache_data
def messages(file):
    '''
    # elif statement to get the stream depending on how the file data was sent to the function
    if isinstance(file, str): # if a file path is provided
        stream = Stream.from_file(file)
        print("file path")
    elif isinstance(file, bytearray): # if a bytearray is provided
        stream = Stream.from_byte_array(file)
        print("bytearray")
    elif isinstance(file, bytes): # if a bytesIO object was provided
        stream = Stream.from_bytes_io(file)
        print("bytesio")
    else: # hopefully this works
        stream = Stream.from_buffered_reader(file)
        print("BufferedReader")
    '''
    stream = Stream.from_byte_array(file)
        
    try:
        st.write(stream)
        
        decoder = Decoder(stream)  # Decoder object to decode the stream

        messages, errors = decoder.read(  # Read the fit file to a dict
            convert_datetimes_to_dates=True,
        )

        st.write(messages)

        if errors:  # If there are errors in decoding the file, error message is returned
            e = "There were errors in decoding the file"
            return e
        else:
            return messages  # If no errors are found, the decoded file is returned as a dict
    except Exception as e:
        st.error(f"An error occurred: {e}")
        return "Please enter a valid .fit file"