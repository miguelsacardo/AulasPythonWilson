stringUsuario = str(input("Digite um texto para ele ser incriptado: "))

#criptografando uma string de acordo com seu valor na tabela ASCII
#e somando 128 ao valor (HASH128)
list = []


for i in stringUsuario:
    cript = ord(i) + 128
    # print("Encriptação com ORD(): ", cript)
    print("Encriptando com ORD(): ",cript," " ,"Passando o ORD para CHR(): ", chr(cript))
    list.append(cript)

#decodificação - uso uma função oposta ao ord() e diminui 128 para encontrar o valor correto
for decode in list:
    print(chr(decode - 128))
