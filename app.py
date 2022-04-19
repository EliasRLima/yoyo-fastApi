from Model import UsuarioEntenty
from Service import UsuarioService
from fastapi import FastAPI

app = FastAPI()

@app.get("/")
async def root():
    return {"Ola": "Bem vindo a app CRUD USUARIO"}

@app.get("/usuarios")
async def root():
    usuarios = UsuarioService.buscarUsuarios()
    return {"Usuarios": usuarios}


@app.get("/usuarios/{id}")
async def say_hello(id: int):
    usuario = UsuarioService.buscarUsuario(id)
    return {"Usuario": usuario}

@app.post('/create-usuario')
def create_user(user: UsuarioEntenty.Usuario):
    return UsuarioService.salvar(user)


@app.put('/update-usuario/')
def update_item(user: UsuarioEntenty.Usuario):
    return UsuarioService.atualizar(user)


@app.delete('/remove-usuario/{user_id}')
def update_item(user_id: int):
    return UsuarioService.deletar(user_id)
