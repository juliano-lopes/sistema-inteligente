from pydantic import BaseModel
from typing import Optional, List
import json
import numpy as np

class ClientSchema(BaseModel):
    """ Define como dados de novo cliente deve ser recebido
    """
    idade: int = 25
    salario_anual: float = 5000.00
    num_contas: int = 1
    juros_emprestimo: float = 8.5
    num_emprestimos: int = 1
    dias_atraso: int = 5
    num_pagamentos_atrasados: int = 2
    divida_total: float = 100.50
    
class ClientScoreSchema(BaseModel):
    """Define como um score de cliente será retornado
    """
    score_classification: str = "Alto"
