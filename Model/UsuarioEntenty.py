from pydantic import BaseModel

class Usuario(BaseModel):
    user_id: int
    dt_nascimento: str
    nome: str
    user_cpf: str
