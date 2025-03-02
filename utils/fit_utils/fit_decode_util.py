from garmin_fit_sdk import Decoder, Stream
import streamlit as st


@st.cache_data
def messages(file):
    '''
    match file:
        case (type(file) === str):
            stream = Stream.from_file(file)
            return stream
        case type(file) === bytearray:
            stream = Stream.from_byte_array
            return stream
        case type(file) === bytes:
            stream = Stream.from_byte_io
            return stream
        case type(file) === 
    '''
    if isinstance(file, str):
        stream = Stream.from_file(file)
        return stream
    elif isinstance(file, bytearray):
        stream = Stream.from_byte_array(file)
        return stream
    elif isinstance(file, bytes):
        stream = Stream.from_byte_io
        return stream
    elif isinstance(file, )


    try:
        stream = Stream.from_byte_array(file)  # Stream object to decode the file
        st.write(stream)
        
        decoder = Decoder(stream)  # Decoder object to decode the stream

        messages, errors = decoder.read(  # Read the fit file to a dict
            convert_datetimes_to_dates=True,
        )

        if errors:  # If there are errors in decoding the file, error message is returned
            e = "There were errors in decoding the file"
            return e
        else:
            return messages  # If no errors are found, the decoded file is returned as a dict
    except Exception as e:
        st.error(f"An error occurred: {e}")
        return "Please enter a valid .fit file"