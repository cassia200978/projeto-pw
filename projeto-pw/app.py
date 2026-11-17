from http import HTTPStatus

from fastapi import FastAPI

from schemas import Message, CompromissoSchema

app = FastAPI()


@app.get("/")
def read_root():
    return {"message": "Olá Mundo!"}


@app.post(
    "/compromissos",
    status_code=HTTPStatus.CREATED,
    response_model=CompromissoSchema,
)
def criar_compromisso(compromisso: CompromissoSchema):
    return compromisso