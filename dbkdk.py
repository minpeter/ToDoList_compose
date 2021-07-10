
cur.execute("insert into test values (?, ?, ?)", ('peter', 1, 13))
conn.commit()

cur.execute("insert into test values (:name, :score, :age)", {'name':'kali', 'score':99, 'age':16})
conn.commit()

data = [
 ('d', 93, 33),
 ('e', 11, 22)
]

cur.executemany("insert into test values (?, ?, ?)", data)
conn.commit()

cur.execute('select * from test')
for row in cur:
    print(row)

cur.execute("update test set score=11 where name='peter'")
conn.commit()

cur.execute("delete from test where name='e'")
conn.commit()

cur.execute("select * from test")
rows = cur.fetchall()

print (rows)

conn.close()