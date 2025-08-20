import csv

def carregar_ncms_validos(arquivo_ncms_validos):
    ncms_validos = set()
    import os
    ncms_path = os.path.join(os.path.dirname(__file__), arquivo_ncms_validos) if not os.path.isabs(arquivo_ncms_validos) else arquivo_ncms_validos
    with open(ncms_path, newline='') as f:
        reader = csv.reader(f)
        for row in reader:
            if row:
                ncms_validos.add(row[0].strip())
    return ncms_validos

def processar_ncms_multicol(arquivo_entrada, ncms_validos, arquivo_saida, ncm_col_name='ncm'):
    import os
    entrada_path = os.path.abspath(arquivo_entrada)
    invalidos_path = os.path.join(os.path.dirname(entrada_path), 'invalidos.csv')
    with open(entrada_path, newline='') as f_entrada, \
         open(invalidos_path, 'w', newline='') as f_invalidos:
        reader = csv.reader(f_entrada, delimiter=';')
        writer_invalidos = csv.writer(f_invalidos, delimiter=';')
        rows = []
        header = next(reader)
        ncm_idx = None
        for i, col in enumerate(header):
            if col.strip().lower() == ncm_col_name.lower():
                ncm_idx = i
                break
        if ncm_idx is None:
            raise Exception(f"Coluna '{ncm_col_name}' não encontrada no arquivo CSV.")
        rows.append([col.strip() for col in header])
        writer_invalidos.writerow([col.strip() for col in header])
        for row in reader:
            if not row or len(row) <= ncm_idx:
                formatted_row = [f'"{cell.strip().replace("\"","")}"' for cell in row]
                rows.append(formatted_row)
                writer_invalidos.writerow(formatted_row)
                continue
            ncm = row[ncm_idx].strip().replace('"','').replace("'",'')
            is_invalid = ncm not in ncms_validos or len(ncm) != 8
            if is_invalid:
                row[ncm_idx] = '00000000'
            formatted_row = [f'"{cell.strip().replace("\"","")}"' if i != ncm_idx else f'"{row[ncm_idx]}"' for i, cell in enumerate(row)]
            rows.append(formatted_row)
            if is_invalid:
                original_row = [f'"{cell.strip().replace("\"","")}"' for cell in row]
                writer_invalidos.writerow(original_row)
    with open(entrada_path, 'w', newline='') as f_saida:
        writer = csv.writer(f_saida, delimiter=';')
        writer.writerows(rows)

if __name__ == '__main__':
    import sys
    if len(sys.argv) < 2:
        print('Uso: python conferir_ncm.py <arquivo_csv>')
        sys.exit(1)
    arquivo_ncms_validos = 'ncms_validos.csv'
    arquivo_entrada = sys.argv[1]
    ncms_validos = carregar_ncms_validos(arquivo_ncms_validos)
    processar_ncms_multicol(arquivo_entrada, ncms_validos, arquivo_entrada)
    print(f"Processamento concluído. O resultado foi escrito em '{arquivo_entrada}' e inválidos em 'invalidos.csv' na mesma pasta.")
