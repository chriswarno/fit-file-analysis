from typing import Annotated
from fastapi import FastAPI, File, UploadFile
from garmin_fit_sdk import Decoder, Stream


app = FastAPI()


@app.post("/uploadfile/")
async def fit_to_csv(file: Annotated[UploadFile, File()]):
    return {"filename":file.filename}


if __name__ == "__main__":
    import uvicorn

    uvicorn.run(app, host="127.0.0.1", port=8000)