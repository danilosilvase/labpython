# Math operation in pyton

# Soma
1 + 1

# Multiplicacao
1 * 3

# Divisao
1 / 2

# Potenciacao
3 ** 2

# Funcao type - sample 1
# Retorna o tipo do objeto colocado como argumento
type(1)

# Funcao type - sample 2

# Mod %
5 % 2

# Expressoes com operacoes basicas
(3 / 2) * (4 +1)

# Definicao de variaveis
# Obs. Variavies nao iniciam com numeros ou caracteres especais
# Sao case sensitive
#Exemplo 1

string = 'nome da variavel'
print(string)
type(string)


#Imprimindo

var = "Danilo"
idade = 34
print('nome_da_variavel: Meu nome é {one} e tenho {two} anos de idade'.format(one=var, two=idade))

# Listas
# Exemplo

lista = [1, 2, 3]
type(lista)

lista = ['a', 'b', 'c']
type(lista)
lista[2]

# Listas permitem todo tipo de valor, inclusive outra lista

lista2 = [1, 2 ,3 , ['a', 'b', 'c']]
print(lista2)
lista2[3]

#Imprimindo lista

# exemplo com range (inicio : fim)

lista = [1, 2 ,3 , ['a', 'b', 'c']]

#imprimindo "a partir de..."
lista[2:] # irah imprimir a partir do indice 2

#imprimindo "ateh..."
lista[:2] # irah imprimir ateh o indice 2

#imprimindo "a partir de... ateh ..."
lista[1:3] 

#A impressao de uma string se assemelha a lista
#Exemplo
string='nome'
string[3]

#Nested list
lista=[1, 2, 3, ['a', 'b', 'c']]

#Dicionario
#lista relacionada com chave/valor
#Exemplo 1
dic= {'valor1':1, 'valor2':2}
print(dic)

type(dic)

#Imprimindo dicionario
#
dic['valor2'] # Imprime a chave e ele retorna o valor

#exemplo2

lista = {'valor1':['a', 'b', 'c'], 'valor2':[1, 2 ,3]}

# imprindo um dicionario e definindno um valor da lista

lista['valor1'][2]

# Tupla
# A tupla eh um objeto imutavel / 'tuple' object does not support item assignment
#Exemplo

tupla =  (1, 2, 3)
type(tupla)
tupla[1]

# tentando alterar valor da tupla e gerando erro "'tuple' object does not support item assignment"
tupla[1] = 2


# Operacoes logicas

# Booleno

True
False

# O resultado de 'X eh igual a Y?
1 == 2 # O valor retornarah true/false

# Maior que

1 > 2

# Menor que

2 < 4

# Maior ou igual a

3 >= 2

# Menor ou igual a

2 <= 4

#diferente

# Operador 'and'
x =1
(x == 1)

(x == 1) and (x <= 0) # este resultado retorna falso

# Operador 'or'

# Condicionais
# if

y = 'Reprovado'
x = 8

if x < 7:
    y = 'Aprovado'
    print(y)

# Else

y = 'Reprovado'
x = 8

if x > 7:
    y = 'Aprovado'
    print(y)
else:
    print(y)

# Elif
# Basicamente um segundo if, ele permite a criacao de condicoes intermediarias
# comparando os profixmos valores com o da primeira condicao. 

y = 'Reprovado'
x = 4

if x > 7:
    y = 'Aprovado'
    print(y)
elif x > 5:
    y = 'Quase lah'
    print(y)
elif x > 4:
    y = 'recuperacao'
    print(y)
else:
    print(y)




