import csv
import unicodedata
import codecs

def remover_acentos(txt):
    return ''.join((c for c in unicodedata.normalize('NFD', txt) if unicodedata.category(c) != 'Mn'))

def substituir_caracteres_portugueses(texto):
    # Dicionário de substituição de caracteres
    substituicoes = {
        'ç': 'c', 'Ç': 'C',
        'ã': 'a', 'Ã': 'A',
        'á': 'a', 'à': 'a', 'â': 'a', 'ä': 'a', 'Á': 'A', 'À': 'A', 'Â': 'A', 'Ä': 'A',
        'é': 'e', 'è': 'e', 'ê': 'e', 'ë': 'e', 'É': 'E', 'È': 'E', 'Ê': 'E', 'Ë': 'E',
        'í': 'i', 'ì': 'i', 'î': 'i', 'ï': 'i', 'Í': 'I', 'Ì': 'I', 'Î': 'I', 'Ï': 'I',
        'ó': 'o', 'ò': 'o', 'ô': 'o', 'ö': 'o', 'Ó': 'O', 'Ò': 'O', 'Ô': 'O', 'Ö': 'O',
        'ú': 'u', 'ù': 'u', 'û': 'u', 'ü': 'u', 'Ú': 'U', 'Ù': 'U', 'Û': 'U', 'Ü': 'U',
        'ñ': 'n', 'Ñ': 'N'
        # Adicione mais caracteres conforme necessário
    }
    
    # Aplicar as substituições
    for original, substituto in substituicoes.items():
        texto = texto.replace(original, substituto)
    
    return texto

def processar_csv_gerar_novo(input_csv, output_csv):
    with codecs.open(input_csv, 'r', encoding='windows-1252') as csv_input, \
         codecs.open(output_csv, 'w', encoding='utf-8') as csv_output:
        
        reader = csv.reader(csv_input)
        writer = csv.writer(csv_output)
        
        for row in reader:
            novo_row = [substituir_caracteres_portugueses(remover_acentos(col)) for col in row]
            writer.writerow(novo_row)

# Exemplo de uso:
if __name__ == '__main__':
    arquivo_csv_original = './export.csv'
    novo_arquivo_csv = './arquivo_modificado.csv'
    
    processar_csv_gerar_novo(arquivo_csv_original, novo_arquivo_csv)
    
    print(f'Arquivo CSV modificado gerado em: {novo_arquivo_csv}')
