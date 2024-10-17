#define a compra como aberta
compraAberta = True

#lista de produtos
listaProdutos = {}
listaUsuario = [] #adiciona a lista de produtos para uma lista, para cadastrar vários

#valor total da compra
valorTotalCompra = 0

#esse while representará o sistema de compra
while compraAberta == True:

    #opções do usuário
    opcoesUsuario = int(input("O que você deseja? \n Opção 1 - Adicionar produtos ao carrinho \n Opção 2 - Visualizar o carrinho \n Opção 3 - Calcular o total \n Opção 4 - Finalizar a compra \n Digite uma opção:\n "))

    match opcoesUsuario:
        case (1):
                #usuário informa o tamanho da lista que deseja
                tamanhoLista = int(input("Quantos itens sua lista terá? (Sua lista deve ter pelo menos 3 itens:\n"))

                #checa o tamanho da lista que o usuário quer. Para o exercício, pelo menos três itens a lista deve ter
                if tamanhoLista < 3:
                    print("A lista deve ter pelo menos três produtos.\n")
                else:
                    # contador
                    i = 0 #o contador deve ser declarado aqui pois ele será definido como 0 sempre que a escolha do usuário cair aqui. Se fosse declarado em cima, o loop ia parar pois i não ia ser definido como 0 novamente.
                    print("=" * 40)

                    #pede os produtos enquanto o contador for menor que o tamanhho da lista
                    while i < tamanhoLista:

                        #o usuário informa aqui as informações do produto
                        listaProdutos['Produto'] = str(input("Digite o nome do produto: "))
                        listaProdutos['Valor do produto'] = float(input("Digite o valor do produto: "))
                        listaProdutos['Quantidade'] = int(input("Digite a quantidade do produto: "))

                        print("=" * 40)

                        #calcular o valor total dessa lista
                        valorTotal = listaProdutos['Valor do produto'] * listaProdutos['Quantidade']
                        valorTotalCompra += valorTotal

                        listaProdutos['Valor Total por Produto'] = valorTotal
                        listaUsuario.append(listaProdutos.copy())
                        # print(f"O valor total da compra é: {valorTotalCompra}")
                        #incrementar o contador do loop
                        i += 1

                    # exibe um aviso ao usuário de que a lista foi feita com sucesso
                    print("Sua lista foi feita com sucesso!\n")

        case(2):
            print("=" * 90)

            if listaUsuario == []:
                print("O carrinho está vazio.\n")
            else:
                #exibe ao usuário que ele está vendo o carrinho atual
                print("Aqui está seu carrinho atual:\n")

                #exibe o carrinho para o usuário
                for listaItens in listaUsuario:
                    print(listaItens)

                print("=" * 90, "\n")

                excluirProduto = str(input("Deseja excluir algum produto? [S/N]\n")).upper()[0]
                if excluirProduto == "S":
                    nomeProduto = str(input("Digite o nome do produto que você quer excluir da lista: "))

                    #conta os itens da listaUsuario
                    for itens in listaUsuario:
                            if itens['Produto'] != nomeProduto: #verifica se o produto que o usuário digitou existe
                                print("O produto informado não está na sua lista.\n")

                            elif itens['Produto'] == nomeProduto: #compara o nome do produto com o nome informado pelo usuário

                                #exclui o item que o usuário informa
                                listaUsuario.remove(itens)
                                print("Produto excluído com sucesso!\n")

                                #diminui do valor total da compra o valor do item que foi removido
                                valorTotalCompra = valorTotalCompra - itens['Valor Total por Produto']
                                break
                elif excluirProduto == "N":
                    continue
                else:
                    print("Digite apenas [S/N].\n")
        case(3):
            print("=" * 90)

            #checa se o carrinho está vazio
            if listaUsuario == []:
                print("O carrinho está vazio, faça sua lista de compras para calcular o total.\n")
            else:
                print(f"O valor total da sua compra é: {valorTotalCompra}\n") #mostra o valor total da compra pro usuário

        case(4):

            print("Sua compra foi finalizada!")

            #criar recibo em txt
            with open("Recibo da sua compra", "a",encoding='utf8') as recibo:

                recibo.write("Seu carrinho: \n")

                # exibe o carrinho para o usuário
                for listaItens in listaUsuario:
                    recibo.write(f"{listaItens} \n")

                recibo.write(f"Valor total da compra: {valorTotalCompra} \n")

            #limpa o carrinho e para o loop
            listaUsuario.clear()
            compraAberta = False





