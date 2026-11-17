from pydantic import BaseModel


class Message(BaseModel):
    message: str


class CompromissoSchema(BaseModel):
    titulo: str
    data: str
    horario: str
    descricao: str | None = None