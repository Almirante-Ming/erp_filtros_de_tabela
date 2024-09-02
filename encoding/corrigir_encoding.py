import pandas as pd

# Caminho do arquivo CSV de origem
arquivo_csv_origem = './origem.csv'

# Caminho do arquivo CSV de destino
arquivo_csv_destino = './destino.csv'

# Ler o arquivo CSV de origem com encoding 'cp1252' e delimitador ';'
df = pd.read_csv(arquivo_csv_origem, encoding='cp1252', delimiter=';')

# Salvar o arquivo CSV com encoding 'utf-8' e delimitador ';'
df.to_csv(arquivo_csv_destino, index=False, encoding='utf-8', sep=';')

print(f'Arquivo {arquivo_csv_destino} criado com sucesso em UTF-8.')
