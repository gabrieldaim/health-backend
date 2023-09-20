from pydantic import BaseModel
from model import *

class enderecoSchema(BaseModel):
    cep: str
    logradouro: str
    numero: str
    bairro: str
    estado: str
    complemento: str


def apresenta_endereco(endereco: Endereco):
    return { 
        "cep": endereco.cep,
        "logradouro": endereco.logradouro,
        "numero": endereco.numero,
        "bairro": endereco.bairro,
        "estado": endereco.estado,
        "complemento": endereco.complemento
    }