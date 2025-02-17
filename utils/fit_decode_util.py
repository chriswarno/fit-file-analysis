from garmin_fit_sdk import Decoder, Stream, Profile


file = str # Variable to hold the file path

def fields(file):
    stream = Stream.from_byte_array(file)
    #print(f"Stream: {stream}")

    record_fields = set()
    def mesg_listener(mesg_num, message):
        if mesg_num == Profile['mesg_num']['RECORD']:
            for field in message:
                record_fields.add(field)

    try:
        decoder = Decoder(stream)
        #print = (f"Decoder: {decoder}")

        messages, errors = decoder.read(
            mesg_listener = mesg_listener,
            convert_datetimes_to_dates = True,
        )
        #print(f"Messages: {messages}")
        #print(f"Errors: {errors}")

        #return messages
        return record_fields
    except Exception as e:
        e =  "Please enter a valid .fit file"
        return e
    

def data(file):
    stream = Stream.from_byte_array(file)
    #print(f"Stream: {stream}")

    record_data = set()
    def mesg_listener(mesg_num, message):
        if mesg_num == Profile['mesg_num']['RECORD']:
            for message in record_mesgs:
                record_data.add(message)

    try:
        decoder = Decoder(stream)
        #print = (f"Decoder: {decoder}")

        messages, errors = decoder.read(
            mesg_listener = mesg_listener,
            convert_datetimes_to_dates = True,
        )
        #print(f"Messages: {messages}")
        #print(f"Errors: {errors}")

        #return messages
        return record_data
    except Exception as e:
        e =  "Please enter a valid .fit file"
        return e


# function to get all messages for debugging
def messages(file):
    stream = Stream.from_byte_array(file)
    #print(f"Stream: {stream}")

    try:
        decoder = Decoder(stream)
        #print = (f"Decoder: {decoder}")

        messages, errors = decoder.read(
            convert_datetimes_to_dates = True,
        )
        #print(f"Messages: {messages}")
        #print(f"Errors: {errors}")

        return messages
    except Exception as e:
        e =  "Please enter a valid .fit file"
        return e