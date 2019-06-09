import de_bruijn as dbg

#fname = 'g200reads.fa'
#reads = db.read_reads(fname)

test = ['aabbbba', 'ybb']
g = dbg.deBruijn(test, 2)
dbg.removeTips(g)
dbg.print_graph(g)

#contig = dbg.eulerian_path_search(g)

#print(contig)