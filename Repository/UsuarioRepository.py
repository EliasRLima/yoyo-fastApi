import sqlalchemy as db
from sqlalchemy.orm import sessionmaker
from Model import UsuarioEntenty

engine = db.create_engine('postgresql+psycopg2://postgres:erl@localhost:5433/testdb')
connection = engine.connect()
Session = sessionmaker(engine)
session = Session()
metadata = db.MetaData()
usuarios = db.Table('usuarios', metadata, autoload=True, autoload_with=engine)

def getUsers():
    query = db.select([usuarios])
    ResultProxy = connection.execute(query)
    ResultSet = ResultProxy.fetchall()
    return ResultSet


def getById(id: int):
    query = db.select([usuarios]).where(usuarios.columns.user_id == id)
    ResultProxy = connection.execute(query)
    ResultSet = ResultProxy.fetchall()
    return ResultSet


def save(user: UsuarioEntenty.Usuario):
    query = db.insert(usuarios)
    value = [{'user_id': user.user_id, 'dt_nascimento': user.dt_nascimento, 'nome': user.nome, 'user_cpf': user.user_cpf}]
    ResultProxy = connection.execute(query, value)
    session.commit()
    return ResultProxy

def update(user: UsuarioEntenty.Usuario):
    query = db.update(usuarios).values(dt_nascimento=user.dt_nascimento, nome=user.nome, user_cpf=user.user_cpf)
    query = query.where(usuarios.columns.user_id == user.user_id)
    results = connection.execute(query)
    session.commit()
    return results


def delete(id: int):
    query = db.delete(usuarios)
    query = query.where(usuarios.columns.user_id == id)
    results = connection.execute(query)
    session.commit()
    return results
