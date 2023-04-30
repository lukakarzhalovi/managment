import sqlite3
import matplotlib.pyplot as plt

 #1ჯამურად რამდენი მგზავრი გადარჩა/ვერ გადარჩა.
def connect(name):
    return sqlite3.connect(name)

# def survive(surv,cu):
#     cu.execute("SELECT count(*) FROM Passengers WHERE Survived = ?",(surv,))
#     return cu.fetchone()[0]

conn = connect("Titanic.sqlite")
cursor = conn.cursor()

# n_survive = survive(1,cursor)
# n_not_surviev = survive(0,cursor)
# min = min(n_survive,n_not_surviev)
# max = max(n_survive,n_not_surviev)
# cursor.execute('''INSERT INTO vall(title,max,min)
#         VALUES("{}", "{}", "{}")'''.format("გადარჩენილთა რაოდენობა", max, min))
# conn.commit()
# conn.close()
# print(n_survive)
# print(n_not_surviev)


    #2 ათ წლიანი რეინჯის მიხედვით, რომელ ასაკობრივ დიაპაზონში რამდენი მგზავრი იყო.

# def Range(age1,age2,cu):
#     cu.execute("SELECT count(*) FROM passengers WHERE age BETWEEN ? AND ?", (age1,age2))
#     return cu.fetchone()[0]

# ten = Range(0,10,cursor)
# twenty = Range(10,20,cursor)
# thirty = Range(20,30,cursor)
# fourthy = Range(30,40,cursor)
# fifthy = Range(40,50,cursor)
# sixty = Range(50,60,cursor)
# seventhy = Range(60,70,cursor)
# eighty = Range(70,80,cursor)
# mylist = [ten,twenty,thirty,fourthy,fifthy,sixty,seventhy,eighty]
# print(ten,twenty,thirty,fourthy,fifthy,sixty,seventhy,eighty)
# max = max(mylist)
# min = min(mylist)
# cursor.execute('''INSERT INTO vall(title,max,min)
#         VALUES("{}", "{}", "{}")'''.format("10 წლიანი შალედის მიხედვით გემზე იმყოფებოდა", f"{max}- ადამიანი {mylist.index(max)*10}-დან {(mylist.index(max)*10)+10}-წლამდე", f"{min}- ადამიანი  {mylist.index(min)*10}-დან {(mylist.index(min)*10)+10}-წლამდე"))
# conn.commit()
# conn.close()


    #3 ათ წლიანი რეინჯის მიხედვით, რომელ ასაკობრივ დიაპაზონში რამდენი მგზავრი გადარჩა/ვერ გადარჩა.

# def Range(age1,age2,surv,cu):
#     cu.execute("SELECT count(*) FROM passengers WHERE (age BETWEEN ? AND ?) AND survived = ?", (age1,age2,surv))
#     if surv == 0 :
#         return cu.fetchone()[0]
#     elif surv == 1 :
#         return cu.fetchone()[0]

# ten = Range(0,10,1,cursor)
# twenty = Range(10,20,1,cursor)
# thirty = Range(20,30,1,cursor)
# fourthy = Range(30,40,1,cursor)
# fifthy = Range(40,50,1,cursor)
# sixty = Range(50,60,1,cursor)
# seventhy = Range(60,70,1,cursor)
# eighty = Range(70,80,1,cursor)
# mylist = [ten,twenty,thirty,fourthy,fifthy,sixty,seventhy,eighty]
# print(mylist)
# max = max(mylist)
# min = min(mylist)
# cursor.execute('''INSERT INTO vall(title,max,min)
#         VALUES("{}", "{}", "{}")'''.format("10 წლიანი შუალედში გადარჩენილთა რაოდენობა", f"{max}- ადამიანი გადარჩა {mylist.index(max)*10}-დან {(mylist.index(max)*10)+10}-წლამდე", f"{min}- ადამიანი გადარჩა {mylist.index(min)*10}-დან {(mylist.index(min)*10)+10}-წლამდე"))
# conn.commit()

# ten = Range(0,10,0,cursor)
# twenty = Range(10,20,0,cursor)
# thirty = Range(20,30,0,cursor)
# fourthy = Range(30,40,0,cursor)
# fifthy = Range(40,50,0,cursor)
# sixty = Range(50,60,0,cursor)
# seventhy = Range(60,70,0,cursor)
# eighty = Range(70,80,0,cursor)
# mylist1 = [ten,twenty,thirty,fourthy,fifthy,sixty,seventhy,eighty]
# print(mylist1)
# max = max(mylist1)
# min = min(mylist1)
# cursor.execute('''INSERT INTO vall(title,max,min)
#         VALUES("{}", "{}", "{}")'''.format("10 წლიანი შუალედში გარდაცვლილთა რაოდენობა", f"{max}- ადამიანი დაიღუპა {mylist1.index(max)*10}-დან {(mylist1.index(max)*10)+10}-წლამდე", f"{min}- ადამიანი დაიღუპა {mylist1.index(min)*10}-დან {(mylist1.index(min)*10)+10}-წლამდე"))
# conn.commit()



    #4 ბილეთის კლასის მიხედვით, რამდენი იყო ბილეთის საშუალო ფასი თითოეული კლასისთვის.

def Ticket_Class(cu):
    cu.execute("SELECT AVG(Fare),Pclass FROM passengers group by Pclass")
    return cu.fetchall()
# A_class = Ticket_Class(1,cursor)
# B_class = Ticket_Class(2,cursor)
# C_class = Ticket_Class(3,cursor)
print(Ticket_Class(cursor))
# mylist = [A_class,B_class,C_class]
# min = min(mylist)
# max = max(mylist)
# cursor.execute('''INSERT INTO vall(title,max,min)
#          VALUES("{}", "{}", "{}")'''.format("ვინ რომელი კლასით მგზავრობა", f"{max}-მგზავრობდა {mylist.index(max)+1} კლასით", f"{min}-მგზავრობდა {mylist.index(min)+1} კლასით"))
# conn.commit()

    #5 ჩასხდომის ადგილის მიხედვით, სად რამდენი მგზავრი ავიდა გემზე.

# def Where(plc,cu):
#     cu.execute("SELECT count(*) FROM passengers WHERE Embarked == ?",(plc))
#     return cu.fetchone()[0]
# c_pass = Where("C", cursor)
# q_pass = Where("Q", cursor)
# s_pass = Where("S", cursor)
# print(c_pass,q_pass,s_pass)
# max = max(c_pass,q_pass,s_pass)
# min = min(c_pass,q_pass,s_pass)
# cursor.execute('''INSERT INTO vall(title,max,min)
#          VALUES("{}", "{}", "{}")'''.format("სად რამდენი მგზავრი ავიდა გემზე", f"{max}-მგზავრი ავიდა Southampton-ში", f"{min}-მგზავრი ავიდა Queenstown-ში"))
# conn.commit()
 # Create table

# cursor.execute('''CREATE TABLE vall(
#                id INTEGER PRIMARY KEY AUTOINCREMENT,
#                title VARCHAR (50),
#                max FLOAT (25),
#                min FLOAT(25))''')

