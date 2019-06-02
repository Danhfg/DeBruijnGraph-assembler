def read_data(nome_arquivo):
    f = open(nome_arquivo, 'r')                          #Abre o arquivo
    linhas = f.readlines()                              #Cria um array onde cada linha do arquivo é o conteúdo
    f.close()                                           #Fecha o arquivo
    leituras = []

    for linha in linhas:                                #Percorre cada linha
        if line[0] != '>':                              #Remove a identificação de cada fragmento do genoma
            leituras = leituras + [linha.rstrip()]      #Remove qualquer espaço após os dados na linhas

    return leituras;                                    #Retorna a leitura