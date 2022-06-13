import re

text = '''
긴급한 사항이 있으면 010-1234-5678 또는
010-987-6543으로 연락주세요.
연락이 안되는 경우,
mnnm22@daum.net로 연락주세요.
'''

result = re.findall(r'\d{3}-\d{3,4}-\d{4}', text)
print(result)

# result = re.findall(r'([\w.]+)@(.+)(\.[a-z]{2,3})', text)
result = re.findall(r'([\w.]+)(\.[a-z]{2,3})', text)
print(result)
print(''.join(result[0]))

result = re.findall(r'([\w.]+)(@)(.+)(\.[a-z]{2,3})', text)
print(result)
print(''.join(result[0]))