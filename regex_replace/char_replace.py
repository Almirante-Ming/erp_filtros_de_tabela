import csv
import unicodedata
import sys

def remover_acentos(txt):
    return ''.join((c for c in unicodedata.normalize('NFD', txt) if unicodedata.category(c) != 'Mn'))

def substituir_caracteres_portugueses(texto):
    substituicoes = {
        '\u00e7': 'c', '\u00c7': 'C',
        '\u00e3': 'a', '\u00c3': 'A',
        '\u00e1': 'a', '\u00e0': 'a', '\u00e2': 'a', '\u00e4': 'a', '\u00c1': 'A', '\u00c0': 'A', '\u00c2': 'A', '\u00c4': 'A',
        '\u00e9': 'e', '\u00e8': 'e', '\u00ea': 'e', '\u00eb': 'e', '\u00c9': 'E', '\u00c8': 'E', '\u00ca': 'E', '\u00cb': 'E',
        '\u00ed': 'i', '\u00ec': 'i', '\u00ee': 'i', '\u00ef': 'i', '\u00cd': 'I', '\u00cc': 'I', '\u00ce': 'I', '\u00cf': 'I',
        '\u00f3': 'o', '\u00f2': 'o', '\u00f4': 'o', '\u00f6': 'o', '\u00d3': 'O', '\u00d2': 'O', '\u00d4': 'O', '\u00d6': 'O',
        '\u00fa': 'u', '\u00f9': 'u', '\u00fb': 'u', '\u00fc': 'u', '\u00da': 'U', '\u00d9': 'U', '\u00db': 'U', '\u00dc': 'U',
        '\u00f1': 'n', '\u00d1': 'N'
    }
    for original, substituto in substituicoes.items():
        texto = texto.replace(original, substituto)
    return texto

def processar_csv_inplace(csv_file):
    with open(csv_file, 'r', encoding='utf-8') as csv_input:
        reader = csv.reader(csv_input)
        rows = []
        for row in reader:
            novo_row = []
            for col in row:
                content = col.strip()
                if content.startswith('"') and content.endswith('"'):
                    content = content[1:-1]
                content = substituir_caracteres_portugueses(remover_acentos(content))
                novo_row.append(f'"{content}"')
            rows.append(novo_row)
    with open(csv_file, 'w', encoding='utf-8', newline='') as csv_output:
        writer = csv.writer(csv_output)
        writer.writerows(rows)

if __name__ == '__main__':
    if len(sys.argv) < 2:
        print('Uso: python char_replace.py <arquivo_csv>')
        sys.exit(1)
    processar_csv_inplace(sys.argv[1])
    print(f'Arquivo CSV modificado gerado em: {sys.argv[1]}')


