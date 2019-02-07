# 문제
# N개의 숫자가 공백 없이 쓰여있다. 이 숫자를 모두 합해서 출력하는 프로그램을 작성하시오.

# 입력
# 첫째 줄에 숫자의 개수 N (1 ≤ N ≤ 100)이 주어진다. 둘째 줄에 숫자 N개가 공백없이 주어진다.

# 출력
# 입력으로 주어진 숫자 N개의 합을 출력한다.

n = int(input(''))
number = list(map(int, input('')))
sub = 0
if 1 <= n <= 100:
    if len(number) == n:
        for i in range(0, n):
            sub = sub + number[i]
        print(sub)
    else:
        print('입력한 숫자만큼 수를 넣으세요')
else:
    print('1이상 100이하로 입력해주세요')
