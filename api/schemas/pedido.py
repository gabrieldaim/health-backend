from pydantic import BaseModel
from model import *

class pedidoSchema(BaseModel):
    produtos: str

def apresenta_pedido(pedidos: Pedidos):
    return { 
            "id": pedidos.id,
            "produtos": pedidos.produtos,
            "horario_criacao": pedidos.horario_criacao,
            "horario_conclusao": pedidos.horario_conclusao,
            "status": pedidos.status,
    }