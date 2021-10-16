n = int(input())
scores = list(map(int, input().split()))
scores.sort()
maxi = max(scores)

for i in range(n):
    for j in range(n):
        if scores[i] > scores[j] and scores[i] < maxi:
            runner_up = scores[i]
        elif scores[i] == scores[j] and scores[i] < maxi:
            runner_up = scores[j]

print(runner_up)