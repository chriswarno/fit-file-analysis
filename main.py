from typing import Annotated
from fastapi import FastAPI, File, UploadFile
from garmin_fit_sdk import Decoder, Stream
import tempfile
import os

app = FastAPI()

@app.post("/uploadfile/")
async def upload_file(file: Annotated[UploadFile, File()]):
    # Ensure the uploaded file is a .fit file
    if file.filename.endswith(".fit"):
        with tempfile.TemporaryDirectory() as uploads:
            # Create the full path for the uploaded file
            path = os.path.join(uploads, file.filename)

            # Save the uploaded file to the temporary directory
        content = await file.read()  # Read the file content
        with open(path, "wb") as temp_file:
            temp_file.write(content)  # Write the file content to the temp file
            
            # Process the file with garmin_fit_sdk
        stream = Stream.from_file(path)
        decoder = Decoder(stream)
        messages, errors = decoder.read()

        # Return results
        return {"errors": errors, "messages": messages}
    else:
        return {"error": "Uploaded file is not a .fit file"}

if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app, host="127.0.0.1", port=8000)
