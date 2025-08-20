import sys
import subprocess
import pandas as pd
import os

def main():
	if len(sys.argv) < 2:
		print('Uso: python corrigir_encoding.py <arquivo_csv>')
		sys.exit(1)
	arquivo_csv = sys.argv[1]
	subprocess.run([
		'python3',
		os.path.join(os.path.dirname(__file__), '../regex_replace/char_replace.py'),
		arquivo_csv
	])
	df = pd.read_csv(arquivo_csv, encoding='utf-8', delimiter=';')
	if isinstance(df, pd.DataFrame):
		df = df.applymap(lambda x: f'"{str(x).strip().replace(chr(34), "")}"') # type: ignore
	else:
		df = df.apply(lambda x: f'"{str(x).strip().replace(chr(34), "")}"')
	df.to_csv(arquivo_csv, index=False, encoding='utf-8', sep=';')
	print(f'Arquivo {arquivo_csv} alterado com sucesso')

if __name__ == '__main__':
	main()
