# 팩토리얼 부분 설명 예제

def factorial(n): # 5
    if n == 1:  # 5 == 1 x
        return 1
    return n * factorial(n-1) #5 * factorial(4)


print(factorial(5))