from exception import NomeNaoLocalizado
from grafo import grafo
import sys
dict_amigos = {
            'Ana': ['Maria','Vinicius','Carlos','João'],
            'Maria': ['Ana','Vinicius'],
            'Vinicius': ['Ana','Maria'],
            'Luiza': ['João'],
            'João': ['Ana','Luiza'],
            'Carlos': ['Ana']
}

lista_grafo = grafo(dict_amigos)

args = sys.argv[1]
#while True:
#    message = sys.stdin.read()
#    sys.stdout.write('Olá Node! Recebi sua mensagem: ' + message)
#    sys.stdout.flush()
#message = json.loads(message)
#args = message['args']

#response = {}

sys.stdout.reconfigure(encoding='utf-8')
try:
    if args == 'listargrafo':
        result = print(lista_grafo.listar_grafo())
    if args == 'listaramigos':
        result = print(lista_grafo.lista_amigos(sys.argv[2]))
    if args == 'listarnivel2':
        result = print(lista_grafo.lista_nivel2(sys.argv[2]))
    if args == 'cadastropessoa':
        result = print(lista_grafo.adicionar_amigo(sys.argv[2],sys.argv[3]))
    sys.response['data'] = result
except Exception as e:
    sys.response['data'] = str(e)

#response = json.dumps(response)
#stdout.write('teste')
#stdout.flush()
#print(lista_grafo.listar_grafo())
#pessoa = 'Carlos'
#try:
#    amigos = lista_grafo.lista_amigos(pessoa)
#    print(f'Os amigos de {pessoa} são: ', [amigo for amigo in amigos if amigo != pessoa], '\n')
#except NomeNaoLocalizado as excecao:
#    print(excecao)
#try:    
#    nivel2 = lista_grafo.lista_nivel2(pessoa)
#    print(f'As pessoas de nível 2 da(o) {pessoa} são: ', [nivel for nivel in nivel2], '\n')
#except NomeNaoLocalizado as excecao:
#    print(excecao)
#try:
#    novapessoa = input('Informe o nome da pessoa: ')
#    amigo = input('Informe no nome do amigo: ')
#    lista_grafo.adicionar_amigo(novapessoa,amigo)
#    print(lista_grafo.adj)
#except NomeNaoLocalizado as excecao:
#    print(excecao)
