import subprocess
import csv
import time
import multiprocessing

def especie():
    with open('Dados/USUARIOS.csv', 'r') as arquivo_csv, open('Dados/USUARIOS_ESPECIE.csv', mode='w', newline='') as novocsvfile:
        leitor_csv = csv.reader(arquivo_csv)
        escritor_csv = csv.writer(novocsvfile)
        header = next(leitor_csv)  # Pula o cabeçalho
        header.append('ESPECIE')
        escritor_csv.writerow(header)
        cont = 1
        # start_row = 2508
        for linha in leitor_csv:

            # if cont-1 < start_row:
            #     cont = cont + 1
            #     continue

            valor_coluna = linha[0]  # Pega o valor da primeira coluna da linha atual

            start_time = time.time()

            # Executa o arquivo python
            subprocess.run(["python3", "gerar_csv_cliente.py", str(valor_coluna)], capture_output=False, text=False)

            end_time = time.time()
            elapsed_time = end_time - start_time
            print("Tempo de execução para gerar csv do cliente: {:.2f} segundos".format(elapsed_time))

            start_time = time.time()

            output = subprocess.check_output(["python3", "teste-naive-bayes-pets.py", str(valor_coluna) , str(3)])

            end_time = time.time()
            elapsed_time = end_time - start_time
            print("Tempo de execução para inferir a especie do cliente: {:.2f} segundos".format(elapsed_time))

            linha.append(output.decode('utf-8').strip())
            escritor_csv.writerow(linha)

            print(f'{cont} usuarios concluidos')
            cont = cont + 1


def porte():
    with open('Dados/USUARIOS.csv', 'r') as arquivo_csv, open('Dados/USUARIOS_PORTE.csv', mode='w', newline='') as novocsvfile:
        leitor_csv = csv.reader(arquivo_csv)
        escritor_csv = csv.writer(novocsvfile)
        header = next(leitor_csv)  # Pula o cabeçalho
        header.append('PORTE')
        escritor_csv.writerow(header)
        cont = 1
        # start_row = 2508
        for linha in leitor_csv:

            # if cont-1 < start_row:
            #     cont = cont + 1
            #     continue

            valor_coluna = linha[0]  # Pega o valor da primeira coluna da linha atual

            start_time = time.time()

            # Executa o arquivo python
            subprocess.run(["python3", "gerar_csv_cliente.py", str(valor_coluna)], capture_output=False, text=False)

            end_time = time.time()
            elapsed_time = end_time - start_time
            print("Tempo de execução para gerar csv do cliente: {:.2f} segundos".format(elapsed_time))

            start_time = time.time()

            output = subprocess.check_output(["python3", "teste-naive-bayes-pets.py", str(valor_coluna) , str(4)])

            end_time = time.time()
            elapsed_time = end_time - start_time
            print("Tempo de execução para inferir a especie do cliente: {:.2f} segundos".format(elapsed_time))

            linha.append(output.decode('utf-8').strip())
            escritor_csv.writerow(linha)

            print(f'{cont} usuarios concluidos')
            cont = cont + 1

def idade():
    with open('Dados/USUARIOS.csv', 'r') as arquivo_csv, open('Dados/USUARIOS_IDADE.csv', mode='w', newline='') as novocsvfile:
        leitor_csv = csv.reader(arquivo_csv)
        escritor_csv = csv.writer(novocsvfile)
        header = next(leitor_csv)  # Pula o cabeçalho
        header.append('IDADE')
        escritor_csv.writerow(header)
        cont = 1
        # start_row = 2508
        for linha in leitor_csv:

            # if cont-1 < start_row:
            #     cont = cont + 1
            #     continue

            valor_coluna = linha[0]  # Pega o valor da primeira coluna da linha atual

            start_time = time.time()

            # Executa o arquivo python
            subprocess.run(["python3", "gerar_csv_cliente.py", str(valor_coluna)], capture_output=False, text=False)

            end_time = time.time()
            elapsed_time = end_time - start_time
            print("Tempo de execução para gerar csv do cliente: {:.2f} segundos".format(elapsed_time))

            start_time = time.time()

            output = subprocess.check_output(["python3", "teste-naive-bayes-pets.py", str(valor_coluna) , str(5)])

            end_time = time.time()
            elapsed_time = end_time - start_time
            print("Tempo de execução para inferir a especie do cliente: {:.2f} segundos".format(elapsed_time))

            linha.append(output.decode('utf-8').strip())
            escritor_csv.writerow(linha)

            print(f'{cont} usuarios concluidos')
            cont = cont + 1

if __name__ == '__main__':
    pa =  multiprocessing.Process(target=especie)
    pb = multiprocessing.Process(target=porte)
    pc = multiprocessing.Process(target=idade)

    pa.start()
    pb.start()
    pc.start()

    pa.join()
    pb.join()
    pc.join()