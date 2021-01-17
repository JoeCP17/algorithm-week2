# Q. 음이 아닌 정수들로 이루어진 배열이 있다.
# # 이 수를 적절히 더하거나 빼서 특정한 숫자를 만들려고 한다.
# 예를 들어 [1, 1, 1, 1, 1]로 숫자 3을 만들기 위해서는 다음 다섯 방법을 쓸 수 있다.

# -1+1+1+1+1 = 3
# +1-1+1+1+1 = 3
# +1+1-1+1+1 = 3
# +1+1+1-1+1 = 3
# +1+1+1+1-1 = 3

# 사용할 수 있는 숫자가 담긴 배열 numbers,
# 타겟 넘버 target_number이 매개변수로 주어질 때
# # 숫자를 적절히 더하고 빼서 타겟 넘버를 만드는 방법의 수를 반환하시오.

# 2,3,1로 변경하여 문제 풀기 
numbers = [2, 3, 1]
target_number = 0
result_count = 0  # target 을 달성할 수 있는 모든 방법의 수를 담기 위한 변수


def get_count_of_ways_to_target_by_doing_plus_or_minus(array, target, current_index, current_sum):
    if current_index == len(numbers):  # 탈출조건!
        if current_sum == target:
            global result_count
            result_count += 1  # 마지막 다다랐을 때 합계를 추가해주면 됩니다.
        return
    get_count_of_ways_to_target_by_doing_plus_or_minus(array, target, current_index + 1,
                                                       current_sum + numbers[current_index])
    get_count_of_ways_to_target_by_doing_plus_or_minus(array, target, current_index + 1,
                                                       current_sum - numbers[current_index])


get_count_of_ways_to_target_by_doing_plus_or_minus(numbers, target_number, 0, 0)
# current_index 와 current_sum 에 0, 0을 넣은 이유는 시작하는 총액이 0, 시작 인덱스도 0이니까 그렇습니다!
print(result_count)  # 2가 반환됩니다!