from exception import NomeNaoLocalizado
from grafo import grafo
import sys
import json
dict_amigos = {
            'Ana': ['Maria','Vinicius','Carlos','João'],
            'Maria': ['Ana','Vinicius'],
            'Vinicius': ['Ana','Maria'],
            'Luiza': ['João'],
            'João': ['Ana','Luiza'],
            'Carlos': ['Ana']
}

lista_grafo = grafo(dict_amigos)

while True:
    message = sys.stdin.readline()
    message = json.loads(message)
    args = message['args']
    response = {}

    sys.stdout.reconfigure(encoding='utf-8')
    try:
        if args[0] == 'listargrafo':
           result = lista_grafo.listar_grafo()
        elif args[0] == 'listaramigos':
          result = lista_grafo.lista_amigos(args[1])
        elif args[0] == 'listarnivel2':
          result = lista_grafo.lista_nivel2(args[1])
        elif args[0] == 'cadastropessoa':
          result = lista_grafo.adicionar_amigo(args[1],args[2])
        else:
            result = ''
        if result == '':
            response['error'] = 'Opção Inválida'    
        else:
            response['data'] = result
    except Exception as e:
        response['error'] = str(e)

    response = json.dumps(response, ensure_ascii=False).encode('utf8')
    sys.stdout.write(response.decode())
    sys.stdout.flush()
