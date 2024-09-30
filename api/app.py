from flask_openapi3 import OpenAPI, Info, Tag
from flask import redirect
from urllib.parse import unquote


from logger import logger
from model.model import Model
from schemas import *
from flask_cors import CORS


# Instanciando o objeto OpenAPI
info = Info(title="API sistema inteligente para classificar score de crédito de clientes, utilizando IA.", version="1.0.0")
app = OpenAPI(__name__, info=info)
CORS(app)

# Definindo tags para agrupamento das rotas
home_tag = Tag(name="Documentação", description="Seleção de documentação: Swagger, Redoc ou RapiDoc")
score_tag = Tag(name="Score", description="Classificação de score de crédito para clientes")


# Rota home
@app.get('/', tags=[home_tag])
def home():
    """Redireciona para /openapi, tela que permite a escolha do estilo de documentação.
    """
    return redirect('/openapi')

# Rota de obtenção da classificação de score de crédito
@app.post('/score', tags=[score_tag],
          responses={"200": ClientScoreSchema, "400": ErrorSchema, "409": ErrorSchema})
def score_client_credit_classification(form: ClientSchema):
    """
    Retorna classificação do score de crédito do cliente
    
    """
    
    
    try:
        # Carregando modelo
        model = Model()
        score_classification = model.predict_score(form)
        score = ClientScoreSchema(score_classification=score_classification)
        return score.json(), 200
    
    # Caso ocorra algum erro na predição
    except Exception as e:
        error_msg = f"Não foi possível classificar o score de crédito: {e}"
        logger.warning(f"Erro ao classificar score de crédito', {error_msg}")
        return {"message": error_msg}, 400
    
