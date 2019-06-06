import de_bruijn as dbg

filename = 'short.fasta'
reads = dbg.read_reads(filename)

test = ['aaabbbba', 'bbbbaaabb', 'baaabaa']
g = dbg.deBruijn(reads, 60)
dbg.print_graph(g)

contig = dbg.eulerian_path_search(g)

print(contig)