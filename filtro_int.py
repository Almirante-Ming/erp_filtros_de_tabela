import re

def limpar_linha(linha):
    # Remove todos os caracteres que não sejam números
    return re.sub(r'\D', '', linha)

def processar_arquivo(arquivo_entrada, arquivo_saida):
    linhas_validas = []
    
    # Ler o arquivo de entrada
    with open(arquivo_entrada, 'r') as f:
        linhas = f.readlines()
        
        for linha in linhas:
            linha_limpa = limpar_linha(linha.strip())
            if len(linha_limpa) == 8:
                linhas_validas.append(linha_limpa)
    
    # Escrever as linhas válidas no arquivo de saída
    with open(arquivo_saida, 'w') as f:
        for linha in linhas_validas:
            f.write(linha + '\n')

# Caminhos dos arquivos
arquivo_entrada = 'input.txt'
arquivo_saida = 'output.txt'

# Processar o arquivo
processar_arquivo(arquivo_entrada, arquivo_saida)

print(f"Processamento concluído. Linhas válidas foram escritas em '{arquivo_saida}'")
