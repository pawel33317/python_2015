# -*- coding: cp1250 -*-
import sqlite3
import os.path, os


dbName='example.db'


if os.path.isfile(dbName):
    print "Plik istnieje"
    conn = sqlite3.connect(dbName)
    c = conn.cursor()
else:
    print "plik nie istnieje utworzono"
    conn = sqlite3.connect(dbName)
    c = conn.cursor()
    c.execute('''CREATE TABLE users (imie text, nazwisko text, mail text, nrindex integer)''')


while True:
    print "--------------"
    print "1 - Usuń wszystkie wpisy"
    print "2 - Usuń bazę"
    print "3 - Wczytaj dane z pliku do bazy"
    print "4 - Wyświetl baze danych"
    wybor=int(raw_input('Wybierz: '))
    if wybor == 1:
        c.execute("delete from users")
        print "Wszystkie rekordy usunięte"
        conn.commit()
    elif wybor == 2:
        conn.close()
        os.remove(dbName)
        print "Połączenie z bazą zamknięte"
        print "Baza usunięta"
    elif wybor == 3:
        f = open('baza.txt', 'r')
        usersList = f.read().split("\n")
        for user in usersList:
            userParm = user.split(" ")
            c.execute("INSERT INTO users VALUES ('"+str(userParm[0])+"','"+str(userParm[1])+"','"+str(userParm[3])+"', "+str(userParm[2])+")")
            conn.commit()       
        
        #c.execute("INSERT INTO users VALUES ('Pawel','Czubak','pawel33317@gmai.com', 201520)")
        #conn.commit()
        print "Dodano do bazy dane z pliku"
    elif wybor == 4:
        for row in c.execute('SELECT * FROM users'):
            print str(row[0])+' '+str(row[1])+' '+str(row[2])+' '+str(row[3])
    else:
        break

