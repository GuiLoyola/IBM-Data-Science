palavra = 'guilherme Gosta de Paçoca Molhadinha'
print(f'capitalize da string "{palavra}": ',palavra.capitalize())#Coloca a primeira letra Maiúscula, % minúsculo
print('casefold: ',palavra.casefold())# Transforma todas as letra em minúsculas 
print(palavra.count(' '))#conta os elementos passados no parâmetro
print(palavra.find('e'))#retorna a posição do elemento em parâmetro
palavra_2 = 'Gui131201'
palavra_3 = 'Gui'
print(palavra_2.isalnum())#Verifica se o texto é todo feito com caracteres alfanuméricos/bool
print(palavra_3.isalnum())# / /
print(palavra_2.isalpha())#verifica se o texto é somente composto d letras/bool
numero = '6745'
print(numero.isnumeric())#verifica se o texto é composto só de dígitos/bool
print(palavra.replace('Paçoca Molhadinha', 'Bolo Molhadinho'))#substitui elementos/palavras do texto
print(palavra_2.split('13'))#Separa de acordo com o parâmetro delimitador
texto = '''Senhoras e senhores 
venho vos apresentar o 
splitlines''' #usando 3 áspas para fazer um comentário com parágrafos
print(texto.splitlines()) #função separa em uma lista texto pelos enters
print(palavra.startswith('Paçoca'))#testa se texto começa com certos elementos passados no parâmetro
teste = 'Eu amo estudar programação 1 é demais '
print(teste.strip())#por padrão retira espaços extras no texto
print(palavra.title()) # coloca a primeira letra de cada palavra no texto em maiúscula
print(palavra.upper()) # todo o texto maiúscula



