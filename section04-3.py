# Section04-3
# 파이썬 데이터 타입(자료형)
# 리스트, 튜플

# 리스트 (순서o, 중복o, 수정o, 삭제o)
# 선언
a = []
b = list()
c = [1, 2, 3, 4]
d = [10, 100, 'Pen', 'Banana', 'Orange']
e = [10, 100, ['Pen', 'Banana', 'Orange']]

# 인덱싱
print(d[3])
print(d[-2])
print(d[0]+d[1])
print(e[2][1])
print(e[-1][-2])

# 슬라이싱
print(d[0:3])
print(d[0:1])
print(e[2][1:3])

# 연산
print(c + d)
print(c * 3)
print(str(c[0])+'hi')

# 리스트 수정, 삭제
c[0] = 77
print(c)

c[1:2] = [100, 1000, 10000]
print(c)
c[1] = ['a', 'b', 'c']
print(c)

del c[1]
print(c)
del c[-1]
print(c)
print()
print()

# 리스트 함수
y = [5, 2, 3, 1, 4]
print(y)
y.append(6) # 끝에 추가
print(y)
y.sort()
print(y)
y.reverse()
print(y)
y.insert(2,7) # 2번 인덱스에 7 추가
print(y)
y.remove(2) # 데이터의 값을 가지고 삭제 (숫자 2가 지워짐)
print(y)
y.pop() # 마지막 요소 꺼내고 삭제
print(y) # LIFO last in first out
ex = [88, 77]
# y.append(ex) # [6, 5, 7, 4, 3, [88, 77]]
y.extend(ex) # 끝분분에 원소 추가 : [6, 5, 7, 4, 3, 88, 77]
print(y)
print()
print()
# 삭제 : del, remove, pop

# 튜플 (순서o, 중복o, 수정x, 삭제x)
a = ()
b = (1,)
c = (1, 2, 3, 4)
d = (10, 100, ('a', 'b', 'c'))
# del c[2]  # TypeError: 'tuple' object doesn't support item deletion

# 인덱싱
print(c[2])
print(c[3])
print(d[2][1])

print(d[2:])
print(d[2][0:2])

# 연산
print(c + d)
print(c * 3)
print()
print()

# 튜플 함수
z = (5, 2, 1, 3, 4, 1)

print(z)
print(3 in z)
print(z.index(5)) # 값이 3인 것의 인덱스
print(z.count(1)) # 값이 1인 것이 몇개나 있는가?