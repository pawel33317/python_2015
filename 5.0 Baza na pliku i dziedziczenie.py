# -*- coding: cp1250 -*-
import locale
import urllib2, urllib, os
locale.setlocale(locale.LC_ALL, '')



class EnhancedFile(file):
    def __init__(self, *args, **keyws):
        file.__init__(self, *args, **keyws)

    def __len__(self):
        return int(os.fstat(self.fileno())[6])

    

class ListOperation(object):
    def saveListTofile(self, filename):
        pass
    def saveToFile(self, filename):
        pass
    def showUsers(self):
        pass

class User:
    def __init__(self, name=None, surname=None, userID=None, mail=None):
        self.name = name
        self.surname=surname
        self.userID=userID
        self.mail=mail

class LocalUsers(ListOperation):
    def __init__(self):
        pass
    def readFromFile(self,fileName):
        f = open(fileName, 'r')
        lineList = f.read().split("\n")
        f.close()
        self.usersList = self.splitLinesIntoUsersObjectsList(lineList);
    def putInNet(self):
        


        theFile = EnhancedFile('dba.txt', 'r')
        theUrl = "http://mmajchr.kis.p.lodz.pl/pwjs/odpowiedz.php"
        theHeaders= {'Content-Type': 'text/xml'}
        theRequest = urllib2.Request(theUrl, theFile, theHeaders)
        response = urllib2.urlopen(theRequest)
        theFile.close()






    
    def splitLinesIntoUsersObjectsList(self,lineList):
        usersList = []
        for i in range(len(lineList)):
            splitedUserLine = lineList[i].split(' ')
            if(len(splitedUserLine) == 4):
                nowy = User(splitedUserLine[0], splitedUserLine[1], splitedUserLine[2],splitedUserLine[3])
            else:
                nowy = User(splitedUserLine[0], splitedUserLine[1], None, None)
            usersList.append(nowy)
        return usersList
    def showUsers(self):
        print "----------Baza Użytkowników----------"
        for i, user in enumerate(self.usersList):
            uid = '' if user.userID == None else user.userID
            umail= '' if user.mail == None else user.mail
            print ("%-3d %-15s %-15s %-15s %-15s" % (i+1,user.name,user.surname,uid,umail))
        print "-------------Koniec Bazy-------------"
    def sortUsers(self,option):
        if option == 0:
            self.usersList.sort(key=lambda x: locale.strxfrm(x.name))
        else:
            self.usersList.sort(key=lambda x: locale.strxfrm(x.surname))
    def addNew(self,newLine):
        self.usersList.extend(self.splitLinesIntoUsersObjectsList(newLine))
    def deleteUser(self,userID):
        self.usersList.pop(userID-1)
    def saveToFile(self,fileName):
        f = open(fileName, 'w')
        fileBuffer = []
        for user in self.usersList:
            uid = '' if user.userID == None else ' '+user.userID
            umail= '' if user.mail == None else ' '+user.mail
            fileBuffer.append(user.name+' '+user.surname+uid+umail)
        f.write('\n'.join(fileBuffer))
        f.close()
    def addUsersFromRemoteFile(self, fileAddress):
        onlineUsers = urllib2.urlopen(fileAddress).read().strip()
        onlineUsers = onlineUsers.split('\n')
        onlineUsers = [line[line.index(' ')+1:].replace(', ',' ') for line in onlineUsers]
        self.usersList.extend(self.splitLinesIntoUsersObjectsList(onlineUsers))

class RemoteUsers(ListOperation):
    def __init__(self):
        pass
    def readFromFile(self,fileName):
        onlineUsers = urllib2.urlopen(fileName).read().strip()
        onlineUsers = onlineUsers.split('\n')
        onlineUsers = [line[line.index(' ')+1:].replace(', ',' ') for line in onlineUsers]
        self.usersList = self.splitLinesIntoUsersObjectsList(onlineUsers)
       
    def splitLinesIntoUsersObjectsList(self,lineList):
        usersList = []
        for i in range(len(lineList)):
            splitedUserLine = lineList[i].split(' ')
            if(len(splitedUserLine) == 4):
                nowy = User(splitedUserLine[0], splitedUserLine[1], splitedUserLine[2],splitedUserLine[3])
            else:
                nowy = User(splitedUserLine[0], splitedUserLine[1], None, None)
            usersList.append(nowy)
        return usersList
    def showUsers(self):
        print "----------Baza Użytkowników----------"
        for i, user in enumerate(self.usersList):
            uid = '' if user.userID == None else user.userID
            umail= '' if user.mail == None else user.mail
            print ("%-3d %-15s %-15s %-15s %-15s" % (i+1,user.name,user.surname,uid,umail))
        print "-------------Koniec Bazy-------------"
    def sortUsers(self,option):
        if option == 0:
            self.usersList.sort(key=lambda x: locale.strxfrm(x.name))
        else:
            self.usersList.sort(key=lambda x: locale.strxfrm(x.surname))
    def addNew(self,newLine):
        self.usersList.extend(self.splitLinesIntoUsersObjectsList(newLine))
    def deleteUser(self,userID):
        self.usersList.pop(userID-1)
    def saveToFile(self,fileName):
        f = open(fileName, 'w')
        fileBuffer = []
        for user in self.usersList:
            uid = '' if user.userID == None else ' '+user.userID
            umail= '' if user.mail == None else ' '+user.mail
            fileBuffer.append(user.name+' '+user.surname+uid+umail)
        f.write('\n'.join(fileBuffer))
        f.close()


myUser1 = LocalUsers()
myUser2 = LocalUsers()
myUser3 = RemoteUsers()
myUser1.readFromFile('db.txt')
myUser1.putInNet();

'''
myUser2.readFromFile('dba.txt')
myUser3.readFromFile('http://mmajchr.kis.p.lodz.pl/pwjs/zadania/lista.txt')
myArr = [myUser1,myUser2,myUser3]
for  ob in myArr:
    ob.showUsers()


while True:
    print "1 - sortowanie po imionach\n2 - sortowanie po nazwiskach\n3 - dodanie uzytkownika"
    print "4 - usunincie uzytkownika\n5 - zapis aktualnego stanu bazy do pliku"
    print "6 - dołącz użytkowników z internetu\n7 - edytuj użytkownika\n8 - wyjscie"
    wybor=int(raw_input('Wybierz: '))
    if wybor == 1:
        myUsers.sortUsers(0)
    elif wybor == 2: 
        myUsers.sortUsers(1)
    elif wybor == 3:
        print "Podan imie i nazwisko oraz opcjonalnie id i email nowego uzytkownika: "
        myUsers.addNew([raw_input('Podaj imie i nazwisko:')])
    elif wybor == 4:  
        print "Podaj id uzytkownika do usuniecia: "
        myUsers.deleteUser(int(raw_input('Wybierz: ')))
    elif wybor == 5:
        myUsers.saveToFile('db2.txt')
        print "Zapisano"
    elif wybor == 6:
        myUsers.addUsersFromRemoteFile('http://mmajchr.kis.p.lodz.pl/pwjs/zadania/lista.txt')
    elif wybor == 7:
        myUsers.editUser(int(raw_input('Podaj id uzytkownika do edycji: ')))
    else:
        break
    myUsers.showUsers()
'''
