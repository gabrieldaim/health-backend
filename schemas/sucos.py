from pydantic import BaseModel
from model import *

class SucosSchema(BaseModel):
    nome: str 
    tamanho:int 
    preco: float 

def apresenta_suco(sucos: Sucos):
    return { 
        "id": sucos.id,
        "nome": sucos.nome,
        "tamanho": sucos.tamanho,
        "preco": sucos.preco
    }