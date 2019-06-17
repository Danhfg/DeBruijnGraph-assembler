import sys
from Bio import SeqIO
from Bio import pairwise2
from Bio.Seq import Seq
from Bio.SeqRecord import SeqRecord
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
        self.length = 0
        reads = read_data("short.fasta")
        for read in reads:
            if self.Vertices != {}:
                aux = len(self.Vertices.keys())
                self.Vertices[aux] = (Vertice(read))
                self.length += 1
                i = 0 
                for v in self.Vertices.keys():
                    if (self.Vertices[v].seq != self.Vertices[aux].seq and pairwise2.align.globalxx(self.Vertices[v].seq, read, score_only=True) > len(read)*0.7):
                        self.Arestas.append((i, aux))
                    i+=1
            else:
                self.Vertices[0] = (Vertice(read))
                self.length += 1
        self.Arestas.append((self.length-1, 0))
        self.length += 1

        #find_hamiltonian_path([self.Vertices, self.Arestas])
        self.ham = True
        self.caminho_ham = self.find_hamiltonian_path()

    def find_hamiltonian_path(self):
        # Escolhe um vértice inicial
        path = [0]
        choosed = 0

        while len(path) < self.length:          # termina quando o ciclo for hamiltoniano
            aux = len(path)
            for a in self.Arestas:
                if(a[0] == choosed):            # encontrar vértice mais proximo ao ultimo vertice
                    if a[1] not in path[1:]:    # 
                        choosed = a[1]
                        path.append(a[1])       # inserir o vértice após o último vértice do caminho
                        break
            if (aux == len(path)):              # caso não inseriu nenhum vertice o grafo não é hamiltoniano
                self.ham = False
                break


        return path

    def assembly(self):
        contig = self.Vertices[0].seq   # adiciona a sequencia inicial 
        last = self.Vertices[0].seq     # guarda a ultima sequencia vista
        for i in self.caminho_ham:
            if i != 0:
                similaridade = int(pairwise2.align.globalxx(self.Vertices[i].seq, last, score_only=True))
                contig += self.Vertices[i].seq[similaridade:]
            last = self.Vertices[i].seq
                
        return contig




@profile
def main():
    filename = sys.argv[1]
    olc = OLC(["AGCCTCGGACTATAAACACTCCGGCCGTACGAGAACTACTCTAGATCGCTGAAGCAAATCTTAGTCTCCTTTGAAGCTTC", 
            "GCCTCGGACTATAAACACTCCGGCCGTACGAGAACTACTCTAGATCGCTGAAGCAAATCTTAGTCTCCTTTGAAGCTTCG", 
            "CCTCGGACTATAAACACTCCGGCCGTACGAGAACTACTCTAGATCGCTGAAGCAAATCTTAGTCTCCTTTGAAGCTTCGT", 
            "CTCGGACTATAAACACTCCGGCCGTACGAGAACTACTCTAGATCGCTGAAGCAAATCTTAGTCTCCTTTGAAGCTTCGTA",
            "TCGGACTATAAACACTCCGGCCGTACGAGAACTACTCTAGATCGCTGAAGCAAATCTTAGTCTCCTTTGAAGCTTCGTAG" 
            ])
#    print(olc.caminho_ham)
    contig = olc.assembly()
    SeqIO.write(SeqRecord(Seq(contig), id="UNKNOWN", description='sequence assembled ' ), filename, "fasta")

if __name__ == '__main__':
    if len(sys.argv) > 1:
        main()