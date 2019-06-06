import read_data as read_data

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
    arestas = dict()
    vertices = dict()

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
    for k in list(Vert.keys()):
        if Vert[k].entrada < Vert[start].entrada:
            start = k

    contig = start
    atual = start

    #Retornar o próximo vertice
    while len(Ares[atual]) > 0:
        next = Ares[atual][0]
        del Ares[atual][0]
        contig += next.nome[-1]
        atual = next.nome

    return contig

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
        print("Arestas: ")
        for e in Arest[k]:
            print(e.nome)
        print()