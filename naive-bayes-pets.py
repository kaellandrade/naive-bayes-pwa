import pandas as pd
import sys
import numpy as np
import time
import multiprocessing
import csv
from sklearn.naive_bayes import MultinomialNB
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


def executeNaiveBayes(cliente, coluna, cliente_data):
    naiveB = NaiveBayes()
    naiveB.splitData(cliente_data, int(coluna))
    naiveB.codeToBynary()
    modelTrained = naiveB.training()
    inputUser = [int(cliente)]
    previsao = modelTrained.predict([inputUser])
    return previsao



# def calculateMetricas():
    # Métricas
    # y_pred = modelTrained.predict(naiveB.get_x_atributos())  # Faz previsões no conjunto de teste
    # print("Acuracia: {:.2f}%".format(naiveB.acccuracy(y_pred, naiveB.get_y_classes())))
    # print("Precisao: {:.1f}%".format(naiveB.precision(y_pred, naiveB.get_y_classes())))
    # print("Sensibilidade: {:.1f}%".format(naiveB.recall(y_pred, naiveB.get_y_classes())))
    # print("F1-Score: {:.1f}%".format(naiveB.f1_score(y_pred, naiveB.get_y_classes())))
    # print("AUC: {:.1f}%".format(naiveB.auc(naiveB.get_y_classes(), naiveB.get_x_atributos(), modelTrained)))


def buscar_produtos_cliente(cliente):
    """
    Função para buscar todas as compras que um cliente fez
    """

    # Leitura do CSV
    df = pd.read_csv('./Dados/DADOS_TRATADOS.csv')

    # Seleciona as linhas que contêm o valor Y na coluna X
    df_Y = df[df['CODCLI'] == cliente]
    return df_Y


def inferir_especie():
    with open('Dados/USUARIOS.csv', 'r') as arquivo_csv, open('Dados/USUARIOS_ESPECIE.csv', mode='w', newline='') as novocsvfile:
        leitor_csv = csv.reader(arquivo_csv)
        escritor_csv = csv.writer(novocsvfile)
        header = next(leitor_csv)  # Pula o cabeçalho
        header.append('ESPECIE')
        escritor_csv.writerow(header)
        cont = 1
        start_row = 20001
        for linha in leitor_csv:

            if cont-1 < start_row:
                cont = cont + 1
                continue

            valor_coluna = linha[0]  # Pega o valor da primeira coluna da linha atual

            start_time = time.time()

            # Buscar todas as compras de um cliente
            clienteData = buscar_produtos_cliente(int(valor_coluna))

            end_time = time.time()
            elapsed_time = end_time - start_time
            print("Tempo de execução para buscar as compras do cliente: {:.2f} segundos".format(elapsed_time))

            start_time = time.time()

            # Rodar naive bayes
            output = executeNaiveBayes(int(valor_coluna), str(3), clienteData)
            output = str(output)

            print(output.strip("[]").strip("'"))

            end_time = time.time()
            elapsed_time = end_time - start_time
            print("Tempo de execução para inferir a especie do cliente: {:.2f} segundos".format(elapsed_time))

            linha.append(output.strip("[]").strip("'"))
            escritor_csv.writerow(linha)

            print(f'{cont} usuarios concluidos')

            cont = cont + 1


def inferir_porte():
    with open('Dados/USUARIOS.csv', 'r') as arquivo_csv, open('Dados/USUARIOS_PORTE.csv', mode='w', newline='') as novocsvfile:
        leitor_csv = csv.reader(arquivo_csv)
        escritor_csv = csv.writer(novocsvfile)
        header = next(leitor_csv)  # Pula o cabeçalho
        header.append('PORTE')
        escritor_csv.writerow(header)
        cont = 1
        start_row = 20001
        for linha in leitor_csv:

            if cont-1 < start_row:
                cont = cont + 1
                continue

            valor_coluna = linha[0]  # Pega o valor da primeira coluna da linha atual

            start_time = time.time()

            # Buscar todas as compras de um cliente
            clienteData = buscar_produtos_cliente(int(valor_coluna))

            end_time = time.time()
            elapsed_time = end_time - start_time
            print("Tempo de execução para buscar as compras do cliente: {:.2f} segundos".format(elapsed_time))

            start_time = time.time()

            # Rodar naive bayes
            output = executeNaiveBayes(int(valor_coluna), str(4), clienteData)
            output = str(output)

            end_time = time.time()
            elapsed_time = end_time - start_time
            print("Tempo de execução para inferir o porte do cliente: {:.2f} segundos".format(elapsed_time))

            linha.append(output.strip("[]").strip("'"))
            escritor_csv.writerow(linha)

            print(f'{cont} usuarios concluidos')



            cont = cont + 1


def inferir_idade():
    with open('Dados/USUARIOS.csv', 'r') as arquivo_csv, open('Dados/USUARIOS_IDADE.csv', mode='w', newline='') as novocsvfile:
        leitor_csv = csv.reader(arquivo_csv)
        escritor_csv = csv.writer(novocsvfile)
        header = next(leitor_csv)  # Pula o cabeçalho
        header.append('IDADE')
        escritor_csv.writerow(header)
        cont = 1
        start_row = 20001
        for linha in leitor_csv:

            if cont-1 < start_row:
                cont = cont + 1
                continue

            valor_coluna = linha[0]  # Pega o valor da primeira coluna da linha atual

            start_time = time.time()

            # Buscar todas as compras de um cliente
            clienteData = buscar_produtos_cliente(int(valor_coluna))

            end_time = time.time()
            elapsed_time = end_time - start_time
            print("Tempo de execução para buscar as compras do cliente: {:.2f} segundos".format(elapsed_time))

            start_time = time.time()

            # Rodar naive bayes
            output = executeNaiveBayes(int(valor_coluna), str(5), clienteData)
            output = str(output)

            end_time = time.time()
            elapsed_time = end_time - start_time
            print("Tempo de execução para inferir a idade do cliente: {:.2f} segundos".format(elapsed_time))

            linha.append(output.strip("[]").strip("'"))
            escritor_csv.writerow(linha)

            print(f'{cont} usuarios concluidos')

            cont = cont + 1



if __name__ == '__main__':
    pa = multiprocessing.Process(target=inferir_especie())
    pb = multiprocessing.Process(target=inferir_porte())
    pc = multiprocessing.Process(target=inferir_idade())

    pa.start()
    pb.start()
    pc.start()

    pa.join()
    pb.join()
    pc.join()





