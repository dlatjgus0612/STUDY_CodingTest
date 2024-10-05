""" 
4-1 상하좌우 
N x N 정사각형 공간. 가장 왼쪽 위 (1, 1)
계획서에는 하나의 줄에 띄어쓰기로 구분. L왼R오U위D아래 
공간 밖은 무시.

- input 첫째 줄 공간의 크기 1 <= N <= 100 , 둘째 줄 계획서 내용 (1 <= 이동 횟수 <= 100)
- output 최종적으로 도착할 지점의 좌표 (X, Y)를 공백으로 구분하여 출력 
"""

# 입력 받기 N, 계획서 
n = int(input())
plans = input().split()
x, y = 1, 1 # 시작점 정의 필요

""" 
L R U D 방향과 이름 정의 ***
(1,1) (1,2)
(2,1) (2,2)
라서 왼이면 dy 에서 -1 
"""

dx = [0, 0, -1, 1]
dy = [-1, 1, 0, 0]
move_types = ['L', 'R', 'U', 'D']

# 계획서 길이만큼 돌며 일치하는 대로 위치 변환 
for plan in plans:
    # 이동 후 좌표 
    for i in range(len(move_types)):
        if plan == move_types[i]:
            nx = x + dx[i]
            ny = y + dy[i]
    # 공간 벗어나면 무시 ***
    if nx < 1 or ny < 1 or nx > n or ny > n:
        continue
    # 이동 수행 ***
    x, y = nx, ny

print (x, y)

"""
예제 4-2 시각
제한 : 2초, 128mb 
N이 입력되면 00시 00분 00초 ~ N시 59분 59초 모든 시각 중 3이 하나라도 포함되는 경우의 수를 구하는 프로그램
input N
output 3이 하나라도 포함되는 모든 경우의 수
"""

# input & output
h = int(input())
count = 0 
# 3중 반복 24x60x60
for i in range(h + 1):
    for j in range(60):
        for k in range(60):
            # '3'포함 그거
            if '3' in str(i) + str(j) + str(k): # str변환하고 확인
                count += 1
print(count)

"""
실전 2 (시뮬레이션) 왕실의 나이트
제한 : 1초, 128mb 
8x8 좌표 평면 L자 형태로만 이동. 정원 밖으론 나갈 수 없음. 특정 2가지 경우로 이동
1. 수평 두 칸, 수직 한 칸
2. 수직 두 칸, 수평 한 칸
시작점이 (1,a) 열 a,b~g,h / 행 1,2~7,8
input 현재 나이트가 위치한 곳의 좌표를 입력 'a1'
output 이동할 수 있는 경우의 수 출력 '2'
"""

# input str+int
input_data = input()
row = int(input_data[1])
column = int(ord(input_data[0])) - int(ord('a')) + 1 # 문자 아스키 - a 아스키 + 1
# 두 가지 이동방법에 있는 모든 경우의 수 ***
# 수평 2 수직 1, 수직 2 수평 1 
steps = [(-2,-1),(-2, 1),(2,-1),(2,1),(1,2),(1,-2),(-1,2),(-1,-2)]

result = 0 # 가짓수 담을 공간 
for step in steps:
    # 이동하고자 하는 위치 확인 ***
    nx_row = row + step[0]
    nx_column = column + step[1]
    # 이동 가능한지 확인 ***
    if nx_row >= 1 and nx_row <= 8 and nx_column >= 1 and nx_column <= 8 :
        result += 1

print(result)

"""
실전 3 (시뮬레이션) 게임 개발
제한 : 1초, 128mb 
N x M 의 직사각형, 육지 or 바다, 캐릭터는 동서남북 중 한 곳을 바라본다. 
맵의 각 칸은 (A, B)로 나타냄. 
1. 현재 위치, 현재 방향을 기준으로 반시계 부터 갈 곳을 정한다. 
2. 가보지 않은 칸이 있으면 전진, 없으면 마저 돌리고 1단계
3. 이미 다 가봤거나 바다면 방향유지, 한 칸 뒤로 가고 다시 searching, 뒤가 바다면 stop
input
첫째줄 세로 N>=3, 가로 M<=50
둘째줄 (A, B) 있는 칸 좌표, 바라보는 방향 d 공백으로 구분하여.
d : 0 북 1 동 2 남 3 서
셋째줄 0 육지 1 바다 로 맵이 주어짐. 처음 캐릭터 위치는 무조건 육지
output 
이동을 마친 후 캐릭터가 방문한 칸의 수
"""

# input N M / A B d 
n, m = map(int, input().split())

# 저장하기 위한 공간 initialize 필수 *** 공간과 받아야하는 맵은 다르다 
d = [[0] * m for _ in range(n)]

x, y, direction = map(int, input().split())
d[x][y] = 1  # 현재좌표 방문처리 *** 까먹음_문제를 잘 읽자

# input NxM info ***
array = []
for i in range(n):
    array.append(list(map(int, input().split())))

# define 북 동 남 서 
dx = [-1, 0, 1, 0]
dy = [0, 1, 0, -1]

# 회전함수 따로 정의 ***
def turn_left():
    global direction  # 전역으로 끌어온다 ***
    direction -= 1
    if direction == -1:  # 북 -> 서
        direction = 3

# 추가 변수 정의 *** 우선 서있는 자리가 1 !
count = 1
turn_time = 0

# 현재의 위치가 육지이면 
while True:
    turn_left()
    nx = x + dx[direction]
    ny = y + dy[direction]

    # 맵 범위 안에서만 동작하도록 조건 추가 ***
    if (0 <= nx < n) and (0 <= ny < m):
        # 보는 방향으로 이동했을 때 육지, 이동
        if d[nx][ny] == 0 and array[nx][ny] == 0:
            x = nx
            y = ny
            d[x][y] = 1  # 방문 처리
            count += 1
            turn_time = 0  # 돌린거 초기화
            continue
        # 보는 방향으로 이동했을 때 바다, 돌려
    turn_time += 1 
    # 왜 else를 빼야 코드가 돌아가는 거지? 무슨 예외가 있지.. 아니 뭐 없어도 되긴하는데... 

    # 4번 돌고 뒤가 육지면 뒤로 가기
    if turn_time == 4:
        nx = x - dx[direction]
        ny = y - dy[direction]

        # 맵 범위 안에서만 동작하도록 조건 추가 + back했는데 육지 
        if (0 <= nx < n) and (0 <= ny < m) and (array[nx][ny] == 0):
            x = nx
            y = ny
        # 4번 돌고 뒤 바다면 종료
        else:
            break
        turn_time = 0

print(count)
