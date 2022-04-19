from Model import UsuarioEntenty
from Repository import UsuarioRepository


def buscarUsuarios():
    return UsuarioRepository.getUsers()


def buscarUsuario(id: int):
    return UsuarioRepository.getById(id)


def salvar(user: UsuarioEntenty.Usuario):
    if user is None:
        return {'Usuario': 'Nao pode ser vazio'}

    usuario = buscarUsuario(user.user_id)
    if usuario != []:
        return {'Usuario': 'Esse id ja foi cadastrado.'}
    return UsuarioRepository.save(user)


def atualizar(user : UsuarioEntenty.Usuario):
    if user is None:
        return {'Usuario': 'Nao pode ser vazio'}
    usuario = buscarUsuario(user.user_id)
    if usuario == []:
        return {'Usuario': 'Esse id nao existe.'}
    return UsuarioRepository.update(user)


def deletar(id : int):
    if id is None:
        return {'Usuario': 'Nao pode ser vazio'}
    usuario = buscarUsuario(id)
    if usuario == []:
        return {'Usuario': 'Esse id nao existe.'}
    return UsuarioRepository.delete(id)
