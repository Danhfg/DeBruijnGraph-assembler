import de_bruijn as dbg

filename = 'short.fasta'
reads = dbg.read_reads(filename)

<<<<<<< HEAD
test = ['aabbbba', 'ybb']
g = dbg.deBruijn(test, 2)
dbg.removeTips(g)
=======
test = ['aaabbbba', 'bbbbaaabb', 'baaabaa']
g = dbg.deBruijn(reads, 60)
>>>>>>> bd3ebc2c391540d6a158470eae590378c8b5af84
dbg.print_graph(g)

#contig = dbg.eulerian_path_search(g)

#print(contig)