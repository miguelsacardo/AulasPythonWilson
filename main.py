v1:int = 5 #numeros inteiros
v2 = "Hello World" #string, precisa estar entre aspas
v3 = 5.5 #float, precisa ser separado por "."
v4 = True #bool, verdadeiro ou falso
#o python identifica automaticamente o valor de uma variável

"""print(type(v1)) #tipe = mostra tipo de uma variável
print(type(v2))
print(type(v3))
print(type(v4))"""

#não pode espaço nas variáveis
#criar a variável: nome que condiz com a função da variável


#formatos de print
area_bosch = "ETS"
idade = 65
print(area_bosch, "POSSUI", idade, "anos de tradição")

#python 2 print
print("{} POSSUI {} ANOS DE TRADIÇÃO".format(area_bosch,idade))

#python 3 print
print(f"{area_bosch} POSSUI {idade} ANOS DE TRADIÇÃO")

#imprimir data
dia = 7
mes = 9
ano = 2002

print(f"{dia:02d}/{mes:02d}/{ano:04d}")
