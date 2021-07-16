# Section12-3
# 파이썬 데이터베이스 연동(SQLite)
# 테이블 데이터 수정 및 삭제

import sqlite3

# DB생성(파일)
conn = sqlite3.connect('c:/workspaces/python_learn/resource/database.db')

# Cursor 연결
c = conn.cursor()

# 데이터 수정1
# c.execute("UPDATE users SET username = ? WHERE id = ?", ('niceman', 2))

# 데이터 수정2
# c.execute("UPDATE users SET username = :name WHERE id = :id ", {"name": 'goodman', "id": 5})

# 데이터 수정3
# c.execute("UPDATE users SET username = '%s' WHERE id= '%s'" % ('badboy', 3))



# 중간 데이터 확인1
for user in c.execute("SELECT * FROM users"):
    print(user)

# Row Delete1
c.execute("DELETE FROM users WHERE id = ?", (2,))

# Row Delete2
c.execute("DELETE FROM users WHERE id = :id",{"id": 5})

# Row Delete3
c.execute("DELETE FROM users WHERE id = '%s'" % 4)
print()
# 중간 데이터 확인2
for user in c.execute("SELECT * FROM users"):
    print(user)

# 테이블 전체 데이터 삭제
print("users db deleted : ", conn.execute("DELETE FROM users").rowcount, "rows")

# 커밋
conn.commit()

# 접속 해체
conn.close()