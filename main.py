import de_bruijn as dbg
import sys
from Bio import SeqIO
from Bio.Seq import Seq
from Bio.SeqRecord import SeqRecord
from memory_profiler import LogFile

@profile()
def main():
    filename = sys.argv[1]#'short.fasta'
    reads = dbg.read_reads(filename)

    #test = ['aabbbba', 'ybb']
    g = dbg.deBruijn(reads, 20)
    dbg.removeTips(g)
    #dbg.print_graph(g)

    contig = dbg.eulerian_path_search(g)

    SeqIO.write(SeqRecord(Seq(contig), id="UNKNOWN", description='sequence assembled from ' +sys.argv[1] ), sys.argv[2], "fasta")

if __name__ == '__main__':
    if len(sys.argv) > 2:
        main()
        #sys.stdout = LogFile('memory_profile_log')
