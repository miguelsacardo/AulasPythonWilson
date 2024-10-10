#define a compra como aberta
compraAberta = True

#lista de produtos
listaProdutos = {}

#informações do produto
tamanhoLista = 0
nomeProduto = ""
valorProduto = 0.0
quantidadeProduto = 0

#contador
i = 0

#esse while representará o sistema de compra
while compraAberta == True:

    #opções do usuário
    opcoesUsuario = int(input("O que você deseja? \n Opção 1 - Adicionar produtos ao carrinho \n Opção 2 - Visualizar o carrinho \n Opção 3 - Calcular o total \n Opção 4 - Finalizar a compra \n Digite uma opção: "))

    match opcoesUsuario:
        case (1):
                #usuário informa o tamanho da lista que deseja
                tamanhoLista = int(input("Quantos itens sua lista terá? (Sua lista deve ter pelo menos 3 itens."))

                if tamanhoLista != 3:
                    print("A lista deve ter pelo menos três produtos.")
                else:
                    #o usuário informa aqui as informações do produto
                    nomeProdutos = input("Digite o nome do produto: ")
                    valorProduto = float(input("Digite um valor para o produto: "))
                    quantidadeProduto = int(input("Digite a quantidade desse produto que você deseja: "))

                    #adicionando as variáveis a lista de produtos
                    listaProdutos[nomeProdutos]=valorProduto,quantidadeProduto


                for nome, preco in listaProdutos.items():
                    print(nome, preco)




