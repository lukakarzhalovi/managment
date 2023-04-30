import sqlite3

## ბაზის დაკავშირება/შექმნა
conn = sqlite3.connect('Titanic.sqlite') # db3; sqlite, sqlite3
#conn.row_factory = sqlite3.Row

cursor = conn.cursor()

# tables in bazashi 
conn = sqlite3.connect('Titanic.sqlite')
cursor = conn.cursor()
cursor.execute("SELECT name FROM sqlite_master WHERE type='table'")
tables = cursor.fetchall()

# Print the names of all the tables
# for table in tables:
#     print(table[0])


#ცხრილიდან სრული ინფორმაციის წამოღება
# res = cursor.execute('select * from Passengers')
# for i in res:
#     print(i)

# # 1) count 
# cursor.execute("select count(*) from Passengers where Survived=1 ")
# print(cursor.fetchall())


# cursor.execute("select count(DISTINCT(Age)) from Passengers")
# print(cursor.fetchall())



# 10 wlisdiapazonshi asakebis datvla
cursor.execute("select (FLOOR(age/10)*10) as range, COUNT(*) as passenger_count from passengers group by range")
rows = cursor.fetchall()
print(rows)
for row in rows:
    range = row[0]
    passenger_count = row[1]
    if range is None:
        range = 0
    if passenger_count is None:
        passenger_count = 0
    print("asakiii: {}-{} mde, raodenoba: {}".format(range, range+9, passenger_count))


# gadarcha ver gadacha

# cursor.execute("select (FLOOR(age/10)*10) as range, survived, count(*) as passenger from passengers GROUP BY range, survived")

# rows = cursor.fetchall()
# for row in rows:
#     range = row[0]
#     survived = row[1]
#     passenger = row[2]
#     if range is None:
#         range = 0
#     if survived == 1:
#         print("asakshu {}-{} mde, gadarcha {}".format(range, range+9, passenger))
#     else:
#         print("asakit {}-{} mde, vergadarcha {}".format(range, range+9, passenger))


# ბილეთის კლასის მიხედვით, რამდენი იყო ბილეთის საშუალო ფასი თითოეული კლასისთვის.


# cursor.execute("select pclass, AVG(fare) as sashualo from passengers group by pclass")
# rows = cursor.fetchall()
# for row in rows:
#     print("clasi: {}, sashualofasi: {}".format(row[0], row[1]))


# ჩასხდომის ადგილის მიხედვით, სად რამდენი მგზავრი ავიდა გემზე.


# cursor.execute("select embarked, COUNT(*) as mgzavrtaraodenoba FROM passengers group by embarked")
# rows = cursor.fetchall()
# for row in rows:
#     print("chasxdomis adgili: {}, raodenoba: {}".format(row[0], row[1]))


# cursor.execute('''CREATE TABLE minimalurimaqsimaluri (
#                     saxelitipi,
#                     max_value REAL,
#                     min_value REAL
#                 )''')

# cursor.execute("INSERT INTO items (saxelitipi, max_value, min_value) VALUES (?, ?, ?, ?)", ('',  100.0, -50.0))
# cursor.execute("INSERT INTO items (saxelitipi, max_value, min_value) VALUES (?, ?, ?, ?)", ('',  100.0, -50.0)) 
# #  ameebshi unda chavsvat mnishvnelobebi boloss da egaaa  prosta ver vaswreb da magito  ar gamiweriaaa ;))
# cursor.execute("INSERT INTO items (saxelitipi, max_value, min_value) VALUES (?, ?, ?, ?)", ('',  100.0, -50.0))
# conn.commit()
# conn.close()