import pandas as pd
import numpy as np
import pickle
from sklearn.naive_bayes import GaussianNB
from sklearn.metrics import accuracy_score
from sklearn.metrics import precision_score
from sklearn.metrics import recall_score
from sklearn.metrics import f1_score
from sklearn.metrics import roc_auc_score
from sklearn.preprocessing import OneHotEncoder

class IO:
  """
  Classe para representar as operações de IO
  """

  def readDataCSV():
      dataBase = pd.read_csv('/content/tennis.csv')
      return dataBase


  def salveDataTrain():
    """
    Salvar a base de dados treinada para evitar reprocessamento (salva em binário)
    """
    with open('tennis.pkl', 'wb') as f:
      pickle.dump([X_attr_train, Y_class_train], f)


  def loadDataTrain():
    """
    Carregar a base de dados treinada
    """
    with open('modelo.pickle', 'rb') as f:
      X_attr_train, Y_class_train = pickle.load(f)
    return X_attr_train, Y_class_train



class Naive_bayes:
  

  def splitData(dataBase):
    """
    Separar os dados entre um array atributos e um array classes
    """
    X_attr_train = dataBase.iloc[:, 0:4].values   # variavel de treinamento
    X_attr_test = dataBase.iloc[:, 0:4].values   # variavel para testar o modelo (acuracia)

    Y_class_train = dataBase.iloc[:, 4].values
    Y_class_test = dataBase.iloc[:, 4].values


  def codeToBynary():
    """
    Realizar conversão de atributos contínuos para discretos (converteR para binário)
    """
    encoder = OneHotEncoder()
    X_attr_train = encoder.fit_transform(X_attr_train).toarray()


  def training():
    """
    Realizar treinamento
    """ 
    naive_tennis = GaussianNB()
    naive_tennis.fit(X_attr_train, Y_class_train)


  def predict():
    """
    Realizar uma inferência / previsão
    """
    X_teste = np.array([['sunny', 'mild', 'high', 'false ']])
    X_teste_encoded = encoder.transform(X_teste).toarray()
    y_pred = naive_tennis.predict(X_teste_encoded)
    return y_pred


  def acccuracy(saidasPrevistas, saidasReais):
    """
    Calcular a acurácia do modelo
    """
    return accuracy_score(saidasReais, saidasPrevistas)
  
  def precision(saidasPrevistas, saidasReais):
    """
    Calcular a precisão do modelo
    """
    # pos_label: qual classe queremos calcular a precisão
    return precision_score(saidasReais, saidasPrevistas, pos_label='yes') 

  def recall(saidasPrevistas, saidasReais):
    """
    Calcular a sensibilidade do modelo
    """
    return recall_score(saidasReais, saidasPrevistas, pos_label='yes')
  
  def f1_score(saidasPrevistas, saidasReais):
    """
    Calcular o F1-Score do modelo
    """
    return f1_score(saidasReais, saidasPrevistas, pos_label='yes')

  def auc(saidasPrevistas, saidasReais, dadosTreinamento):
    """
    Calcular o auc do modelo
    """
    y_scores = naive_tennis.predict_proba(dadosTreinamento)[:, 1]  # obter as probabilidades de classe positiva
    return roc_auc_score(saidasReais, y_scores)


def executeTraining():
  dataBase = readDataCSV()
  X_attr_train, X_attr_test = splitData(dataBase)





def executePredict():



# Métricas

X_attr_t = encoder.fit_transform(X_attr_test).toarray()  # Converter para binário
y_pred = naive_tennis.predict(X_attr_t)   # Faz previsões no conjunto de teste



