def converter_data(data):
    try:
        partes = str(data).split('/')
        if len(partes) != 3:
            return data
        dia = partes[0].zfill(2)
        mes = partes[1].zfill(2)
        ano = partes[2]
        ano = '20' + ano if len(ano) == 2 else ano
        return f'{ano}-{mes}-{dia}'
    except Exception:
        return data


def processar_csv(entrada_csv, saida_csv):
    try:
        try:
            df = pd.read_csv(entrada_csv, delimiter=';')
        except Exception:
            df = pd.read_csv(entrada_csv)

        for coluna in df.columns:
            if 'data' in coluna.lower():
                df[coluna] = df[coluna].apply(converter_data)

        for col in df.columns:
            df[col] = df[col].apply(lambda x: f'"{str(x).strip().replace(chr(34), "")}"')

        df.to_csv(saida_csv, index=False, sep=';')
        print(f"CSV processado e salvo em: {saida_csv}")
    except Exception as e:
        print(f"Erro ao processar o CSV: {e}")


import sys
import pandas as pd

def main():
    if len(sys.argv) < 2:
        print('Uso: python dd-mm-yy_replace.py <arquivo_csv>')
        sys.exit(1)
    import os
    arquivo_csv = sys.argv[1]
    arquivo_csv = os.path.abspath(arquivo_csv)
    try:
        df = pd.read_csv(arquivo_csv, delimiter=';')
        for coluna in df.columns:
            if 'data' in coluna.lower():
                df[coluna] = df[coluna].apply(converter_data)
        for col in df.columns:
            df[col] = df[col].apply(lambda x: f'"{str(x).strip().replace(chr(34), "")}"')
        df.to_csv(arquivo_csv, index=False, sep=';')
        print(f"CSV processado e salvo em: {arquivo_csv}")
    except Exception as e:
        print(f"Erro ao processar o CSV: {e}")

if __name__ == '__main__':
    main()
