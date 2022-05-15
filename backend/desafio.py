from exception import NomeNaoLocalizado
from grafo import grafo
#import networkx as nx
#import matplotlib.pyplot as plt

#grafo = nx.Graph()

#grafo.add_node('Ana')

#nx.draw(grafo, with_labels = True)

#dict_amigos = {}
#dict_amigos['Ana'] = ['Maria','Vinicius','Carlos','João']
#dict_amigos['Maria'] = ['Ana','Vinicius']
#dict_amigos['Vinicius'] = ['Ana','Maria']
#dict_amigos['Luiza'] = ['João']
#dict_amigos['João'] = ['Ana','Luiza']
#dict_amigos['Carlos'] = ['Ana']
#dict_amigos['Luiza'] = ['']

dict_amigos = {
            'Ana': ['Maria','Vinicius','Carlos','João'],
            'Maria': ['Ana','Vinicius'],
            'Vinicius': ['Ana','Maria'],
            'Luiza': ['João'],
            'João': ['Ana','Luiza'],
            'Carlos': ['Ana']
}

lista_grafo = grafo(dict_amigos)
print(lista_grafo)
print(lista_grafo.listar_grafo())
pessoa = 'Carlos'
try:
    amigos = lista_grafo.lista_amigos(pessoa)
    print(f'Os amigos de {pessoa} são: ', [amigo for amigo in amigos if amigo != pessoa], '\n')
except NomeNaoLocalizado as excecao:
    print(excecao)
try:    
    nivel2 = lista_grafo.lista_nivel2(pessoa)
    print(f'As pessoas de nível 2 da(o) {pessoa} são: ', [nivel for nivel in nivel2], '\n')
except NomeNaoLocalizado as excecao:
    print(excecao)
try:
    novapessoa = input('Informe o nome da pessoa: ')
    amigo = input('Informe no nome do amigo: ')
    lista_grafo.adicionar_amigo(novapessoa,amigo)
    print(lista_grafo.adj)
except NomeNaoLocalizado as excecao:
    print(excecao)
