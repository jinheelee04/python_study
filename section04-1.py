# 데이터 타입

v_str1 = "Niceman"
v_bool = True # True/False
v_str2 = "Goodboy"
v_float =10.3
v_int = 7
v_dict = {
    "name" : "Kim",
    "age"  : 25
           }
v_list = [3, 5, 7]
v_tuple =3, 5, 7
v_set = {7, 8 ,9}

print(type(v_str1))
print(type(v_bool))
print(type(v_str2))
print(type(v_float))
print(type(v_int))
print(type(v_dict))
print(type(v_list))
print(type(v_tuple))
print(type(v_set))

# 연산자
# +, -, *, / : 사칙연산
# // : 나누기(몫), % : 나누기(나머지), **: 지수(제곱)

i1 = 39
i2 = 939
big_int1 = 99999999999999999999999999999999999999999
big_int2 = 77777777777777777777777777777777777777777
f1 = 1.234
f2 = 3.784
f3 = .5
f4 = 10.

print(i1 * i2)
print(big_int1 * big_int2)
print(f1 ** f2) # 제곱
print(f3 + i2) # 자동 형변환

result = f3 + i2
print(result, type(result))

a = 5. # float
b = 4 # int
c = 10

print(type(a), type(b))
result2 = a + b
print(result2)

# 형변환
# int, float, complex(복소수)

print(int(result2))
print(float(c))
print(complex(3)) # (3+0j)
print(int(True)) # 1
print(int(False)) # 0
print(int('3')) # 문자 -> 숫자
print(complex(False)) # 0j

# 단항 연산자
y = 100
y += 100
print(y)

# 수치 연산 함수
# https://docs.python.org/3/library/math.html

print(abs(-7)) # 절대값
n, m = divmod(100, 8)
print(n , m) # n: 몫, m: 나머지

import math

print(math.ceil(5.1))
print(math.floor(3.874))
