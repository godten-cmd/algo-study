def solution(sizes):
    n = len(sizes)
    size_b = [0 for _ in range(n)]
    size_s = [0 for _ in range(n)]
    for cnt in range(n):
        b,s = sizes[cnt][0], sizes[cnt][1]
        if b<s: b,s = s,b
        size_b[cnt] = b
        size_s[cnt] = s
    answer = max(size_b)*max(size_s)
    return answer