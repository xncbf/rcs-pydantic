from fastapi import FastAPI

from rcs_pydantic import SendInfo

app = FastAPI()


@app.post("/")
def read_root(request, payload: SendInfo):
    return {"Hello": "World"}


def test_openapi():
    assert app.openapi()
