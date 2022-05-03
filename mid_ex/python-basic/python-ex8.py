from numpy import square


N = [] #수로 구성되는 리스트
S = [] #제곱으로 구성되는 리스트

for i in range(50):
    N.append(int(i))
print(N)

for j in range(50):
    S.append(square(int(j)))
print(S)