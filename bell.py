binom = {(0,0): 1, (1,0): 1, (1,1): 1}

def binomial(n, k):
    if n < k:
        return 0
    if k == 0:
        binom[(n,0)] = 1
        return 1
    if (n, k) in binom:
        return binom[(n, k)]
    
    if (n - 1, k - 1) not in binom:
        binom[(n - 1, k - 1)] = binomial(n - 1, k - 1)
    if (n - 1, k) not in binom:
        binom[(n - 1, k)] = binomial(n - 1, k)
    
    binom[(n, k)] = binom[(n - 1, k - 1)] + binom[(n - 1, k)]
    return binom[(n, k)]

bell = {0: 1}
def bell(n):
    if n in bell: return bell[n]
    res = 0
    for i in range (1,n + 1):
        res += bell(i - 1) * binomial(n - 1, i - 1)
    bell[n] = res 
    return res


def main():
    n= int(input())
    k = int(input())
    print (binomial(n, k))

main()

def binomialNaive(n,k):
    if n < k: return 0 
    if k == 0: return 1
    return binomialNaive(n - 1, k - 1) + binomialNaive(n - 1,k)