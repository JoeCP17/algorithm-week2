# Q. 다음과 같이 문자열이 입력되었을 때,
# 회문이라면 True 아니라면 False 를 반환하시오.
# 재귀함수 사용
input = "abcba"


def is_palindrome(string):
    if string[0] != string[-1]:  # 첫글자와 마지막글자가 맞지 않을경우
        return False  # 거짓으로 호출
    if len(string) <= 1:  # 가운데 남는수를 위한 탈출조건 1개가남았다면 다 맞는것일것이므로
        return True  # 참으로 탈출
    return is_palindrome(string[1:-1])


print(is_palindrome(input))
# "가나다라마바사" [(처음인덱스) : (끝 인덱스)]적으면 잘라서 사용가능
#   "가나다라마바사" [(처음인덱스) : -에서(끝 인덱스)]


# 탈출조건 있을것
