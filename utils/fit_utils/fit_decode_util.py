from garmin_fit_sdk import Decoder, Stream


def messages(file):
    stream = Stream.from_byte_array(file) # Stream object to decode the file

    try:
        decoder = Decoder(stream) # Decoder object to decode the stream

        messages, errors = decoder.read( # Read the fit file to a dict
            convert_datetimes_to_dates = True,
        )

        if errors > 0: # If there are errors in decoding the file, error message is returned
            e = "There were errors in decoding the file"
            return e
        else:
            return messages # If no errors are found, the decoded file is returned as a dict
    except Exception as e:
        e =  "Please enter a valid .fit file"
        return e