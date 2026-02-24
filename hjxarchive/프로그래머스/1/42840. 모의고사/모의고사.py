def solution(answers):
    answer = []
    
    ans1 = [1,2,3,4,5]
    ans2 = [2,1,2,3,2,4,2,5]
    ans3 = [3,3,1,1,2,2,4,4,5,5]
    
    cnt1 = 0
    cnt2 = 0
    cnt3 = 0
    
    n = len(answers)
    
    for cnt in range(n):
        a1 = ans1[cnt%5]
        a2 = ans2[cnt%8]
        a3 = ans3[cnt%10]
        
        cnt1 += (answers[cnt]==a1)
        cnt2 += (answers[cnt]==a2)
        cnt3 += (answers[cnt]==a3)
        
    max_cnt = max(cnt1,cnt2,cnt3)
    if cnt1 == max_cnt: answer.append(1)
    if cnt2 == max_cnt: answer.append(2)
    if cnt3 == max_cnt: answer.append(3)
    
    return answer