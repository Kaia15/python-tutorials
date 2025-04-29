h = {0: 1, 1: 1}
def catalan(n):
    if n == 0 or n == 1: return h[n]
    res = 0
    for i in range (1,n + 1):
        l,r = i - 1, n - i
        if l not in h:
            h[l] = catalan(l)
        if r not in h: 
            h[r] = catalan(r)
        res += h[l]*h[r]
    if n not in h: h[n] = res
    return res
        
def main():
    n = int(input())
    print (catalan(n))

main()
print (h)