from pydantic import BaseModel
from model import *

class carrinhoSchema(BaseModel):
    produto_nome: str
    observacao: str
    quantidade: int
    preco: float

class removeCarrinhoSchema(BaseModel):
    id: int

def apresenta_carrinho(carrinho: Carrinho):
    return { 
        "id": carrinho.id,
        "produto_nome": carrinho.produto_nome,
        "observacao": carrinho.observacao,
        "quantidade": carrinho.quantidade,
        "preco": carrinho.preco
    }