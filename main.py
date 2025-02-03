from typing import Annotated
from fastapi import FastAPI, File, UploadFile, HTTPException
from fastapi.responses import FileResponse
from garmin_fit_sdk import Decoder, Stream, Profile
import python_multipart
import aiofiles
import json
from datetime import datetime
import tempfile

app = FastAPI()

# data_file = tempfile.NamedTemporaryFile()

@app.get("/")
def read_root():
    return {"Hello": "World"}

@app.post("/upload_file/")
async def upload_file(file: Annotated[UploadFile, File()]):
    # Ensure the uploaded file is a .fit file
    if file.filename.endswith(".fit"):
        file_location = f"/tmp/{file.filename}"
        async with aiofiles.open(file_location, 'wb') as f:
            while chunk := await file.read(1024):
                await f.write(chunk)

        result = await decode_file(file_location)
        #async with aiofiles.open(data_file.name, 'w') as f:
            #await f.write(result)
        
        # Return results
        return result
    else:
        return {"error": "Uploaded file is not a .fit file"}
    

record_fields = set()
record_data = set()
async def decode_file(file_location: str):
    async with aiofiles.open(file_location, 'rb') as f:
        print(f"Decoding file: {file_location}")

        stream = await stream_file(f, file_location)
        print(f"Stream: {stream}")

        decoder = decode(stream)
        print(f"Decoder: {decoder}")

        
        print(f"Record Fields: {record_fields}")

        try:
            messages, errors = decoder.read(
                mesg_listener = mesg_listener,
                convert_datetimes_to_dates = True,
            )
            #print(f"Messages: {messages}")
            print(f"Errors: {errors}")
            print(f"Record Fields: {record_fields}")
            print(f"Record Data: {record_data}")
            csv = parse_to_csv(messages)
        except Exception as e:
            print(f"Error during decoding: {e}")
            return {"error": "Failed to decode file"}

    return csv


async def stream_file(f, file_location: str):
    file_contents = await f.read()
    stream = Stream.from_byte_array(file_contents)
    print(f"Stream created from file: {file_location}")
    return stream


def decode(stream):
    decoder = Decoder(stream)
    print(f"Decoder created with stream: {stream}")
    return decoder


def mesg_listener(mesg_num, message):
    if mesg_num == Profile['mesg_num']['RECORD']:
        for field in message:
            record_fields.add(field)
            
        for field in message:
            record_data.add(message[field])


def parse_to_csv ():
    data = [
        [record_fields]
        #[]
    ]

    
    return data


'''
async def decode_file(file_location: str):
    # Process the file with garmin_fit_sdk
    with open(file_location, 'rb') as f:
        stream = Stream.from_buffered_reader(f)
        decoder = Decoder(stream)
        messages, errors = decoder.read()

        print(f"Messages: {messages}")


    return messages
'''



if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app, host="127.0.0.1", port=8000)