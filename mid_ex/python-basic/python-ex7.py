#각 자리수 합 구하기
# N = input()
# num = str(N)

# sum = 0
# for i in range(len(num)):
#     sum += int(num[int(i)])
# print(sum)


#1부터 1000까지 자리 수 합
def sum_digit(num):
    total = 0
    str_num = str(num)

    for digit in str_num:
        total += int(digit)

    return total


# sum_digit(1)부터 sum_digit(1000)까지의 합 구하기
result = 0
for i in range(1, 1001):
    result += sum_digit(i)

print(result)