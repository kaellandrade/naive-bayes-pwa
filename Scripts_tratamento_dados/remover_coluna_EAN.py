import csv

with open('../Dados/DADOS_BRUTOS.csv', 'r', newline='', encoding='utf-8') as arquivo_entrada, \
        open('../Dados/DADOS_SEM_EAN.csv', 'w', newline='', encoding='utf-8') as arquivo_saida:
    leitor = csv.DictReader(arquivo_entrada)
    escritor = csv.DictWriter(arquivo_saida, fieldnames=[campo for campo in leitor.fieldnames if campo != 'EAN'])
    escritor.writeheader()

    for linha in leitor:
        del linha['EAN']
        escritor.writerow(linha)
