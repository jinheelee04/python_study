# Section09
# 파일 읽기, 쓰기
# 읽기 모드 : r, 쓰기 모드(기존 파일 삭제) : w, 추가 모드(파일 생성 또는 추가): a
# .. : 상대 경로, . : 절대 경로
# 기타 : https://docs.python.org/3.7/library/functions.html#open

# 파일 읽기
# 예제1
f = open('./resource/review.txt')
content = f.read()
print(content)
print(dir(f))
# 반드시 close 리소스 반환
f.close()
print("--------------------------------")
print("--------------------------------")
# 예제2
# with 문이 끝나면 close를 하지 않아도 자동으로 반환 해줌
with open('./resource/review.txt', 'r') as f:
    c = f.read()
    print(c)
    print(list(c))
    print(iter(c))
print("--------------------------------")
print("--------------------------------")

# 예제3
with open('./resource/review.txt', 'r') as f:
    for c in f:
        print(c.strip())

print("--------------------------------")
print("--------------------------------")

# 예제4
with open('./resource/review.txt', 'r') as f:
    content = f.read() # 한번에 읽어옴
    print(">", content)
    content = f.read() # 내용 없음
    print(">", content)
print("--------------------------------")
print("--------------------------------")

# 예제5
with open('./resource/review.txt', 'r') as f:
    line = f.readline()
    while line:
        print(line, end=' ##### ')
        line = f.readline()
print("--------------------------------")
print("--------------------------------")

# 예제 6
with open('./resource/review.txt', 'r') as f:
    contents = f.readlines() # list 반환
    print(contents)
    for c in contents:
        print(c, end=' ***** ')
print("--------------------------------")
print("--------------------------------")
print()
# 예제 7
score = []
with open('./resource/score.txt', 'r') as f:
    for line in f:
        score.append(int(line))
    print(score)
print('Average : {:6.4}'.format(sum(score)/len(score)))
print()
print()

# 파일 쓰기
# 예제1
with open('./resource/text1.txt', 'w') as f:
    f.write('niceman!\n')

# 예제2
with open('./resource/text1.txt', 'a') as f:
    f.write('goodman!\n')

# 예제3
from random import randint

with open('./resource/text2.txt', 'w') as f:
    for cnt in range(6):
        f.write(str(randint(1, 50))) # 0부터 50이하의 랜덤 값 생성
        f.write('\n')

# 예제4
# writelines : 리스트 -> 파일로 저장
with open('./resource/text3.txt','w') as f:
    list = ['Kim\n', 'Park\n', 'Cho\n']
    f.writelines(list)

# 예제5
with open('./resource/text4.txt', 'w') as f:
    print('Test Contests1!', file=f)
    print('Test Contests2!', file=f)
