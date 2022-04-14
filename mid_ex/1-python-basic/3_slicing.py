# # 슬라이싱 응용문제 찾아보기

# word = 'Python'
# print(word[4:42])

# # 슬라이싱을 이용해 새로운 만자열 만들기

# word2 = 'G' + word[1:]
# print(word2)

# outStr = ""
# count, i = 0, 0

# inStr = input('Type string: ')
# count = len(inStr)

# for i in range(0, count):
#     outStr += inStr[count-(i+1)]

# print("Reversed string: ", outStr)


# flag = 'ABC'.isupper()
# flag = 'A B  C'.isspace()
# flag = '   '.isspace()
# print(flag)

# str = "python is easy"
# # str.upper()
# print(str.upper())


# a = [1, 2, 3]
# b = [5, 6, 7]
# print(b+a)

x = ['a', 1, True]
# y = [False , -19 , "hello"]
# print(x+y)

a, b, c = x
print(a, b, c)