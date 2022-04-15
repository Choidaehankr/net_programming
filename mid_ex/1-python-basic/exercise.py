# # 연습문제 1번

# str = "My name is Daehan, Choi"

# def repeat(str):
#     for i in range(0, 10):
#         print(str)

# def fourth_char(str):
#     cnt = 0
#     temp = ""
#     for x in str:
#         if(cnt == 4): 
#             break
#         if(x == ' '):
#             continue
#         temp += x
#         cnt+=1
#     return temp

# print(len(str))  # 문자 수 출력
# repeat(str)  # 문자열 10번 반복
# print(str[0])  # 첫번째 문자
# # print(str[:4])
# print(fourth_char(str))  # 처음 4문자 (공백 제외)
# print(str[::-1])  # 문자열 거꾸로 출력
# print(str[1:-1])  # 첫번째, 마지막 문자 제거
# print(str.upper())  # 대문자
# print(str.lower())  # 소문자
# print(str.replace('a', 'e'))  # a를 e로 변경




    # 연습문제 2번

# friends = ['최대한', '김태경', '이현', '김민수', '백승우']
# friends.insert(0, '윤병수')
# friends.insert(2, '윤병수')
# friends.append('윤병수')
# print(friends)

# numbers = [100, 15, 2.5, 1, 2, 3]
# numbers[1] = 17
# numbers.extend([5, 6, 7])  # 한번에 5 6 7 넣기
# numbers.pop(0)  # 첫번째 요소 제거
# numbers.sort()
# numbers.sort(reverse=True)
# numbers.insert(3, 25)
# print(numbers)

    # 연습문제 3번
