import read_data as read_data
import collections

class Vertice:
    def __init__(no, nome_):
        no.nome = nome_
        no.entrada = 0
        no.saida = 0

class Aresta:
    def __init__(no, nome_):
        no.nome = nome_

# Realiza a construção do de Bruijn Graph conforme apresentado, realizando leitura de k-mers.
def deBruijn(leituras, kmers):
    arestas = collections.OrderedDict()
    vertices = collections.OrderedDict()

    for leitura in leituras:
        i = 0
        while i+kmers < len(leitura):
            v1 = leitura[i:i+kmers]
            v2 = leitura[i+1:i+kmers+1]
            if v1 in arestas.keys():
                vertices[v1].saida += 1
                arestas[v1] += [Aresta(v2)]
            else:
                vertices[v1] = Vertice(v1)
                vertices[v1].saida += 1
                arestas[v1] = [Aresta(v2)]

            if v2 in arestas.keys():
                vertices[v2].entrada += 1
            else:
                vertices[v2] = Vertice(v2)
                vertices[v2].entrada += 1
                arestas[v2] = []
            
            i += 1

    return (vertices, arestas)

#Realiza a busca do caminho euleriano no grafo
def eulerian_path_search(graph):
    
    Vert = graph[0]
    Ares = graph[1]

    start = list(Vert.keys())[0]
    # Realiza a busca pelo nó que possui o menor grau de entrada
    for k in list(Vert.keys()):
        if Vert[k].entrada < Vert[start].entrada:
            start = k

    tour = start
    atual = start

    #Visita os nós de forma a ir gerando o grau de entrada
    while len(Ares[atual]) > 0:
        next = Ares[atual][0]           # obtem o próximo nó
        del Ares[atual][0]              # remove ele do dicionário, marcar que foi visitado
        tour += next.nome[-1]           # adiciona o nó ao caminho
        atual = next.nome               # atualiza o nó atual

    return tour


# Realiza a leitura das reads a partir de um arquivo com o formato FASTA. 
def read_reads(filename):
    f = open(filename, 'r')
    linhas = f.readlines()
    f.close()
    reads = []

    for linha in linhas:
        if linha[0] != '>':
            reads = reads + [linha.rstrip()]

    return reads


#Imprimir o grafo
def print_graph(graph):
    Vert = graph[0]
    Arest = graph[1]


    for k in list(Vert.keys()):
        print("nome: ", Vert[k].nome, ". entrada: ", Vert[k].entrada, ". saida: ", Vert[k].saida)
        print("Arestas para: ")
        #for e in Arest[k]:
            #print(e.nome)

# Realiza a remoção das tips.
# Observar se possui algum vértice ( diferente do inicio ) que não possui conexão de entrada
# com nenhum outro vertice. De forma que ele seja uma nova fonte, dai remove ele.
# Como a remoção é do suposto segundo fonte, então não há problemas.

def removeTips(graph):
    Vert = graph[0]     # obtemos os vertices
    Arest = graph[1]    # obtemos as arestas do grafo#
    lista = list(Vert.keys())

    rem_vert = []
    rem_ares = []
    
    
    for index, k in enumerate(list(Vert.keys())):             # percorre cada vertice
        if k != lista[0] and Vert[k].entrada == 0:  # verifica se não é o fonte e se possui grau de entrada 0
            #Verificar os vértices que possuem alguma conexão para dar baixa
            
            #adiciona os vértices a ser removidos
            rem_ares.append(k)
            rem_vert.append(k)

    qnt_ares = 0
    
    for i in rem_ares:
        for e in Arest[i]:
            #print(e.nome)
            for k in list(Vert.keys()):     # percorre cada vertice
                if e.nome == k :            # verfica se o vetor atual vai para o vertice que se deseja excluir
                    Vert[k].entrada -= 1          # diminui o grau de entrada do vertice atual (considerar exclusão).
        del Vert[i]

    for i in rem_ares:
        del Arest[i]
    