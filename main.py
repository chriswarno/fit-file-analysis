from typing import Annotated
from fastapi import FastAPI, File, UploadFile, HTTPException
from garmin_fit_sdk import Decoder, Stream
import python_multipart
import aiofiles

app = FastAPI()

@app.post("/uploadfile/")
async def upload_file(file: Annotated[UploadFile, File()]):
    # Ensure the uploaded file is a .fit file
    if file.filename.endswith(".fit"):
        with open(file.filename, 'wb') as f:
            while contents := file.file.read(1024 * 1024):
                f.write(contents)

        # Process the file with garmin_fit_sdk
        stream = Stream.from_byte_array(contents)
        decoder = Decoder(stream)
        messages, errors = decoder.read()

        # Return results
        return {"errors": errors, "messages": messages}
    else:
        return {"error": "Uploaded file is not a .fit file"}

if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app, host="127.0.0.1", port=8000)
