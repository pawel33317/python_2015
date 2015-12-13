# -*- coding: cp1250 -*-
import locale
locale.setlocale(locale.LC_ALL, '')
def showUsers(splitedUsersList):
    print "Baza uzytkownikow: "
    for i in range(len(splitedUsersList)):
        print str(i+1) + " - " + splitedUsersList[i][0] + " " + splitedUsersList[i][1] + " sep: " + splitedUsersList[i][2]
 
 
def splitUsers(usersList):
    splitedUsersList = []
    for i in range(len(usersList)):
        separator=False
        for j in range(len(usersList[i])):   
            if (usersList[i][j].isspace()!=True) and (usersList[i][j].isalpha()!=True) and (separator == False):
                separator = usersList[i][j]   
        splitedUsersList.append([usersList[i][:usersList[i].index(separator)], usersList[i][usersList[i].index(separator)+1:], separator])
    return splitedUsersList
 
 
f = open('db.txt', 'r')
usersList = f.read().split("\n")
f.close()
splitedUsersList = splitUsers(usersList)
showUsers(splitedUsersList)
while True:
    print "--------------\n1 - sortowanie po imionach\n2 - sortowanie po nazwiskach\n3 - dodanie uzytkownika"
    print "4 - usunincie uzytkownika\n5 - zapis aktualnego stanu bazy do pliku\n6 - wyjscie\n--------------\n"
    wybor=int(raw_input('Wybierz: '))
    if wybor == 1:
        splitedUsersList.sort(key=lambda x: locale.strxfrm(x[0]))
    elif wybor == 2: 
        splitedUsersList.sort(key=lambda x: locale.strxfrm(x[1]))
    elif wybor == 3:
        print "Podan imie i nazwisko nowego uzytkownika: "
        splitedUsersList = splitedUsersList + splitUsers([raw_input('Podaj imie i nazwisko:')])
    elif wybor == 4:  
        print "Podaj id uzytkownika do usuniecia: "
        deleteUserId=int(raw_input('Wybierz: '))
        splitedUsersList.pop(deleteUserId-1)
    elif wybor == 5:
        f = open('db2.txt', 'w')
        fileBuffer = []
        for i in range(len(splitedUsersList)):
            fileBuffer.append(splitedUsersList[i][0]+""+splitedUsersList[i][2]+""+splitedUsersList[i][1])
        f.write('\n'.join(fileBuffer))
        f.close()
        print "Zapisano"
    else:
        break
    showUsers(splitedUsersList)
 
