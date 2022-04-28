# you can write to stdout for debugging purposes, e.g.
# print("this is a debug message")
# solution to problem related to having same pattern for all part of string
def solution(S):
    # write your code in Python 3.6
    final = ""
    counts = {}
    max = 0
    for i in range(0, len(S)-1):
        counts[S[i]] = S.count(S[i])
        if i > 0 and S.count(S[i]) > S.count(S[i-1]):
            max = S.count(S[i])
    for key, value in counts.items():
        final += key*(value + (max-value))
    return final
    # for letter in S:
    #     a = S.count(letter)
    #     print(a)


print(solution("aabbkkccdddzz"))
