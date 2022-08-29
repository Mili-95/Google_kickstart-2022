T = int(input())
for i in range(T):
    N = int(input())
    visit = list(map(int, input().split()))
    max = -1
    record = 0
    for j in range(N):
        first_condition = visit[j] > max
        if j+1 < N:
            second_condition = visit[j] > visit[j+1]
        else:
            second_condition = True
        if first_condition and second_condition:
            record += 1
        if first_condition:
            max = visit[j]
    print("Case #{}: {}" .format(str(i+1), str(record)))               