P = {2, 4, 6, 8, 10, 12, 14, 16, 18, 20}
Q = {5, 10, 15, 20, 25, 30, 35, 40, 45, 50}


A = set(range(1, 1000)) # 0 не берем! 

for x in range(1, 10000):
    if not (((x in A) <= (x in P)) or (not(x in Q) <= (not(x in A)))):
        A.remove(x)  

print(len(A))
