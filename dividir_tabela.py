import pandas as pd

# Caminho do arquivo CSV de origem
arquivo_csv_origem = 'tabela_origem.csv'

# Nome base para os arquivos CSV de destino
nome_base_destino = 'tabela_destino_'

# Número de linhas por arquivo de destino (excluindo o cabeçalho)
linhas_por_arquivo = 500

# Ler o arquivo CSV de origem com encoding 'cp1252' e delimitador ';'
df = pd.read_csv(arquivo_csv_origem, encoding='cp1252', delimiter=';')

# Contar o número total de linhas (excluindo o cabeçalho)
total_linhas = len(df)

# Calcular o número de arquivos de destino necessários
numero_de_arquivos = (total_linhas // linhas_por_arquivo) + (1 if total_linhas % linhas_por_arquivo != 0 else 0)

# Loop para criar e salvar arquivos de destino com encoding 'cp1252' e delimitador ';'
for i in range(numero_de_arquivos):
    inicio = i * linhas_por_arquivo
    fim = inicio + linhas_por_arquivo
    df_parcial = df.iloc[inicio:fim]
    nome_arquivo_destino = f'{nome_base_destino}{i+1}.csv'
    df_parcial.to_csv(nome_arquivo_destino, index=False, header=True, encoding='cp1252', sep=';')
    print(f'Arquivo {nome_arquivo_destino} criado com sucesso.')

print('Divisão do arquivo CSV concluída.')