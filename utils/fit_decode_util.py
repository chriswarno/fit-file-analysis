from garmin_fit_sdk import Decoder, Stream, Profile


file = str # Variable to hold the file path

def constr(file):
    stream = Stream.from_bytes_io(file)
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


