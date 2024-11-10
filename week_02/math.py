A={9, 12, 15, 21, 24, 27, 30, 33, 36, 42, 48, 51, 54, 57, 60, 63, 66, 69, 72, 78, 81, 84, 87, 90, 93, 96}

B={12, 16, 24, 28, 32, 36, 48, 52, 56, 60, 64, 68, 72, 80, 84, 88, 92, 96}

C={6, 12, 18, 24, 30, 36, 42, 48, 54, 60, 66, 72, 78, 84, 90, 96}



#len(A)

#len(B)

#print( len(A) , len(B) )


#print(A.union(B), A.intersection(B))

#print( A.union(B))

#print( len (A) + len(B) - len (A.intersection(B)))


print(A.union(B).union(C))

print(len(A) + len(B) + len(c) - (len (A.intersection(B) + len (B.intersection(C) + len (A.intersection(C))
