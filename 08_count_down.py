# Q. 60에서 0까지 숫자를 출력하시오.

def count_down(number):
    if number < 0: #만약 number 가 0보다 작다면
        return        # 함수 처음부분으로 다시 리턴해라

    print(number)          # number를 출력하고


    count_down(number - 1) # count_down 함수를 number - 1 인자를 주고 다시 호출한다!



count_down(60)