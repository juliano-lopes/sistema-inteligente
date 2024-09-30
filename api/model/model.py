import numpy as np
import pickle
import joblib
import pandas as pd
from sklearn.preprocessing import MinMaxScaler
from imblearn.under_sampling import RandomUnderSampler
from ml_model.ml_path import MlPath

class Model:
    def __init__(self, model_path=None, scaler_path=None) -> None:
        self.model_path = model_path if model_path != None else  MlPath.model_path
        self.scaler_path = scaler_path if scaler_path != None else MlPath.scaler_path
        self.load_model()
    def load_model(self):
        """Dependendo se o final for .pkl ou .joblib, carregamos de uma forma ou de outra
        """
        
        if self.model_path.endswith('.pkl'):
            self.model = pickle.load(open(self.model_path, 'rb'))
            self.scaler = pickle.load(open(self.scaler_path, 'rb'))
        elif self.ml_path.endswith('.joblib'):
            self.model = joblib.load(self.model_path)
            self.scaler = joblib.load(self.scaler_path)
        else:
            raise Exception('Formato de arquivo não suportado')
        return self.model, self.scaler
    
    def predict_score(self, form):
        """Realiza a predição da classe do score de crédito do cliente com base no modelo treinado
        """
        try:
            attributes = list(form.dict().keys())
            entry = pd.DataFrame([form.dict()], columns=attributes)
            X_entry = entry.values
            scalerX = self.scaler.transform(X_entry)
            score_classification = self.predict(scalerX)
            return str(score_classification[0])
        except Exception as e:
            raise Exception(f"Erro no modelo ao predizer score: {e}")
    def predict(self, X_input):
        predictions = self.model.predict(X_input)
        return predictions

    def treat_data(self, dataframe):
        """
        realiza limpesa dos dados
        """
        try:
            dataframe['salario_anual'] = pd.to_numeric(dataframe['salario_anual'], errors='coerce')
            dataframe.dropna(inplace=True)
            return dataframe
        except Exception as e:
            raise Exception(f"Erro ao tratar dados: {e}")
        
    def balance_classes(self, dataframe):
        """
        realiza balanceamento das classes
        """
        try:
            X = dataframe.drop('score_credito', axis=1)
            y = dataframe['score_credito']
            rus = RandomUnderSampler(random_state=42)
            X_resampled, y_resampled = rus.fit_resample(X, y)
            print("Balanceado")
            print(pd.Series(y_resampled).value_counts())
            return     X_resampled, y_resampled
        except Exception as e:
            raise Exception(f"Erro ao balancear classes: {e}")
        
    def scale_data(self, X_input):
        """
        aplica scaler nos dados
        """
        try:
            rescaledX = self.scaler.transform(X_input) # aplicação da normalização
            return rescaledX
        except Exception as e:
            raise Exception(f"Erro ao aplicar o scaler: {e}")
        
    def load_data(self, source, cols):
        """
        carrega dados
        """
        try:
            dataset = pd.read_csv(source, usecols=cols, delimiter=',')
            dataset.head()
            return dataset
        except Exception as e:
            raise Exception(f"Erro ao carregar dados: {e}")