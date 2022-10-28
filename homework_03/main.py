from fastapi import FastAPI
from starlette import status
from starlette.responses import JSONResponse

app = FastAPI()


@app.get("/")
def read_root():
    return {"message": "hello world"}


@app.get("/ping/")
def get_ping():
    return {"message": "pong"}


@app.exception_handler(status.HTTP_404_NOT_FOUND)
async def custom_404_handler(request, exception):
    return JSONResponse(
        {
            "request_url": request.url.path,
            "exception": str(exception)
        },
        status_code=status.HTTP_404_NOT_FOUND,
    )
