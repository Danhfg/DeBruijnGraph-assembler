from Bio import pairwise2
# Realiza a leitura das reads a partir de um arquivo com o formato FASTA. 
def read_data(filename):
    f = open(filename, 'r')
    linhas = f.readlines()
    f.close()
    reads = []

    for linha in linhas:
        if linha[0] != '>':
            reads = reads + [linha.rstrip()]

    return reads



class Vertice:
    def __init__(self, seq):
        self.seq = seq

class Aresta:
    def __init__(self, v1, v2):
        self.v1 = v1
        self.v2 = v2

class OLC:
    def __init__(self,reads):
        self.Vertices = {}
        self.Arestas = []
        reads = read_data("short.fasta")
        for read in reads:
            if self.Vertices != {}:
                aux = len(self.Vertices.keys())
                self.Vertices[aux] = (Vertice(read))
                i = 0 
                for v in self.Vertices.keys():
                    if (self.Vertices[v].seq != self.Vertices[aux].seq and pairwise2.align.globalxx(self.Vertices[v].seq, read, score_only=True) > len(read)*0.7):
                        self.Arestas.append((i, aux))
                    i+=1
            else:
                self.Vertices[0] = (Vertice(read))

@profile
def main():
    olc = OLC(["AGCCTCGGACTATAAACACTCCGGCCGTACGAGAACTACTCTAGATCGCTGAAGCAAATCTTAGTCTCCTTTGAAGCTTC", 
            "GCCTCGGACTATAAACACTCCGGCCGTACGAGAACTACTCTAGATCGCTGAAGCAAATCTTAGTCTCCTTTGAAGCTTCG", 
            "CCTCGGACTATAAACACTCCGGCCGTACGAGAACTACTCTAGATCGCTGAAGCAAATCTTAGTCTCCTTTGAAGCTTCGT"])
    #print(olc.Vertices[0].seq)
    #for colnum, edge in enumerate(edges):
    #    print()
    #print(olc.Arestas)

if __name__ == '__main__':
    main()