import tkinter as tk
from tkinter import filedialog, messagebox
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

class App:
    def __init__(self, root):
        self.root = root
        self.root.title('ERP Filtros de Tabela - Processador CSV')
        self.csv_path = tk.StringVar()
        self.check_vars = [tk.BooleanVar() for _ in PROCESS_SCRIPTS]
        self.all_var = tk.BooleanVar()

        tk.Label(root, text='Selecione o arquivo CSV para processar:').pack(anchor='w')
        file_frame = tk.Frame(root)
        file_frame.pack(fill='x')
        tk.Entry(file_frame, textvariable=self.csv_path, width=60).pack(side='left', fill='x', expand=True)
        tk.Button(file_frame, text='Procurar', command=self.browse_file).pack(side='left')

        tk.Label(root, text='Escolha o(s) processo(s) a aplicar:').pack(anchor='w')
        for i, (name, _) in enumerate(PROCESS_SCRIPTS):
            tk.Checkbutton(root, text=name, variable=self.check_vars[i]).pack(anchor='w')
        tk.Checkbutton(root, text='Aplicar todos', variable=self.all_var, command=self.toggle_all).pack(anchor='w')

        btn_frame = tk.Frame(root)
        btn_frame.pack(fill='x', pady=5)
        tk.Button(btn_frame, text='Processar', command=self.process).pack(side='left')
        tk.Button(btn_frame, text='Sair', command=root.quit).pack(side='left')

        self.output = tk.Text(root, height=20, width=80)
        self.output.pack(fill='both', expand=True)

    def browse_file(self):
        file_path = filedialog.askopenfilename(filetypes=[('CSV Files', '*.csv')])
        if file_path:
            self.csv_path.set(file_path)

    def toggle_all(self):
        for var in self.check_vars:
            var.set(self.all_var.get())

    def process(self):
        csv_path = self.csv_path.get()
        if not csv_path or not os.path.isfile(csv_path):
            messagebox.showerror('Erro', 'Por favor, selecione um arquivo CSV válido.')
            return
        selected = [i for i, var in enumerate(self.check_vars) if var.get()]
        if not selected:
            messagebox.showerror('Erro', 'Selecione pelo menos um processo.')
            return
        self.output.delete(1.0, tk.END)
        input_file = csv_path
        base, ext = os.path.splitext(csv_path)
        for idx, i in enumerate(selected):
            name, script = PROCESS_SCRIPTS[i]
            output_file = f"{base}_mod{idx+1}{ext}"
            self.output.insert(tk.END, f'Executando: {name}...\n')
            result = subprocess.run(['python3', script, input_file, output_file], capture_output=True, text=True)
            self.output.insert(tk.END, result.stdout + '\n' + result.stderr + '\n')
            input_file = output_file
        self.output.insert(tk.END, f'Processamento concluído. Arquivo final: {input_file}\n')

def main():
    root = tk.Tk()
    app = App(root)
    root.mainloop()

if __name__ == '__main__':
    main()
