from typing import Optional
from Model import UsuarioService
from fastapi import FastAPI

app = FastAPI()

@app.get("/usuarios")
async def root():
    usuarios = UsuarioService.buscarUsuarios()
    return {"Usuarios": usuarios}


@app.get("/usuarios/{id}")
async def say_hello(id: int):
    usuario = UsuarioService.buscarUsuario(id)
    return {"Usuario": usuario}
