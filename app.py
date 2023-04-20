from flask_openapi3 import OpenAPI, Info, Tag
from flask import redirect, jsonify
from flask_cors import CORS
from urllib.parse import unquote

from sqlalchemy.exc import IntegrityError

from model import *
from schemas import *

info = Info(title="Minha API", version="1.0.0")
app = OpenAPI(__name__, info=info)
CORS(app)


# definindo tags
home_tag = Tag(name="Documentação", description="Seleção de documentação: Swagger, Redoc ou RapiDoc")
pratos_tag = Tag(name="Pratos", description="Rotas relacionadas a tabela de pratos")
sucos_tag = Tag(name="Sucos", description="Rotas relacionadas a tabela de Sucos")
carrinho_tag = Tag(name="Carrinho", description="Rotas relacionadas a tabela de Carrinho")
pedidos_tag = Tag(name="Pedidos", description="Rotas relacionadas a tabela de Pedidos")




@app.get('/', tags=[home_tag])
def home():
    """Redireciona para /openapi, tela que permite a escolha do estilo de documentação.
    """
    return redirect('/openapi')

@app.get('/prato', tags=[pratos_tag])
def getPrato():
    """Busca todos os itens da tabela pratos
    """
    session = Session()
    pratos = session.query(Pratos).all()
    return jsonify({'pratos': [apresenta_prato(prato) for prato in pratos]})


@app.get('/suco', tags=[sucos_tag])
def getSuco():
    """Busca todos os itens da tabela sucos
    """
    session = Session()
    sucos = session.query(Sucos).all()
    return jsonify({'Sucos': [apresenta_suco(suco) for suco in sucos]})

    
@app.get('/carrinho', tags=[carrinho_tag])
def getCarrinho():
    """Busca todos os itens da tabela carrinho
    """
    session = Session()
    carrinho = session.query(Carrinho).all()
    return jsonify({'carrinho': [apresenta_carrinho(item) for item in carrinho]})

@app.post('/carrinho', tags=[carrinho_tag] , responses={
    "400": ErrorSchema
})
def add_carrinho(form: carrinhoSchema):
    """Adiciona um novo Produto à base de dados de carrinho
    """
    carrinho = Carrinho(
        produto_nome=form.produto_nome,
        observacao=form.observacao,
        quantidade=form.quantidade,
        preco=form.preco)
    try:
        # criando conexão com a base
        session = Session()
        # adicionando produto
        session.add(carrinho)
        # efetivando o camando de adição de novo item na tabela
        session.commit()
        return apresenta_carrinho(carrinho), 200

    except IntegrityError as e:
        session.rollback()
        err = e.args
        return {"mesage": err}, 400

@app.delete('/carrinho', tags=[carrinho_tag] , responses={
    "400": ErrorSchema
})
def remove_carrinho(form: removeCarrinhoSchema):
    """remove um Produto à base de dados de carrinho
    """
    try:
        # criando conexão com a base
        id_produto = unquote(unquote(form.id))
        session = Session()
        # adicionando produto
        produto = session.query(Carrinho).filter(Carrinho.id == id_produto).first()
        if not produto:
            return {"mesage": "produto não encontrado na base"},404
        session.query(Carrinho).filter(Carrinho.id == id_produto).delete()
        # efetivando o camando de adição de novo item na tabela
        session.commit()
        return apresenta_carrinho(produto), 200

    except IntegrityError as e:
        session.rollback()
        err = e.args
        return {"mesage": err}, 400

@app.get('/pedidos', tags=[pedidos_tag])
def getPedidos():
    """Busca todos os itens da tabela pedidos
    """
    session = Session()
    pedidos = session.query(Pedidos).all()
    return jsonify({'pedidos': [apresenta_pedido(pedido) for pedido in pedidos]})

@app.post('/pedidos', tags=[pedidos_tag] , responses={
    "400": ErrorSchema
})
def add_pedido(form: pedidoSchema):
    """Adiciona um novo Produto à base de dados pedidos
    """
    pedido = Pedidos(produtos=form.produtos)

    try:
        # criando conexão com a base
        session = Session()
        # adicionando produto
        session.add(pedido)
        # efetivando o camando de adição de novo item na tabela
        session.commit()
        carrinho = session.query(Carrinho).all()
        for item in carrinho:
            session.delete(item)
        session.commit()
        return apresenta_pedido(pedido), 200

    except IntegrityError as e:
        session.rollback()
        err = e.args
        return {"mesage": err}, 400
    
if __name__ == '__main__':
    app.run(host="0.0.0.0", port=5000, debug=True)