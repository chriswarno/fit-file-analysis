from typing import Annotated
from fastapi import FastAPI, File, UploadFile
from garmin_fit_sdk import Decoder, Stream

app = FastAPI()


@app.post("/uploadfile/")
async def upload_file(file: Annotated[UploadFile, File()]):
    # Ensure the uploaded file is a .fit file
    if file.filename.endswith(".fit"):
        # Read the file content as a stream
        file_content = await file.read()
        stream = Stream.from_file(file_content)  # Use from_bytes for the in-memory content

        # Check if the stream is a valid .fit file
        is_fit = Decoder.is_fit(stream)
        return {"filename": file.filename, "is_fit": is_fit}
    
    return {"error": "Uploaded file is not a .fit file"}


if __name__ == "__main__":
    import uvicorn

    uvicorn.run(app, host="127.0.0.1", port=8000)
