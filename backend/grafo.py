from exception import NomeNaoLocalizado
class grafo(object):
    def __init__(self,arestas):
        self.adj = {}
        self.arestas = arestas
        self.relacao_amigos = {}
        self.adiciona_arestas(arestas)

    def cria_aresta(self, chave, valor):

        if chave not in list(self.adj.keys()):
            self.adj[chave] = valor
        else:
            if valor not in self.adj[chave]:
                self.adj[chave].append(valor)                


    def adiciona_arestas(self, arestas):

        for chave, valor in arestas.items():
            self.cria_aresta(chave, valor)

    def lista_amigos(self,pessoa):
        if pessoa in list(self.adj.keys()):
            listagem_amigos = self.adj[pessoa]
        else:
            raise NomeNaoLocalizado
        
        return listagem_amigos
    
    def lista_nivel2(self,pessoa):
        listagem_nivel2 = []
        for chave, valor in self.arestas.items():
            if pessoa not in self.arestas[chave] and pessoa != chave and pessoa in list(self.adj.keys()):
                listagem_nivel2.append(chave)
        if listagem_nivel2 == []:
            raise NomeNaoLocalizado('Nome existe nomes a serem listados')
        else:
            return listagem_nivel2

    def listar_grafo(self):
        return list(self.adj.keys())
    
    def adicionar_amigo(self,pessoa,amigo):
        if amigo not in list(self.adj.keys()):
            raise NomeNaoLocalizado('Amigo não localizado !')
        else:
            self.adj[amigo].append(pessoa)
            return f'Nome Adicionado'

    def __str__(self):
        return f'Grafo({self.adj})'