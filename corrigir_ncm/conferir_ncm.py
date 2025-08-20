import csv

def carregar_ncms_validos(arquivo_ncms_validos):
    ncms_validos = set()
    with open(arquivo_ncms_validos, newline='') as f:
        reader = csv.reader(f)
        for row in reader:
            if row:
                ncms_validos.add(row[0].strip())
    return ncms_validos

def processar_ncms_multicol(arquivo_entrada, ncms_validos, arquivo_saida, ncm_col_name='ncm'):
    with open(arquivo_entrada, newline='') as f_entrada, \
         open('invalidos.csv', 'w', newline='') as f_invalidos:
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
        formatted_header = [f'"{col.strip().replace("\"","")}"' for col in header]
        rows.append(formatted_header)
        writer_invalidos.writerow(formatted_header)
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
    with open(arquivo_entrada, 'w', newline='') as f_saida:
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
    print(f"Processamento concluído. O resultado foi escrito em '{arquivo_entrada}' e inválidos em 'invalidos.csv'")
