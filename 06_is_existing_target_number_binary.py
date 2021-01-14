# Q. 1에서 16까지 오름차순으로 정렬되어 있는 배열이 있다.
# 이 배열 내에 14가 존재한다면 True, 존재하지 않는다면 False 를 반환하시오.
# 이진탐색 방법

finding_target = 14
finding_numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16]


def is_existing_target_number_binary(target, array):
    find_count = 0
    current_min = 0           # 현재 최소 값
    current_max = len(array) - 1       # 현재 최대 값 : len 통한 배열의 길이(17이므로) - 1
    current_guess = (current_min + current_max) // 2 #추측값 : (최소 + 최대) / 2 후 나머지 소수부분 버림

    while current_min <= current_max:  #최소에서 시작해 최대 까지 반복
        find_count += 1
        if array[current_guess] == target: # 배열 추측 값이 타겟과 동일할경우
            print(find_count)
            return True #true 출력
        elif array[current_guess] < target: #배열 추측값이 타겟보다 작을경우
            current_min = current_guess + 1 #최소값에 시돗값 +1로 업데이트 해줘라
        else: #그게아니면 클경우기 떄문에
            current_max = current_guess - 1 # 최댓값에 시돗값 -1로 업데이트해줘라
        current_guess = (current_min + current_max) // 2 # 다시한번 추측값을 업데이트해준다.

    return False #돌경우 아무것도 없을 경우 false 출력


result = is_existing_target_number_binary(finding_target, finding_numbers)
print(result)


#시간 복잡도 분석 : 3번안에 찾음 (처음 절반 쪼개고  = > 9 ~16중 12쪼개고 그후 찾음)

