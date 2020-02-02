# [Gordinho?, PerninhaCurta?, FazAuAu? ]
# AQUI DIFINIMOS AS VARIAVEIS RELATIVAS AS CARACTERISCAS DOS ANIMAIS
porco1 = 	[1, 1, 0]
porco2 = 	[1, 1, 0]
porco3 = 	[1, 1, 0]
cachorro1 = [1, 1, 1]
cachorro2 = [0, 1, 1]
cachorro3 = [0, 1, 1]

dados = [porco1, porco2, porco3, cachorro1, cachorro2, cachorro3]

marcacoes = [1, 1, 1, -1, -1, -1]

from sklearn.naive_bayes import MultinomialNB

# TREINANDO O MODELO 
modelo = MultinomialNB()
modelo.fit(dados, marcacoes)

misterioso = [1, 1, 1]
misterioso2 = [1, 0, 0]
misterioso3 = [0, 0, 2]

# ARREY COM TESTES
teste = [misterioso, misterioso2, misterioso3]

# MARCACAO DOS ARRAYS DE TESTE
marcacoes_teste = [-1, 1, 1]

# GUARDANDO O RESULTADO DO RESTE
resultado = modelo.predict(teste)

diferencas = resultado - marcacoes_teste

acertos = [d for d in diferencas if d == 0]

total_de_acertos = len(acertos)
total_de_elementos = len(teste)

taxa_de_acerto = 100.0 * total_de_acertos / total_de_elementos


# IMPRIMINDO OS TESTES
print(resultado)
print(diferencas)
print(taxa_de_acerto)


