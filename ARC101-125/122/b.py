N = int(input())
A = list(map(int, input().split()))
A.append(0)
A.sort()
prices = set(A)
sumA = sum(A)

lostA = [0]*(N+1)
for n in range(N+1):
    if n > 0:
        lostA[n] = lostA[n-1] - (A[n] - A[n-1])*(N+1-n)
    else:
        lostA[0] = sumA

minlost = float("inf")
for n in range(N+1):
    lost = N*A[n]/2 + lostA[n]
    if minlost > lost:
        minlost = lost
        x = A[n]/2


A = A[1:]
ans = x + sumA/N - sum([min(a, 2*x) for a in A])/N
print(ans)