# Q. 다음과 같이 숫자로 이루어진 배열이 있을 때,
# 2이 존재한다면 True 존재하지 않는다면 False 를 반환하시오.
# 순차배열로 풀었을때
finding_target = 2
finding_numbers = [0, 3, 5, 6, 1, 2, 4]


def is_exist_target_number_binary(target, numbers):
    count_number = 0
    for number in numbers:
        count_number += 1
        if number == target:
            print(count_number)
            return True

    return False


result = is_exist_target_number_binary(finding_target, finding_numbers)
print(result)


#이진탐색을 못사용하는 이유는 정렬이 되어있지않음

# 이진탐색은 정렬이 확실히되어있을때만 사용이 가능하다.

# 이문제의경우 중간 값 6을기준으로 0 , 3 , 5 부분을 바라봐야맞겠지만 그부분엔 2가없다

# 찾을수 없기때문에 해당 부분은 잘못된 문제