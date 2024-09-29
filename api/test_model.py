import pandas as pd
from sklearn.metrics import accuracy_score

from model.model import Model

# To run: pytest -v test_modelos.py

# Instanciação das Classes
model = Model()

# Parâmetros    
url_data = "https://media.githubusercontent.com/media/juliano-lopes/sistema-inteligente/refs/heads/main/dados_de_clientes_teste.csv"
cols = [
    'idade',
    'salario_anual',
    'num_contas',
    #'num_cartoes',
    'juros_emprestimo',
    'num_emprestimos',
    'dias_atraso',
    'num_pagamentos_atrasados',
    'divida_total',
    #'investimento_mensal',
    'score_credito'
    ]

# Carga dos dados
dataset = model.load_data(url_data, cols)
dataset = model.treat_data(dataset)
X, y = model.balance_classes(dataset)
rescaledX = model.scale_data(X)

# Método para testar a acurácia do modelo
def test_model_accuracy():
    predictions = model.predict(rescaledX)
    accuracy = accuracy_score(y, predictions)
    assert accuracy >= 0.70
def test_score_classification():
    # Novos dados  com classes ainda não determinadas
    data = {'idade':  [25, 34, 46],
        'salario_anual': [19000.33, 34148.50, 30144.22],
        'num_contas': [1, 3, 2],
        #'num_cartoes': [1, 3, 2],
        'juros_emprestimo': [29.55, 15.33, 6.38],
        'num_emprestimos': [15, 9, 3],
        'dias_atraso': [60, 20, 4],
        'num_pagamentos_atrasados': [30, 9, 1],
        'divida_total': [20345.33, 1000.55, 835.00]
        #'investimento_mensal': [1.55, 0.00, 10.33],
        }
    attributes = list(data.keys())
    input_data = pd.DataFrame(data, columns=attributes)
    X_input = input_data.values
    rescaledInputX = model.scale_data(X_input)
    predictions = model.predict(rescaledInputX)
    assert predictions[0] == "Baixo"
    assert predictions[1] == "Regular"
    assert predictions[2] == "Alto"