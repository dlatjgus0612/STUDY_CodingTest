# 직각 삼각형 그리기
def solution1():
    return print('\n'.join('*'*(i+1) for i in range (int(input()))))

# 짝수 홀수 개수 출력 
def solution2(num_list):
    answer = [0, 0]
    for n in num_list:
        answer[n%2] += 1  # 짝수면 answer[0]에 추가, 홀수면 answer[1]에 추가
    return answer  # 루프가 끝난 후에 결과 반환

# 진료순서 정하기
def solution3(emergency):
    tmp = sorted(emergency, reverse = True) #내림차순
    ans = []
    for i in emergency:
        ans.append(tmp.index(i)+1) #순서 1 부터 나오도록 
    return ans

#-----------------------------------
solution1() # 직각 삼각형 그리기

num_list = [1, 2, 3, 4, 6]
print("solution2 : " + str(solution2(num_list)))  # 짝수 홀수 개수 출력

emergency = [30, 10, 23, 6, 100] #[2,4,3,5,1]순위 
print(solution3(emergency))