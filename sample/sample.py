T = int(input())
 
for x in range(1, T + 1):
    N, M = tuple(map(int, input().split())) 
    C = list(map(int, input().split()))
    sum = 0
    for ci in C:
        sum += ci
    modulo = sum % M
    print("Case #%s: %s " %(x , modulo))  