# Section04-2
# 문자열, 문자열 연산, 슬라이싱

str1 = "I am a boy"
str2 = 'NiceMan'
str3 = ''
str4 = str() # str('ace')

print(len(str1), len(str2), len(str3), len(str4)) #공백도 1byte

# 이스케이프 문자
escape_str1 = "Do you have a \"big collection\""
print(escape_str1)
escape_str2 = "Tab\tTab\tTab"
print(escape_str2)

# Raw String
# 있는 그대로 출력
raw_s1  = r'C:\Programs\Test\Bin'
print(raw_s1)
raw_s2 = r"\\a\\a"
print(raw_s2)

# 멀티 라인
multi = \
""" 
문자열 
    
멀티라인 
    
테스트
"""
print(multi)

# 문자열 연산
str_o1 = '*'
str_o2 = 'abc '
str_o3 = 'def'
str_o4 = "Niceman"

print(str_o1 * 100)
print(str_o2 + str_o3)
print(str_o1 * 3)
print('a' in str_o4) # 'a'라는 문자가 str_o4에 포함되어 있냐
print('f' in str_o4)
print('z' not in str_o4)

# 문자열 형 변환
# print(77 + 'a') 에러
# print('a' + 77)  can only concatenate str (not "int") to str
print(str(77) + 'a')
print(str(10.4))

# 문자열 함수
# 참고 : https://www.w3schools.com/python/python_ref_string.asp

# a = 'niceman is good'
# b = 'orange'
#
# # 전체 문자가 소문자인지
# print(a.islower()) # True
# # 마지막 문자가 's'인지
# print(a.endswith('s'))
# # 첫번째 문자 대문자로
# print(a.capitalize())
# # 첫 번째 문자를 두 번째 문자로 바꾸기
# print(a.replace('nice', 'good'))
# # 역순으로 리스트 형태로 반환
# print(list(reversed(b)))

a = 'niceman'
b = 'orange'

print(a[0:3]) # nic
print(a[0:4]) # nice
print(a[0:7]) # niceman
print(a[0:len(a)]) # niceman
print(a[0:len(a)-1]) # nicema
print(a[:]) # 처음부터 끝까지
# 세 번째 옵션이 추가되면 그 값만큼 건너 뛰게 됨
print(b[0:4:2])
print(b[1:-2]) # 1: r, -2 : g, r부터 g이전 까지
print(b[::-1]) # 역순으로 출력