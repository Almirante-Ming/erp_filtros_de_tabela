import PySimpleGUI as sg
import subprocess
import os

PROCESS_SCRIPTS = [
    ('Corrigir Data', 'corrigir_data/datas.py'),
    ('DD-MM-YY Replace', 'corrigir_data/dd-mm-yy_replace.py'),
    ('Conferir NCM', 'corrigir_ncm/conferir_ncm.py'),
    ('Corrigir Encoding', 'encoding/corrigir_encoding.py'),
    ('Char Replace', 'regex_replace/char_replace.py'),
]

def run_script(script_path, csv_path):
    try:
        result = subprocess.run(['python3', script_path, csv_path], capture_output=True, text=True)
        return result.stdout + '\n' + result.stderr
    except Exception as e:
        return str(e)

def main():
    sg.theme('SystemDefault')
    layout = [
        [sg.Text('Selecione o arquivo CSV para processar:')],
        [sg.Input(key='-CSV-', enable_events=True), sg.FileBrowse(file_types=(('CSV Files', '*.csv'),))],
        [sg.Text('Escolha o(s) processo(s) a aplicar:')],
    ]
    for i, (name, _) in enumerate(PROCESS_SCRIPTS):
        layout.append([sg.Checkbox(name, key=f'-PROC{i}-')])
    layout += [
        [sg.Checkbox('Aplicar todos', key='-ALL-')],
        [sg.Button('Processar'), sg.Button('Sair')],
        [sg.Output(size=(80, 20))]
    ]
    window = sg.Window('ERP Filtros de Tabela - Processador CSV', layout)

    while True:
        event, values = window.read()
        if event in (sg.WIN_CLOSED, 'Sair'):
            break
        if event == '-ALL-':
            for i in range(len(PROCESS_SCRIPTS)):
                elem = window[f'-PROC{i}-']
                if elem is not None:
                    elem.update(values['-ALL-'])
        if event == 'Processar':
            csv_path = values['-CSV-']
            if not csv_path or not os.path.isfile(csv_path):
                print('Por favor, selecione um arquivo CSV válido.')
                continue
            selected = [i for i in range(len(PROCESS_SCRIPTS)) if values.get(f'-PROC{i}-')]
            if not selected:
                print('Selecione pelo menos um processo.')
                continue
            for i in selected:
                name, script = PROCESS_SCRIPTS[i]
                print(f'Executando: {name}...')
                output = run_script(script, csv_path)
                print(output)
            print('Processamento concluído.')
    window.close()

if __name__ == '__main__':
    main()
