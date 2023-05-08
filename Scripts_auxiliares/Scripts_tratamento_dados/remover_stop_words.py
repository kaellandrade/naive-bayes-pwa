import pandas as pd
import nltk
nltk.download('stopwords')
from nltk.corpus import stopwords


FILE_DADOS_BASE = 'DADOS_IA_PROJETO.csv'
FILE_DADOS_TRATADOS = 'DADOS_IA_TRATADOS.csv'  # arquivo onde será salvo o modelo treinado


def remove_stop_words(text):
    stop_words = set(stopwords.words('portuguese'))
    words = text.split()
    clean_words = [word for word in words if word.lower() not in stop_words]  # Remove as stop words
    clean_text = ' '.join(clean_words)  # Junta as palavras novamente em uma string
    return clean_text


def readDataCSV():
    dataBase = pd.read_csv(FILE_DADOS_BASE)
    return dataBase


def main():
    dataBase = readDataCSV()
    dataBase['PRODUTO'] = dataBase['PRODUTO'].apply(remove_stop_words)
    dataBase.to_csv('DADOS_IA_TRATADOS.csv', index=False)


if __name__ == '__main__':
    main()

