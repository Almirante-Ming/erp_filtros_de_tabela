import csv
# separe a coluna de ncm em um csv separado para conferir.

def carregar_ncms_validos(arquivo_ncms_validos):
    ncms_validos = set()
    with open(arquivo_ncms_validos, newline='') as f:
        reader = csv.reader(f)
        for row in reader:
            if row:
                ncms_validos.add(row[0].strip())
    return ncms_validos

def processar_ncms(arquivo_entrada, ncms_validos, arquivo_saida):
    with open(arquivo_entrada, newline='') as f_entrada, open(arquivo_saida, 'w', newline='') as f_saida:
        reader = csv.reader(f_entrada)
        writer = csv.writer(f_saida)
        
        for row in reader:
            if row:  
                ncm = row[0].strip()
                if ncm not in ncms_validos or len(ncm) != 8:
                    writer.writerow(['00000000'])
                else:
                    writer.writerow([ncm])

arquivo_ncms_validos = 'ncms_validos.csv'
arquivo_entrada = 'input.csv'
arquivo_saida = 'output.csv'

ncms_validos = carregar_ncms_validos(arquivo_ncms_validos)
processar_ncms(arquivo_entrada, ncms_validos, arquivo_saida)
print(f"Processamento concluído. O resultado foi escrito em '{arquivo_saida}'")
