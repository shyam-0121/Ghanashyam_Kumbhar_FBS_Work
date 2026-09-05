'''
1 
1 1 
1 2 1 
1 3 3 1 

'''
for i in range(4):
    for j in range(i+1):
        
        fact_i = 1
        for x in range(1, i+1):
            fact_i *= x
        
        fact_j = 1
        for x in range(1, j+1):
            fact_j *= x
        
        fact_ij = 1
        for x in range(1, i-j+1):
            fact_ij *= x
        
        C = fact_i // (fact_j * fact_ij)
        print(C  , end=' ')
    
    print()