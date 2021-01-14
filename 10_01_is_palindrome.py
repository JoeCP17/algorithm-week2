#Q. 다음과 같이 문자열이 입력되었을 때, 회문이라면 True 아니라면 False 를 반환하시오.
# 반복문 사용하면 엄청 쉬움

input = "abcba"


def is_palindrome(string):
    chr = len(string)
    for i in range(chr):
        if string[i] != string[chr-1-i]: # 맨뒤가 chr-1 이고 i가 0부터 시작하기때문에 비교가 가능하다.
            return False

    return True


print(is_palindrome(input))

# "가나다라마바사" [(처음인덱스) : (끝 인덱스)]적으면 잘라서 사용가능
#   "가나다라마바사" [(처음인덱스) : -에서(끝 인덱스)]