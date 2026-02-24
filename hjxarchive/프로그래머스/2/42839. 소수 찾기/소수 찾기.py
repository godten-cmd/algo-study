import itertools
import math

def is_prime(n):
    if n < 2:
        return 0
    for cnt in range(2, int(math.sqrt(n)) + 1):
        if n % cnt == 0:
            return 0
    return 1

def solution(numbers):
    # 기존에는 소수(~10^7)를 먼저 계산하고 그 뒤 가능한 모든 Permutation에 대해 검증 진행...
    # 시간복잡도 이슈가 있음. 
    # 먼저 가능한 조합을 구하고(Set를 사용해 중복 문제 해결, 011, 11 같은)
    # 이를 소수로 판별(아리스토테네스의 체) 
    # 소수 판별함수에서 DP 쓰면 추가적인 성능 향상이 가능할 것 같음. 
    answer = 0
    
    candidates = set()
    
    for cnt in range(1, len(numbers) + 1):
        for p in itertools.permutations(list(numbers), cnt):
            num = int("".join(p))
            candidates.add(num)
            
    for num in candidates:
        answer += is_prime(num)
    
    return answer