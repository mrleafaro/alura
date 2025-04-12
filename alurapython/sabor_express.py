import os

lista_restaurantes = [{"Nome": "Pizza Palace", "Categoria": "Italiana", "Ativo": False},
                      {"Nome": "Sushi Temple", "Categoria": "Japonesa", "Ativo": True},
                      {"Nome": "Taco Mountain", "Categoria": "Mexicana", "Ativo": False}]

def nome_app():
    '''Essa função é responsável por exibir o título do aplicativo
    
    Output: título do aplicativo
    
    '''
    print("""
      ─▄▀▀▀▀▀▀▀▀▀▀▄▄
────▄▀▀░░░░░░░░░░░░░▀▄
──▄▀░░░░░░░░░░░░░░░░░░▀▄
──█░░░░░░░░░░░░░░░░░░░░░▀▄
─▐▌░░░░░░░░▄▄▄▄▄▄▄░░░░░░░▐▌
─█░░░░░░░░░░░▄▄▄▄░░▀▀▀▀▀░░█
▐▌░░░░░░░▀▀▀▀░░░░░▀▀▀▀▀░░░▐▌
█░░░░░░░░░▄▄▀▀▀▀▀░░░░▀▀▀▀▄░█
█░░░░░░░░░░░░░░░░▀░░░▐░░░░░▐▌
▐▌░░░░░░░░░▐▀▀██▄░░░░░░▄▄▄░▐▌
─█░░░░░░░░░░░▀▀▀░░░░░░▀▀██░░█
─▐▌░░░░▄░░░░░░░░░░░░░▌░░░░░░█
──▐▌░░▐░░░░░░░░░░░░░░▀▄░░░░░█
───█░░░▌░░░░░░░░▐▀░░░░▄▀░░░▐▌
───▐▌░░▀▄░░░░░░░░▀░▀░▀▀░░░▄▀
───▐▌░░▐▀▄░░░░░░░░░░░░░░░░█
───▐▌░░░▌░▀▄░░░░▀▀▀▀▀▀░░░█
───█░░░▀░░░░▀▄░░░░░░░░░░▄▀
──▐▌░░░░░░░░░░▀▄░░░░░░▄▀
─▄▀░░░▄▀░░░░░░░░▀▀▀▀█▀
▀░░░▄▀░░░░░░░░░░▀░░░▀▀▀▀▄▄▄▄▄
      ---SABOR EXPRESS---
""")

def reiniciar():
    input('\nDigite uma tecla para voltar ao menu principal: ')
    main()

def limpar_exibir(texto):
    '''Essa função é responsável por limpar os dados e exibir a tela inicial
    
    Output: título do aplicativo
    
    '''
    os.system('cls')
    linha = '*' * (len(texto))
    print(linha)
    print(texto)
    print(linha)
    print()

def cadastrar():
    '''Essa função é responsável por cadastrar os restaurantes
    
    Inputs:
    - Nome do restaurante
    - Categoria do restaurante

    Output:
    - Adiciona um novo restaurante a lista de restaurantes, assim como sua categoria
    
    '''
    limpar_exibir('--CADASTRO DE RESTAURANTES--')
    restaurante = input("Digite o nome do restaurante que deseja cadastrar: ")
    categoria = input(f"Digite a categoria do restaurante {restaurante}: ")
    dados = {"Nome": restaurante, "Categoria": categoria, "Ativo": False}
    lista_restaurantes.append(dados)
    print(f"O restaurante {restaurante} foi cadastrado com sucesso!")
    reiniciar()

def listar():
    '''Essa função é responsável por listar todos os restaurantes cadastrados
    
    Output: lista dos restaurantes cadastrados
    
    '''
    limpar_exibir('--LISTAGEM DE RESTAURANTES--')
    print(f"{'Nome do restaurante'.ljust(21)} | {'Categoria'.ljust(20)} | Status")
    for restaurante in lista_restaurantes:
        nome_restaurante = restaurante["Nome"]
        categoria = restaurante["Categoria"]
        ativo = "Ativado" if restaurante["Ativo"] else "Desativado"
        print(f"-{nome_restaurante.ljust(20)} | {categoria.ljust(20)} | {ativo}")
    reiniciar()


def exibir_opcoes():
    '''Essa função é responsável por exibir as opções de funcionalidades do aplicativo
    
    Output: opções de funcionalidades do aplicativo
    
    '''
    print('1. Cadastrar restaurante')
    print('2. Listar restaurante')
    print('3. Ativação do restaurante')
    print('4. Sair do app\n')

def encerrar():
    '''Essa função é responsável por encerrar o aplicativo
    
    Output: encerrar o app
    
    '''
    limpar_exibir('Encerrando o programa')

def opcao_invalida():
    '''Essa função é responsável por exibir um aviso caso uma opção inválida for digitada
    
    Output: mensagem de opção inválida
    
    '''
    print("Opção inválida\n")
    reiniciar()

def ativacao():
    '''Essa função é responsável por alternar o estado de ativação do restaurante, ativando-o ou desativando-o
    
    Input: nome do restaurante a ser ativado/desativado

    Output: ativação/desativação do restaurante
    
    '''
    limpar_exibir('--ATIVAÇÃO DE RESTAURANTES--')
    nome_restaurante = input("Digite o nome do restaurante que deseja ativar ou desativar: ")
    restaurante_encontrado = False
    for restaurante in lista_restaurantes:
        if nome_restaurante == restaurante["Nome"]:
            restaurante_encontrado = True
            restaurante["Ativo"] = not restaurante["Ativo"]
            mensagem = f'O restaurante {nome_restaurante} foi ativado com sucesso' if restaurante["Ativo"] else f'O restaurante {nome_restaurante} foi desativado com sucesso'
            print(mensagem)
    if not restaurante_encontrado:
        print("O restaurante não foi encontrado")        
    reiniciar()

def escolher_opcoes():
    '''Essa função é responsável por receber o valor que representa a opção desejada pelo usuário e funcionalizar tal opção
    
    Input: opção escolhida

    Output: funcionalização da opção escolhida
    
    '''
    try:
        opcao = int(input('Escolha uma das opções: '))

        if opcao == 1:
            cadastrar()
        elif opcao == 2:
            listar()
        elif opcao == 3:
            ativacao()
        elif opcao == 4:
            encerrar()
        else:
            opcao_invalida()
    except:
        opcao_invalida()
   

def main():
    '''Essa função é responsável por reiniciar e reexibir todas as funções iniciais do aplicativo
    
    Output: funções iniciais (título, opções etc)
    
    '''
    os.system("cls")
    nome_app()
    exibir_opcoes()
    escolher_opcoes()

if __name__ == '__main__':
    main()