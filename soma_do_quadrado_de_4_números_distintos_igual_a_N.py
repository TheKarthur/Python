import sys
import math

n = int(input())

# para otimizar os loops, devemos entender que todos os números
# são menores que a raiz quadrada de N
# logo se N=36,   0<i<j<k<l<sqrt(N)

for i in range(1, int(math.sqrt(n))): 
    for j in range(i+1, int(math.sqrt(n))):
        for k in range(j+1, int(math.sqrt(n))):
            for l in range(k+1, int(math.sqrt(n))):
                if i*i + j*j + k*k + l*l == n:
                    print(i, j, k, l)
                    exit()
