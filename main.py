import de_bruijn as dbg

filename = 'short.fasta'
reads = dbg.read_reads(filename)

test = ['aabbbba', 'ybb']
g = dbg.deBruijn(test, 2)
dbg.removeTips(g)
dbg.print_graph(g)

#contig = dbg.eulerian_path_search(g)

#print(contig)