import csv

def carregar_acessos():
	X = []
	Y = []

	arquivo = open ('acesso.csv', 'rb')
	leitor = csv.reader(arquivo)

	next(leitor)

	for home, como_funciona, contato, comprou in leitor:
		dado = [int(home),int(como_funciona), int(contato), int(comprou) ]
		X.append(dado)
		Y.append(comprou)

	return X, Y