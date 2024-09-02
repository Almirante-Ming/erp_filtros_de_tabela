def convert_date_format(date_str):
    # Remove caracteres não numéricos e espaços extras
    date_str = date_str.strip().replace('"', '')
    # Divide a data pelo caractere '-'
    parts = date_str.split('-')
    
    if len(parts) == 3:
        month, day, year = parts
        # Adiciona zeros à esquerda, se necessário, e retorna a data no novo formato "yyyy-mm-dd"
        day = f"{int(day):02d}"
        month = f"{int(month):02d}"
        year = f"{int(year):04d}"
        return f"{year}-{month}-{day}"
    else:
        print(f"Formato de data não reconhecido: {date_str}")
    return date_str

def process_file(input_file, output_file):
    with open(input_file, 'r') as file:
        lines = file.readlines()

    converted_lines = []
    for line in lines:
        line = line.strip()
        if line:  # Ignora linhas vazias
            converted_date = convert_date_format(line)
            converted_lines.append(converted_date)
            print(f"Convertido: {line} -> {converted_date}")

    with open(output_file, 'w') as file:
        for line in converted_lines:
            file.write(line + '\n')

# Use os caminhos dos seus arquivos aqui
input_file = 'datas.txt'
output_file = 'datas_convertidas.txt'

process_file(input_file, output_file)
print("Conversão concluída e salva em", output_file)
