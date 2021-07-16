# Section12-1
# 파이썬 데이터베이스 연동(SQLite)
# 테이블 생성 및 삽입

import sqlite3
import datetime

# 삽입 날짜 생성
now = datetime.datetime.now()
print('now: ', now)
nowDateTime = now.strftime('%Y-%m-%d %H:%M:%S')
print(nowDateTime)
#sqlite3 version
print('sqlite3.version : ', sqlite3.version) # 버전
print('sqlite3.sqite_version : ', sqlite3.sqlite_version) # 엔진 버전

# DB 생성 & Auto Commit(Rollback)
conn = sqlite3.connect('C:/workspaces/python_learn/resource/database.db', isolation_level=None) # auto commit

# Cursor
c = conn.cursor()
print('Cursor Type : ', type(c))

# 테이블 생성(Data Type : TEXT, NUMERIC INTEGER REAL BLOB)
c.execute("CREATE TABLE IF NOT EXISTS users( id INTEGER PRIMARY KEY, username text, email text\
          , phone text, website text, regdate text )")

# 데이터 삽입
# c.execute("INSERT INTO users VALUES(1, 'Kim', 'Kim@naver.com', '010-0000-0000', 'Kim.com', ?)", (nowDateTime,))
# c.execute("INSERT INTO users(id, username, email, phone, website, regdate) VALUES(?, ?, ? ,?, ?, ?)", (2, 'Park', 'Park@daum.net', '010-1111-1111', 'Park.com', nowDateTime))

# Many 삽입(튜플, 리스트)
userList = (
    (3, 'Lee', 'Lee@naver.com', '010-2222-2222', 'Lee.com', nowDateTime),
    (4, 'Cho', 'Cho@daum.net', '010-3333-3333', 'Cho.com', nowDateTime),
    (5, 'Yoo', 'Yoo@google.com', '010-4444-4444', 'Yoo.net', nowDateTime)
)
# c.executemany("INSERT INTO users(id, username, email, phone, website, regdate) VALUES (?, ?, ?, ?, ?, ?)", userList)
# conn.rollback
# 테이블 데이터 삭제
# conn.execute("DELETE FROM users")
# 삭제한 데이터 수 반환
# print("users db deleted : ", conn.execute("DELETE FROM users").rowcount)

# 커밋 : isolation_level = None 일 경우 자동 반영(으로 커밋)
# conn.commit()

# 롤백
# conn.rollback()

# 접속 해제
conn.close()