import pandas as pd
import sys
import numpy as np
import pickle
import csv
from sklearn.naive_bayes import GaussianNB
from sklearn.naive_bayes import BernoulliNB
from sklearn.naive_bayes import CategoricalNB
from sklearn.naive_bayes import MultinomialNB
from sklearn.naive_bayes import ComplementNB
from sklearn.metrics import accuracy_score
from sklearn.metrics import precision_score
from sklearn.metrics import recall_score
from sklearn.metrics import f1_score
from sklearn.metrics import roc_auc_score
from sklearn.preprocessing import OneHotEncoder


FILE_DADOS_BASE = './Dados/DADOS_CLIENTE_X.csv'
FILE_DADOS_TREINADOS = 'DADOS_MODEL.pkl'  # arquivo onde será salvo o modelo treinado


class IO:
    """
    Classe para representar as operações de IO
    """
    @staticmethod
    def readDataCSV():
        dataBase = pd.read_csv(FILE_DADOS_BASE)
        return dataBase

    @staticmethod
    def salveDataTrain(x_atributos, y_classes, model, encoder):
        """
        Salvar a base de dados treinada para evitar reprocessamento (salva em binário)
        """
        with open(FILE_DADOS_TREINADOS, 'wb') as f:
            pickle.dump([x_atributos, y_classes, model, encoder], f)

    @staticmethod
    def loadDataTrain():
        """
        Carregar a base de dados treinada
        """
        with open(FILE_DADOS_TREINADOS, 'rb') as f:
            x_atributos, y_classes, modelTrained, encoder = pickle.load(f)
        return x_atributos, y_classes, modelTrained, encoder


class NaiveBayes:
    x_atributos = None
    y_classes = None

    def set_x_atributos(self, dados):
        self.x_atributos = dados

    def set_y_classes(self, dados):
        self.y_classes = dados

    def get_x_atributos(self):
        return self.x_atributos

    def get_y_classes(self):
        return self.y_classes

    def splitData(self, database, column):
        """
        Separar os dados entre um array atributos e um array classes
        """
        self.x_atributos = database.iloc[:, 0:1].values
        self.y_classes = database.iloc[:, column].values

    def codeToBynary(self):
        """
        Realizar conversão de atributos contínuos para discretos (converter para binário)
        """
        encoder = OneHotEncoder()
        self.x_atributos = encoder.fit_transform(self.x_atributos).toarray()
        return encoder

    def training(self):
        """
        Realizar treinamento
        """
        model = MultinomialNB()
        model.fit(self.x_atributos, self.y_classes)
        return model

    @staticmethod
    def doPredict(input_user, model_trained, encoder):
        """
        Realizar uma inferência / previsão
        """
        x_input = np.array(input_user)
        x_input_encoded = encoder.transform(x_input).toarray()
        y_pred = model_trained.predict(x_input_encoded)
        return y_pred

    @staticmethod
    def acccuracy(saidas_previstas, saidas_reais):
        """
        Calcular a acurácia do modelo
        """
        return accuracy_score(saidas_reais, saidas_previstas) * 100

    @staticmethod
    def precision(saidas_previstas, saidas_reais):
        """
        Calcular a precisão do modelo
        """
        # pos_label: qual classe queremos calcular a precisão
        return precision_score(saidas_reais, saidas_previstas, pos_label='yes') * 100

    @staticmethod
    def recall(saidas_previstas, saidas_reais):
        """
        Calcular a sensibilidade do modelo
        """
        return recall_score(saidas_reais, saidas_previstas, pos_label='yes') * 100

    @staticmethod
    def f1_score(saidas_previstas, saidas_reais):
        """
        Calcular o F1-Score do modelo
        """
        return f1_score(saidas_reais, saidas_previstas, pos_label='yes') * 100

    @staticmethod
    def auc(saidas_reais, dados_treinamento, model):
        """
        Calcular o auc do modelo
        """
        y_scores = model.predict_proba(dados_treinamento)[:, 1]  # obter as probabilidades de classe positiva
        return roc_auc_score(saidas_reais, y_scores) * 100


def execute():
    naiveB = NaiveBayes()
    io = IO()
    dataBase = io.readDataCSV()
    inputColumn = int(sys.argv[2])
    naiveB.splitData(dataBase, inputColumn)
    encoder = naiveB.codeToBynary()
    modelTrained = naiveB.training()

    inputUser = [int(sys.argv[1])]
    # inputUser = [20]

    previsao = modelTrained.predict([inputUser])
    print(previsao)



# def executePredict():
#     # y_prob = modelTrained.predict(naiveB.get_x_atributos())  # Retorno de probabilidade pra cada classe
#     # print("Probabilidades: ", y_prob)
#
#     # Métricas
#     # y_pred = modelTrained.predict(naiveB.get_x_atributos())  # Faz previsões no conjunto de teste
#     # print("Acuracia: {:.2f}%".format(naiveB.acccuracy(y_pred, naiveB.get_y_classes())))
#     # print("Precisao: {:.1f}%".format(naiveB.precision(y_pred, naiveB.get_y_classes())))
#     # print("Sensibilidade: {:.1f}%".format(naiveB.recall(y_pred, naiveB.get_y_classes())))
#     # print("F1-Score: {:.1f}%".format(naiveB.f1_score(y_pred, naiveB.get_y_classes())))
#     # print("AUC: {:.1f}%".format(naiveB.auc(naiveB.get_y_classes(), naiveB.get_x_atributos(), modelTrained)))


if __name__ == '__main__':
    execute()



