# -*- coding: cp1250 -*-
import locale
import urllib2
locale.setlocale(locale.LC_ALL, '')
class User:
    def __init__(self, name=None, surname=None, userID=None, mail=None):
        self.name = name
        self.surname=surname
        self.userID=userID
        self.mail=mail
        
def readFromFile(fileName):
    f = open(fileName, 'r')
    lineList = f.read().split("\n")
    f.close()
    return lineList
def splitLinesIntoUsersObjectsList(lineList):
    usersList = []
    for i in range(len(lineList)):
        splitedUserLine = lineList[i].split(' ')
        if(len(splitedUserLine) == 4):
            nowy = User(splitedUserLine[0], splitedUserLine[1], splitedUserLine[2],splitedUserLine[3])
        else:
            nowy = User(splitedUserLine[0], splitedUserLine[1], None, None)
        usersList.append(nowy)
    return usersList
def showUsers(usersList):
    print "----------Baza Użytkowników----------"
    for i, user in enumerate(usersList):
        uid = '' if user.userID == None else user.userID
        umail= '' if user.mail == None else user.mail
        print ("%-3d %-15s %-15s %-15s %-15s" % (i+1,user.name,user.surname,uid,umail))
    print "-------------Koniec Bazy-------------"
lineList = readFromFile('db.txt')
usersList = splitLinesIntoUsersObjectsList(lineList);
showUsers(usersList)

while True:
    print "1 - sortowanie po imionach\n2 - sortowanie po nazwiskach\n3 - dodanie uzytkownika"
    print "4 - usunincie uzytkownika\n5 - zapis aktualnego stanu bazy do pliku"
    print "6 - dołącz użytkowników z internetu\n7 - edytuj użytkownika\n8 - wyjscie"
    wybor=int(raw_input('Wybierz: '))
    if wybor == 1:
        usersList.sort(key=lambda x: locale.strxfrm(x.name))
    elif wybor == 2: 
        usersList.sort(key=lambda x: locale.strxfrm(x.surname))
    elif wybor == 3:
        print "Podan imie i nazwisko oraz opcjonalnie id i email nowego uzytkownika: "
        usersList.extend(splitLinesIntoUsersObjectsList([raw_input('Podaj imie i nazwisko:')]))
    elif wybor == 4:  
        print "Podaj id uzytkownika do usuniecia: "
        deleteUserId=int(raw_input('Wybierz: '))
        usersList.pop(deleteUserId-1)
    elif wybor == 5:
        f = open('db2.txt', 'w')
        fileBuffer = []
        for user in usersList:
            uid = '' if user.userID == None else ' '+user.userID
            umail= '' if user.mail == None else ' '+user.mail
            fileBuffer.append(user.name+' '+user.surname+uid+umail)
        f.write('\n'.join(fileBuffer))
        f.close()
        print "Zapisano"
    elif wybor == 6:
        onlineUsers = urllib2.urlopen('http://mmajchr.kis.p.lodz.pl/pwjs/zadania/lista.txt').read().strip()
        onlineUsers = onlineUsers.split('\n')
        onlineUsers = [line[line.index(' ')+1:].replace(', ',' ') for line in onlineUsers]
        usersList.extend(splitLinesIntoUsersObjectsList(onlineUsers))
    elif wybor == 7:
        editUserID=int(raw_input('Podaj id uzytkownika do edycji: '))
        uditedUser = User();
        uditedUser.name = raw_input("Podaj imię (enter jeśli to samo): ")
        uditedUser.surname = raw_input("Podaj nazwisko (enter jeśli to samo): ")
        uditedUser.userID = raw_input("Podaj numer (enter jeśli to samo): ")
        uditedUser.mail = raw_input("Podaj mail (enter jeśli to samo): ")
        uditedUser.name = usersList[editUserID-1].name if uditedUser.name == '' else uditedUser.name
        uditedUser.surname = usersList[editUserID-1].surname if uditedUser.surname == '' else uditedUser.surname
        uditedUser.userID = usersList[editUserID-1].userID if uditedUser.userID == '' else uditedUser.userID
        uditedUser.mail = usersList[editUserID-1].mail if uditedUser.mail == '' else uditedUser.mail
        usersList[editUserID-1] = uditedUser
    else:
        break
    showUsers(usersList)


    
#print vars(usersList[0])






















