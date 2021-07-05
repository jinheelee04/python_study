# Section02-1
# 파이썬 기초 코딩
# Print 구문의 이해

#기본출력
print('Hello Python!')
print("Hello Python!")
print("""Hello Python!""")
print('''Hello Python!''')

# 줄바꿈
print()

# Separator 옵션 사용
print('T', 'E', 'S','T') # 결과 : T E S T
print('T', 'E', 'S','T', sep='') # 결과 : TEST
print('2019', '02', '19', sep='-') # 결과 : 2019-02-19
print('niceman', 'google.com', sep='@') # 결과 : niceman@gmail.com

# end 옵션 사용
print("Welcome To", end=' ') # 줄바꿈 하지 않음
print('the black parade', end=' ')
print('piano notes')

print()

# format 사용 [] 대괄호 , {} 중괄호, () 소괄호
print('{} and {}'.format('You', 'Me'))
print("{0} and {1} and {0}".format('You', 'Me'))
print("{a} are {b}".format(a='You', b='Me'))

# %s : 문자, %d : 정수, %f : 실수
print("%s's favorite number is %d" % ('Jinhee', 7))

print("Test1: %5d, Price: %4.2f" %(776, 6534.123))
print("Test1: {0: 5d}, Price:{1: 4.2f}".format(776, 6543.123))
print("Test1: {a: 5d}, Price:{b: 4.2f}".format(a=776, b=6543.123))

#참고 : Escape코드
# \n : 개행
# \t : 탭
# \\ : 문자
# \' : 문자
# \" : 문자
# \r : 캐리지 리턴
# \f : 폼 피드
# \a : 벨 소리
# \b : 백 스페이스
# \000 : 널 문자
# '''
# """

print("'you'")
print('\'you\'')
print('"you"')
print('\\you\\\n\n\n\n')
print('\t\t\ttest')

