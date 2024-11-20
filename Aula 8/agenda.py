def menu():
	print("1- Cadastrar amigo (no final da lista)\n"
		  "2- Mostrar os nomes de todos os amigos\n"
		  "3- Cadastrar um amigo (no início da lista)\n"
		  "4- Remover um nome\n"
		  "5- Substituir um nome\n"
		  "6- Mostrar o número total de amigos cadastrados\n"
		  "7- Colocar os nomes dos amigos em ordem alfabética\n"
		  "9- Sair do programa")
	op = int(input("Opção Selecionada: "))
	while op < 1 or op > 9:
		op = int(input("Opção Selecionada: "))
	return op

def inserirAmigo(amigo):
	nome = input("Nome: ")
	amigo.append(nome)

def mostrarNomes(amigo):
	print(amigo)

def inserirAmigoFinal(amigo):
	nome = input("Digite um Nome: ")
	amigo.insert(0, nome)

def removerAmigo(amigo):
	nome = input("Qual o nome a ser removido: ")
	for i in range(len(amigo)):
		if amigo[i] == nome:
			del amigo[i]
			break

def substituirNome(amigo):
	nome = input("Qual o nome a ser substituído: ")
	nomeNovo = input("Qual o novo nome: ")
	for i in range(len(amigo)):
		if amigo[i] == nome:
			amigo[i] = nomeNovo
			break

def totalCadastro(amigo):
	print("Total de amigos = %d" % len(amigo))

def ordenarAmigos(amigo):
	amigo.sort()
	mostrarNomes(amigo)

def main():
	amigo = []
	while True:
		op = menu()
		if op == 1:
			inserirAmigo(amigo)
		elif op == 2:
			mostrarNomes(amigo)
		elif op == 3:
			inserirAmigoFinal(amigo)
		elif op == 4:
			removerAmigo(amigo)
		elif op == 5:
			substituirNome(amigo)
		elif op == 6:
			totalCadastro(amigo)
		elif op == 7:
			ordenarAmigos(amigo)
		elif op == 9:
			break

main()
