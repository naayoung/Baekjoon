# 문제
# 세 정수 A, B, C가 주어진다. 이때, 두 번째로 큰 정수를 출력하는 프로그램을 작성하시오.

# 입력
# 첫째 줄에 세 정수 A, B, C가 공백으로 구분되어 주어진다. (1 ≤ A, B, C ≤ 100)

# 출력
# 두 번째로 큰 정수를 출력한다.

a, b, c = map(int, input('').split())
if 1 <= a and b and c <= 100:
    if a < b:
        if b < c:
            print(b)
        else:
            if c < a:
                print(a)
            else:
                print(c)
    else:
        if a < c:
            print(a)
        else:
            if b < c:
                print(c)
            else:
                print(b)
else:
    print('수를 1이상 100이하로 입력하세요')
