from Model import UsuarioEntenty, UsuarioRepository


def buscarUsuarios():
    return UsuarioRepository.getUsers()


def buscarUsuario(id: int):
    return UsuarioRepository.getById(id)


def salvar(user: UsuarioEntenty.Usuario):
    if user is None:
        return {'Usuario': 'Nao pode ser vazio'}
    return UsuarioRepository.save(user)


def atualizar(user : UsuarioEntenty.Usuario):
    if user is None:
        return {'Usuario': 'Nao pode ser vazio'}
    return UsuarioRepository.update(user)


def deletar(id : int):
    if id is None:
        return {'Usuario': 'Nao pode ser vazio'}
    return UsuarioRepository.delete(id)
