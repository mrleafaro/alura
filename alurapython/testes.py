numero = int(input("Digite um número: "))
if numero % 2 == 0:
    print(numero, "é par!")
else:
    print(numero, "é ímpar!")


idade = int(input("Digite sua idade: "))
if 0< idade <=12:
    print("Você é uma criança")

if 13 < idade <=18:
    print("Você é um adolescente maneiro😎")

if 18 < idade:
    print("você é um adulto chato😒")

print("Bem vindo ao programa onde odiamos os Pedros!")

usuario = input("Digite seu nome de usuário: ")
senha = input("Digite a senha do usuário: ")

if usuario == "Pedro":
    print("Você é um Pedro, não é bem vindo aqui!")
else:
    print("Bem vindo, não Pedro!")

if senha == "Pedro":
    print("Pedro não pode ser uma senha!")
else:
    print("Senha aceita, bem vindo não Pedro!")

nomes = ['Rafael', 'Henrique', 'Felipe']

nome = input("Digite seu nome: ")

nomes.append(nome)

for nome in nomes:
    print(f'-{nome}')

dicionario = [{"Nome": "Alex", "Idade": "20"}]

# Acessando o dicionário dentro da lista
dicionario[0]["Profissão"] = input("Digite uma nova profissão para Alex: ")

print(dicionario)
