"""
Faça uma lista de comprar com listas
O usuário deve ter a possibilidade de
inserir, apagar e listar valores da sua lista
Não permita que o programa quebre com 
erros de índices inexistentes na lista.

"""
lista = []

while True:
    print('Selecione uma opção')
    opcao = input('[i]nserir [a]pagar [l]istar: ')
    
    if opcao == 'i':
        produto = input('Produto: ')
        lista.append(produto)

    elif opcao == 'a':
        indice = input('Índice que você apagar: ')
        try:
            numIndice = int(indice)
            del lista[numIndice]
        except ValueError:
            print('Por favor digite número int.')
        except IndexError:
            print('Índice não existe na lista')
        except Exception:
            print('Erro desconhecido')

    elif opcao == 'l':
        if len(lista) == 0:
            print('Nada para listar')

        for indice, produto in enumerate(lista):
            print(indice, produto)
    else: 
        print('Por favor, escolha i, a ou l.')

