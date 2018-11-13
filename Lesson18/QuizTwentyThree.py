# Creating an Empty Hash Table
# Define a procedure, make_hashtable,
# that takes as input a number, nbuckets,
# and returns an empty hash table with
# nbuckets empty buckets.

def make_hashtable(nbuckets):
    i = 0
    hashTable = []
    while i < nbuckets:
        hashTable.insert(i,[])
        i += 1
    return hashTable

# test
print make_hashtable(2)
