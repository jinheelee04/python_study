# Section10
# 파이썬 예외처리의 이해

# 예외 종류
# 문법적으로 에러가 없지만, 코드 실행(런타임) 프로세스에서 발생하는 예외처리도 중요
# linter : 코드 스타일, 문법 체크

# SyntaxError : 잘못된 문법
# 1.
# print('Test)

# 2.
# if True
#     pass

# 3.
# x => y

# NameError : 참조변수 없음
# a = 10
# b = 15
# print(c)

# ZeroDivisionError : 0 나누기 에러
# print(10 / 0)

# IndexError : 인덱스 범위 오버
x = [10, 20, 30]
# print(x[3])

dic = {'name': 'Kim', 'Age': 33, 'City': 'Seoul'}
# print(dic['hobby']) 에러
print(dic.get('hobby')) # None

# AttributeError : 모듈 클래스에 있는 잘못된 속성 사용시에 예외
import time
print(time.time())
# print(time.month()) # AttributeError: module 'time' has no attribute 'month'

# ValueError : 참조 값이 없을 때 발생
x = [1, 5, 9]
# x.remove(10) #ValueError: list.remove(x): x not in list
# x.index(10)

# FileNotFoundError
# f = open('text.txt', 'r') # FileNotFoundError: [Errno 2] No such file or directory: 'text.txt'

# TypeError
x = [1, 2]
y = (1, 2)
z = 'test'

# print(x + y) # TypeError: can only concatenate list (not "tuple") to list
# print(x + z)
# print(x + list(y)) # 형변환해서 더해야함

# 항상 예외가 발생하지 않을 것으로 가정하고 먼저 코딩
# 그 후 런타임 예외 발생시 예외 처리 코딩 권장(EAFP 코딩 스타일)

# 예외 처리 기본
# try : 에러가 발생할 가능성이 있는 코드 실행
# except : 에러명1
# except : 에러명2
# else : 에러가 발생하지 않을 경우 실행
# finally : 항상 실행

# 예제1
name = ['Kim', 'Lee', 'Park']

try:
    z = 'Kim' # Cho 예외 발생
    x = name.index(z)
    print('{} Found it! in name'.format(z, x+1))
except ValueError:
    print('Not found it! - Occured ValueError!')
# try이 정상적으로 실행되었을때만 실행됨
else:
    print('Ok! else!')

# 예제2
name = ['Kim', 'Lee', 'Park']

try:
    z = 'zin'
    x = name.index(z)
    print('{} Found it! in name'.format(z, x+1))
except: # 어떤 에러가 나올지 모를 경우
    print('Not found it! - Occured Error!')
# try이 정상적으로 실행되었을때만 실행됨
else:
    print('Ok! else!')

# 예제
name = ['Kim', 'Lee', 'Park']

try:
    z = 'Kidm'
    x = name.index(z)
    print('{} Found it! in name'.format(z, x+1))
except Exception: # 에러발생했을 경우만
    print('Not found it! - Occured Error!')
else: # 정상일 경우만
    print('Ok! else!')
finally: # 무조건 실행
    print('finally ok!')

# 예제 4
# 예외 처리는 하지 않지만, 무조건 수행되는 코딩 패턴
try:
    print('Try')
finally:
    print('Ok Finally!!!!')
print()
print()
# 예제 4
# 예외 처리는 하지 않지만, 무조건 수행되는 코딩 패턴
try:
    z = 'Kidm'
    x = name.index(z)
    print('{} Found it! in name'.format(z, x+1))
except ValueError as l:
    print(l)
    print('Not found it! - Occurred ValueError!')
except IndexError:
    print('Not found it! - Occurred IndexError!')
except Exception:
    print('Not found it! - Occurred Error!')
else: # 정상일 경우만
    print('Ok! else!')
finally: # 무조건 실행
    print('finally ok!')

# 예외6
# 예외 발생 : raise
# raise 키워드로 예외 직접 발생

try:
    a = 'Kim'
    if a == 'Kim':
        print('Ok 허가!')
    else:
        raise ValueError # 직접 규정해서 예외 발생 처리
except ValueError:
    print('문제 발생!')
except Exception as f:
    print(f)
else:
    print('Ok!')