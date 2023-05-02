from scipy.stats import shapiro
import pandas as pd

df = pd.read_csv('../Dados/USUARIOS_PETS_REPRESENTACAO_FINAL.csv')

stat, p = shapiro(df['IDADE'])

print('Estatística de teste:', stat)
print('Valor-p:', p)

if p > 0.05:
    print('Os dados parecem seguir uma distribuição normal')
else:
    print('Os dados não seguem uma distribuição normal')
