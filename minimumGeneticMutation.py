"""Minimum Genetic Mutation II"""

def minMutation(start, end, bank):
    """Minimum Genetic Mutation"""
    if end not in bank:
        return -1
    bank = set(bank)
    queue = [(start, 0)]  # (gene, step)
    while queue:
        gene, step = queue.pop(0) # BFS
        if gene == end:
            return step
        for i in range(len(gene)): # for each gene
            for c in 'ACGT': # for each char
                new_gene = gene[:i] + c + gene[i+1:] # replace char 
                if new_gene in bank: # if new gene in bank
                    bank.remove(new_gene)
                    queue.append((new_gene, step+1)) # add to queue
    return -1 # if not found


print(minMutation("AACCGGTT", "AACCGGTA", ["AACCGGTA"]))
print(minMutation("AACCGGTT", "AAACGGTA", ["AACCGGTA", "AACCGCTA", "AAACGGTA"]))
print(minMutation("AAAAACCC", "AACCCCCC", ["AAAACCCC", "AAACCCCC", "AACCCCCC"]))