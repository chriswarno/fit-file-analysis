from typing import Annotated
from fastapi import FastAPI, File, UploadFile
from fastapi.responses import FileResponse
from garmin_fit_sdk import Decoder, Stream
import tempfile
import os

app = FastAPI()

uploads = tempfile.TemporaryDirectory()  # Temporary directory to store uploaded files


@app.post("/uploadfile/")
async def upload_file(file: Annotated[UploadFile, File()]):
    # Ensure the uploaded file is a .fit file
    if file.filename.endswith(".fit"):
        upload_directory = uploads.name
        file_path = os.path.join(upload_directory, file.filename)

        with open(file_path, "wb") as temp_file:
            temp_file.write(await file.read())

        uploaded_file = file_path
        stream = Stream.from_file(uploaded_file)
        decoder = Decoder(stream)
        messages, errors = decoder.read()

        return {"errors": errors, "messages": messages}
    
    return {"error": "Uploaded file is not a .fit file"}


if __name__ == "__main__":
    import uvicorn

    uvicorn.run(app, host="127.0.0.1", port=8000)
