# DeBruijnGraph-assembler
Genome assembler based on De Bruijn Graph
# Antes de executar o programa, certifique-se que os seguintes pacotes estão instalaldos
    sudo apt-get -y install python3-pip
    pip3 install biopython --user
    pip3 install memory_profiler --user
# Para executar o programa utilize o comando abaixo:
    python3 -m memory_profiler main.py data/short.fasta assembled.fa