# -*- coding: cp1250 -*-
import locale
locale.setlocale(locale.LC_ALL, '')
def showUsers(usersList):
    print "Baza użytkowników: "
    for i in range(len(usersList)):
        print str(i+1) + " - " + usersList[i]
def sortt(x):
    print x
    return locale.strxfrm(x[0])
f = open('db.txt', 'r')
usersList = f.read().split("\n")
f.close()
showUsers(usersList)
while True:
    print "--------------\n1 - sortowanie po imionach\n2 - sortowanie po nazwiskach\n3 - dodanie użytkownika"
    print "4 - usunięcie użytkownika\n5 - zapis aktualnego stanu bazy do pliku\n6 - wyjście\n--------------\n"
    wybor=int(raw_input('Wybierz: '))
    if (wybor == 1) or (wybor == 2) :
        user = []
        for i in range(len(usersList)):
            user.append([usersList[i][:usersList[i].index(' ')], usersList[i][usersList[i].index(' '):]])
        if wybor == 1:
            user.sort(key=sortt)
        else:
            user.sort(key=lambda x: locale.strxfrm(x[1]))
        usersList = []
        for i in range(len(user)):
            usersList.append(user[i][0]+user[i][1])
    elif wybor == 3:
        print "Podan imię i nazwisko nowego użytkownika: "
        newUser=raw_input('Podaj imie i nazwisko:')
        usersList.append(newUser)
    elif wybor == 4:  
        print "Podaj id użytkownika do usunięcia: "
        deleteUserId=int(raw_input('Wybierz: '))
        usersList.pop(deleteUserId-1)
    elif wybor == 5:
        f = open('db2.txt', 'w')
        f.write('\n'.join(usersList))
        f.close()
        print "Zapisano"
    else:
        break
    showUsers(usersList)
