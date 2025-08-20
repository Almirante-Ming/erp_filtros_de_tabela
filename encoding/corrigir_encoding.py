import pandas as pd

# corrigir caracteres antes de passar pelo reencoding, caso contrario alguns caracteres irao quebrar

arquivo_csv_origem = 'input.csv'

arquivo_csv_destino = 'output.csv'

df = pd.read_csv(arquivo_csv_origem, encoding='cp1252', delimiter=';')

df.to_csv(arquivo_csv_destino, index=False, encoding='utf-8', sep=';')

print(f'Arquivo {arquivo_csv_destino} alterado com sucesso')
