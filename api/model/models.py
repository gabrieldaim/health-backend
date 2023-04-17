from sqlalchemy import create_engine, Column, Integer, String, Float, Text, DateTime, JSON
from datetime import datetime, timedelta
from sqlalchemy.ext.declarative import declarative_base


Base = declarative_base()

class Pratos(Base):
    __tablename__ = 'pratos'
    id = Column(Integer, primary_key=True)
    nome = Column(String(255))
    ingredientes = Column(Text)
    preco = Column(Float)


class Sucos(Base):
    __tablename__ = 'sucos'
    id = Column(Integer, primary_key=True)
    nome = Column(String(255))
    tamanho = Column(Integer)
    preco = Column(Float)

class Carrinho(Base):
    __tablename__ = 'carrinho'
    id = Column(Integer, primary_key=True)
    produto_nome = Column(String(255))
    observacao = Column(Text)
    quantidade = Column(Integer)
    preco = Column(Float)

class Pedidos(Base):
    __tablename__ = 'pedidos'
    id = Column(Integer, primary_key=True)
    produtos = Column(Text)
    horario_criacao = Column(DateTime, default=datetime.utcnow)
    horario_conclusao = Column(DateTime)
    status = Column(String, default=False) 

    def __init__(self,produtos):
        self.produtos = produtos
        self.horario_conclusao = datetime.utcnow() + timedelta(minutes=10)
    
    def changeStatus(self):
        self.status = not self.status 

engine = create_engine('sqlite:///meu_banco_de_dados.db')  # Substitua pelo tipo de banco de dados que você deseja utilizar

Base.metadata.create_all(engine)
