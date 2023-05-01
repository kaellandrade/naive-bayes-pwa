import subprocess
import csv
import time



with open('Dados/USUARIOS.csv', 'r') as arquivo_csv, open('Dados/USUARIOS_ESPECIE.csv', mode='w', newline='') as novocsvfile:
    leitor_csv = csv.reader(arquivo_csv)
    escritor_csv = csv.writer(novocsvfile)
    header = next(leitor_csv)  # Pula o cabeçalho
    header.append('ESPECIE')
    escritor_csv.writerow(header)
    cont = 1
    start_row = 2508
    for linha in leitor_csv:

        if cont-1 < start_row:
            cont = cont + 1
            continue

        valor_coluna = linha[0]  # Pega o valor da primeira coluna da linha atual

        start_time = time.time()

        # Executa o arquivo python
        subprocess.run(["python", "gerar_csv_cliente.py", str(valor_coluna)], capture_output=False, text=False)

        end_time = time.time()
        elapsed_time = end_time - start_time
        print("Tempo de execução para gerar csv do cliente: {:.2f} segundos".format(elapsed_time))

        start_time = time.time()

        output = subprocess.check_output(["python", "teste-naive-bayes-pets.py", str(valor_coluna)])

        end_time = time.time()
        elapsed_time = end_time - start_time
        print("Tempo de execução para inferir a especie do cliente: {:.2f} segundos".format(elapsed_time))

        linha.append(output.decode('utf-8').strip())
        escritor_csv.writerow(linha)

        print(f'{cont} usuarios concluidos')
        cont = cont + 1

