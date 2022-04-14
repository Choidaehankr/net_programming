# # Separator 사용

# print('2022', '03', '02', sep='_')  # 단어 사이 ' _ '를 추가

# # format 사용

# print('{} and {}'.format('You', 'Me'))
# print("{0} and {1} and {2}".format('You', "Me", "We"))

# # %s, %d %f

# print("%s's favorite number is %d" %('Daehan', 8))

# print("Test1: %5d, Price: %4.2f" %(7761, 6534.123))
# # %5d: 5자리의 숫자가 온다고 자릿수를 지정, %4.2f: 정수 4자리 소수 2자리 인 실수
# print("Test1: {0:5d}, Price: {1:4.2f}".format(776, 765432.123456))
# print("Test1: {a:5d}, Price: {b:4.2f}".format(a=776, b=6534.123))


# a = 2
# b = 2
# print(id(a))
# print(id(b))
# # print(id(a) == id(b))
# a += 1
# print(id(a))
# print(id(b))

    # 10진수를 입력 받아 2진수로 변환하여 출력하는 프로그램. 8진수, 16진수 각? ㄷㄷ;

n = int(input('Number: '))
result = ''

while n != 0:
    # m = n % 2
    m = n % 8
    result = str(m) + result
    n = n // 8

print(result)