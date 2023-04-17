from pydantic import BaseModel
from model import *

class PratosSchema(BaseModel):
    nome: str 
    ingredientes:str 
    preco: int 

def apresenta_prato(pratos: Pratos):
    return { 
        "id": pratos.id,
        "nome": pratos.nome,
        "ingredientes": pratos.ingredientes,
        "preco": pratos.preco
    }

