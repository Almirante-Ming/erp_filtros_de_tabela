import pandas as pd

def converter_data(data):
    try:
        partes = data.split('/')
        if len(partes) != 3:
            return data  # Retorna o valor original se não puder ser convertido
        dia = partes[0].zfill(2)
        mes = partes[1].zfill(2)
        ano = partes[2]
        ano = '20' + ano if len(ano) == 2 else ano  # Adiciona '20' para anos no formato de 2 dígitos
        return f'{ano}-{mes}-{dia}'
    except Exception as e:
        return data  # Retorna o valor original em caso de erro

def processar_csv(entrada_csv, saida_csv):
    try:
        df = pd.read_csv(entrada_csv)
        
        for coluna in df.columns:
            df[coluna] = df[coluna].apply(lambda x: converter_data(str(x)))
        
        df.to_csv(saida_csv, index=False)
        print(f"CSV processado e salvo em: {saida_csv}")
    except Exception as e:
        print(f"Erro ao processar o CSV: {e}")

entrada_csv = './corrigir_data/datas.csv'
saida_csv = './corrigir_data/novo_arquivo.csv'

processar_csv(entrada_csv, saida_csv)
