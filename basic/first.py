# 이거슨 3의배수랑 5의배수 빼고 출력
#i = 1
# while i < 50:
#     if (i % 3 == 0) or (i % 5 == 0):
#         i += 1
#     else:
#         print(i)
#         i += 1

#  1~ 50까지 출력
# for i in range(1,50):
#     print(i)

# 3번째인자 찾기 ( while 문이랑 for 문으로 )
# testList = ['number','double','integer','float']
#
# check = 0
# while check < len(testList):
#     if testList[check] == 'integer':
#         print('찾았다', testList[check])
#     else:
#         print('못찾았다')
#     check += 1
#
# check = 0
# for check in testList:
#     if check == 'integer':
#         print('찾았다')
#     else:
#         print('못찾았다')

# 1 부터 30 까지 다 더하기!
# i = 1
# count = 0
# for i in range(1,31):
#     count += i
#     i += 1
# print(count)

# 11 부터 21 까지 소수 출력
# for i in range(11,100):
#     if (i % 2 == 0) or (i % 3 == 0) or (i % 5 == 0) or (i % 7 == 0):
#         pass
#     else:
#         print(i)


# 요기서부터 함수~
# def add_many(*hi):
#     result = 0
#     for i in hi:
#         result = result + i
#     return result
# print(add_many(1+2+3+4))


# 사칙연산 함수짜기
# print('a 를 입력하세요')
# a = input()
# print('b 를 입력하세요')
# b = input()
# print('c 를 입력하세요')
# c = input()
# print(a,b,c)
#
# def Arithmetic(a,b,c):
#     print("더하기는 ",int(a)+int(b)+int(c))
#     print("빼기는",int(a)-int(b)-int(c))
#     print("곱하기는",int(a)*int(b)*int(c))
#     print("나누기는",int(a)/int(b)/int(c))
#
# Arithmetic(a,b,c)

# 재귀함수 - 팩토리얼 함수 짜기
# def factorial(n):
#     if n == 1:
#         return 1
#     elif n == 0:
#         return 1
#     else:
#         return n * factorial(n-1)
#
# print(factorial(5))

# 이진수 만들기 함수
# def binary(n):
# #     if n == 0:
# #         print(0, end="")
# #     elif n == 1:
# #         print(1, end="")
# #     else:
# #         binary(int(n/2))
# #         print(n % 2, end="")
# #
# # binary(15)

