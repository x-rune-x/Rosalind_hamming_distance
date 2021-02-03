def hamming_distance(s, t):
    ham_dist = 0
    for index in range(len(s)):
        if s[index] != t[index]:
            ham_dist += 1

    return ham_dist


file = open("rosalind_hamm.txt", "r")
dna_s = file.readline().rstrip()
dna_t = file.readline().rstrip()

h_dist = hamming_distance(dna_s, dna_t)
print(h_dist)
print(dna_s)
print(dna_t)
