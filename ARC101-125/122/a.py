N = int(input())
A = list(map(int, input().split()))
mod = 10**9+7

mcnt = [0]*(N)
pdp = [0]*N
mdp = [0]*N

if N == 1:
    print(A[0])
else:
    pdp[1] = mdp[1] = 1
    for n in range(2, N):
        pdp[n] = (pdp[n-1] + mdp[n-1])%mod
        mdp[n] = pdp[n-1]

    ans = 0
    h = pdp[N-1] + mdp[N-1]
    h %= mod
    for n in range(N):
        if n == 0:
            ans += A[n]*h
        else:
            mcnt[n] = mdp[n]*mdp[N-n]%mod
            ans += A[n]*(h-mcnt[n]*2)%mod
    print(ans%mod)