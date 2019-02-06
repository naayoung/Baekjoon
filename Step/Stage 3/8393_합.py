# 문제
# n이 주어졌을 때, 1부터 n까지 합을 구하는 프로그램을 작성하시오.

# 입력
# 첫째 줄에 n (1 ≤ n ≤ 10,000)이 주어진다.

# 출력
# 1부터 n까지 합을 출력한다.

n = int(input(''))
sub = 0
if 1 <= n <= 10000:
    for i in range(n+1):
        sub = sub + i
    print(sub)
else:
    print('1이상 10000이하로 입력해주세요')

# print(n*(n+1)//2)
