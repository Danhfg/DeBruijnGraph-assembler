import de_bruijn as dbg
import time

start_time = time.time()

filename = 'short.fasta'
reads = dbg.read_reads(filename)

#test = ['abcefg', 'bwqf']
g = dbg.deBruijn(reads, 2)
dbg.removeTips(g)
dbg.print_graph(g)

contig = dbg.eulerian_path_search(g)

print(contig)

print('--- %s seconds ---' % (time.time() - start_time))