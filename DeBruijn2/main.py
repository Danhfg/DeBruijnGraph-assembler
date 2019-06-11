import sys

spectral_alignment_cutoff = 5;
spectral_alignment_iterations = 3;
contig_coverage_cutoff = 5; //10 works too but this is safer

def read_data(nome_arquivo):
    f = open(nome_arquivo, 'r')                          #Abre o arquivo
    linhas = f.readlines()                              #Cria um array onde cada linha do arquivo é o conteúdo
    f.close()                                           #Fecha o arquivo
    leituras = []

    for linha in linhas:                                #Percorre cada linha
        if line[0] != '>':                              #Remove a identificação de cada fragmento do genoma
            leituras = leituras + [linha.rstrip()]      #Remove qualquer espaço após os dados na linhas

    return leituras;                                    #Retorna a leitura

def main():
    if (sys.argc != 5):
        print ("wrong number of arguments (5 required)")
        return 0

    sys.argv[1]
    inFileName = sys.argv[1]
    outFileName = sys.argv[2]
    kmer_size = sys.argv[3]
    try:
        reads = readFile(inFileName)

        #add all kmers from file into de Bruijn Graph
        factory = DBGFactory();
        dbg = DBG();
        factory.add_read_kmers(dbg, reads, kmer_size);
        reads.clear();
        errorCorrector = ErrorCorrector()
        for i in range(spectral_alignment_iterations):
            if(not errorCorrector.spectral_alignment(dbg, spectral_alignment_cutoff)):
                break
        assembler = Assembler()
        sequences = []
        assembler.assemble(dbg, contig_coverage_cutoff, sequences);

        #find all linear stretches in DBG, remove those with an average coverage lower than a cutoff
        Assembler assembler;
        vector<string> sequences;
        assembler.assemble(dbg, contig_coverage_cutoff, sequences);
        print(sequences)


    except Exception as e:
        pass
    return 0

if __name__ == '__main__':
    main()