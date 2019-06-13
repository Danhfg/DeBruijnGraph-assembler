class DBG:
    def __init__(self):
        KmerMap = {}

    def previous_kmer(kmer_pos, prefix):
        if kmer_pos < len(list(KmerMap.keys())):
            prev_kmer = DNA(list(KmerMap.keys())[kmer_pos:], list(KmerMap.values())[kmer_pos:])
            prev_kmer.insert(prev_kmer.begin(), prefix);
            
            kmer_pos = KmerMap[prev_kmer];
        return kmer_pos
        
    def next_kmer(kmer_pos, suffix):
        if kmer_pos < len(list(KmerMap.keys())):
            next_kmer = DNA(list(KmerMap.keys())[kmer_pos+1:], list(KmerMap.values())[kmer_pos+1:])
            next_kmer.insert(next_kmer.end(), suffix)
            kmer_pos = KmerMap[next_kmer];

        return kmer_pos;

    def previous_kmers(kmer_pos):
        prev = []
        for prev_it in [previous_kmer(kmer_pos, 'A'),previous_kmer(kmer_pos, 'C'),
                    previous_kmer(kmer_pos, 'G'), previous_kmer(kmer_pos, 'T')]:
            if (prev_it in KmerMap.keys()):
                #prev kmer exists, return it
                prev.append(prev_it)
    return prev;

    def next_kmers(kmer_pos):
        next = []
        for next_it in [next_kmer(kmer_pos, 'A'),next_kmer(kmer_pos, 'C'),
                    next_kmer(kmer_pos, 'G'), next_kmer(kmer_pos, 'T')]:
            if next_it in KmerMap.keys():
                next.append(next_it)

        return next;

    def in_degree(kmer_pos):
        return len(previous_kmers(kmer_pos));

    def out_degree(kmer_pos):
        return len(next_kmers(kmer_pos));

    def increment(kmer):
        KmerMap[kmer] += 1

    def increase(kmer, count):
        KmerMap[kmer] += count

    """
    const size_t size() const;

    iterator begin();

    const_iterator begin() const;

    iterator end();

    const_iterator end() const;

    iterator erase(const_iterator pos);

    iterator find(const DNA &dna);

    const_iterator find(const DNA &dna) const;

    bool empty() const;
    """
