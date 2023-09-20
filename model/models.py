from sqlalchemy import create_engine, Column, Integer, String, Float, Text, DateTime, JSON
from datetime import datetime, timedelta
from sqlalchemy.ext.declarative import declarative_base


Base = declarative_base()

class Pratos(Base):
    __tablename__ = 'pratos'
    id = Column(Integer, primary_key=True)
    nome = Column(String(255))
    ingredientes = Column(Text)
    descricao = Column(Text)
    preco = Column(Float)


class Sucos(Base):
    __tablename__ = 'sucos'
    id = Column(Integer, primary_key=True)
    nome = Column(String(255))
    tamanho = Column(Integer)
    descricao = Column(Text)
    preco = Column(Float)

class Carrinho(Base):
    __tablename__ = 'carrinho'
    id = Column(Integer, primary_key=True)
    produto_nome = Column(String(255))
    observacao = Column(Text)
    quantidade = Column(Integer)
    preco = Column(Float)

class Endereco(Base):
    __tablename__ = 'endereco'
    id = Column(Integer, primary_key=True)
    cep = Column(Text)
    logradouro = Column(Text)
    numero = Column(Text)
    bairro = Column(Text)
    estado = Column(Text)
    complemento = Column(Text)

class Pedidos(Base):
    __tablename__ = 'pedidos'
    id = Column(Integer, primary_key=True)
    produtos = Column(Text)
    horario_criacao = Column(DateTime, default=datetime.utcnow)
    horario_conclusao = Column(DateTime)
    status = Column(String, default=False) 
    endereco = Column(Text)

    def __init__(self,produtos):
        print(produtos)
        self.produtos = produtos
        self.horario_conclusao = datetime.utcnow() + timedelta(minutes=25)
    
    def changeStatus(self):
        self.status = not self.status 

