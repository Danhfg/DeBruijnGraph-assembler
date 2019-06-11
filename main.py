import de_bruijn as dbg
import sys

filename = sys.argv[1]#'short.fasta'
reads = dbg.read_reads(filename)

#test = ['aabbbba', 'ybb']
g = dbg.deBruijn(reads, 20)
#dbg.removeTips(g)
#dbg.print_graph(g)

contig = dbg.eulerian_path_search(g)

print(contig)
