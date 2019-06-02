import de_bruijn as dbg

#fname = 'g200reads.fa'
#reads = db.read_reads(fname)

test = ['aaabbbba']
g = dbg.deBruijn(test, 2)
dbg.print_graph(g)

contig = dbg.eulerian_path_search(g)

print(contig)