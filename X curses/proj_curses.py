# -*- coding: utf-8 -*-
import locale, time
import urllib2,curses
from curses import wrapper
import curses.textpad as textpad
locale.setlocale(locale.LC_ALL, '')

zz = 0
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
        splitedUserLine = lineList[i].strip().rstrip().split(' ')
        if(len(splitedUserLine) == 4):
            nowy = User(splitedUserLine[0].strip().rstrip(), splitedUserLine[1].strip().rstrip(), splitedUserLine[2].strip().rstrip(),splitedUserLine[3].strip().rstrip())
        else:
            nowy = User(splitedUserLine[0].strip().rstrip(), splitedUserLine[1].strip().rstrip(), None, None)
        usersList.append(nowy)
    return usersList
def showUsers(usersList,stdscr):
    global zz
    stdscr.addstr(0, 0, "--------------------Baza Użytkowników--------------------", curses.A_REVERSE)
    height,width = stdscr.getmaxyx()
    zz = 0
    for i, user in enumerate(usersList):
	if zz >= (height-20):
	    stdscr.addstr(zz+1, 0, "Wcisnij przycisk aby wypisac dalsza czesc")
	    stdscr.refresh() 
	    zz=0
	    stdscr.refresh()
            wait=stdscr.getch()
	    stdscr.addstr(0, 0, "--------------------Baza Użytkowników--------------------", curses.A_REVERSE)
	    stdscr.clear()
	    stdscr.clear()
	    stdscr.refresh()
	    stdscr.addstr(0, 0, "--------------------Baza Użytkowników--------------------", curses.A_REVERSE)
        uid = ' ' if user.userID == None else user.userID
        umail= ' ' if user.mail == None else user.mail
	stdscr.addstr(zz+1, 0, str(i+1))
	stdscr.addstr(zz+1, 3, user.name)
	stdscr.addstr(zz+1, 15, user.surname)
	stdscr.addstr(zz+1, 30, uid)
	stdscr.addstr(zz+1, 40, umail) 
	zz+=1
    stdscr.refresh()
    stdscr.addstr(zz+1,0, "-----------------------Koniec Bazy-----------------------", curses.A_REVERSE)

def main(stdscr):
	global zz
	lineList = readFromFile('db.txt')
	usersList = splitLinesIntoUsersObjectsList(lineList);
	while True:
	    stdscr.clear()
	    showUsers(usersList,stdscr)
	    dims = stdscr.getmaxyx()
	    stdscr.addstr(zz+3, 5, "1 - sortowanie po imionach", curses.A_REVERSE)
	    stdscr.addstr(zz+4, 5, "2 - sortowanie po nazwiskach", curses.A_REVERSE)
	    stdscr.addstr(zz+5, 5, "3 - dodanie uzytkownika", curses.A_REVERSE)
	    stdscr.addstr(zz+6, 5, "4 - usunincie uzytkownika", curses.A_REVERSE)
	    stdscr.addstr(zz+7, 5, "5 - zapis aktualnego stanu bazy do pliku", curses.A_REVERSE)
	    stdscr.addstr(zz+8, 5, "6 - dołącz użytkowników z internetu", curses.A_REVERSE)
	    stdscr.addstr(zz+9, 5, "7 - edytuj użytkownika", curses.A_REVERSE)
	    stdscr.addstr(zz+10, 5, "8 - wypisz ładnie", curses.A_REVERSE)
	    stdscr.addstr(zz+11, 5, "9 - wyjscie", curses.A_REVERSE)
	
	    stdscr.refresh()

	    stdscr.addstr(zz+13, 5, "Podaj znak: ")
	    stdscr.refresh()
	    wybor=int(stdscr.getch())
	    stdscr.refresh()

	    if wybor == ord(str(1)):
		usersList.sort(key=lambda x: locale.strxfrm(x.name))
	    elif wybor == ord(str(2)): 
		usersList.sort(key=lambda x: locale.strxfrm(x.surname))
	    elif wybor == ord(str(3)):
		u = User()

		stdscr.clear()
		curses.echo()
	 	stdscr.addstr(0, 0, "Podaj imie: ")
		stdscr.clrtoeol()
		u.name = stdscr.getstr()
		stdscr.insertln()
		stdscr.addstr(1, 0, "Imię: " + u.name + "")

	 	stdscr.addstr(0, 0, "Podaj nazwisko: ")
		stdscr.clrtoeol()
		u.surname = stdscr.getstr()
		stdscr.insertln()
		stdscr.addstr(1, 0, "Nazwisko: " + u.surname + "")

	 	stdscr.addstr(0, 0, "Podaj id: ")
		stdscr.clrtoeol()
		u.userID = stdscr.getstr()
		stdscr.insertln()
		stdscr.addstr(1, 0, "ID: " + u.userID + "")

	 	stdscr.addstr(0, 0, "Podaj email: ")
		stdscr.clrtoeol()
		u.mail = stdscr.getstr()
		stdscr.insertln()
		stdscr.addstr(1, 0, "Email: " + u.mail + "")

		curses.noecho()
		usersList.append(u)
		stdscr.clear()
		stdscr.refresh()
	    elif wybor == ord(str(4)):  
		stdscr.addstr(len(usersList)+15, 5, "Podaj id uzytkownika do usuniecia: ")
		stdscr.addstr(len(usersList)+16, 5, "Wybierz: ")
		deleteUserId=int(chr(stdscr.getch()))
		usersList.pop(deleteUserId-1)
	    elif wybor == ord(str(5)):
		f = open('db2.txt', 'w')
		fileBuffer = []
		for user in usersList:
		    uid = '' if user.userID == None else ' '+user.userID
		    umail= '' if user.mail == None else ' '+user.mail
		    fileBuffer.append(user.name+' '+user.surname+uid+umail)
		f.write('\n'.join(fileBuffer))
		f.close()
		stdscr.clear()
	 	stdscr.addstr(5,0, "-------------------------ZAPISANO-------------------------", curses.A_REVERSE)
		stdscr.refresh()
		time.sleep(1)
		stdscr.clear()
	    elif wybor == ord(str(6)):
		onlineUsers = urllib2.urlopen('http://mmajchr.kis.p.lodz.pl/pwjs/zadania/lista.txt').read().strip()
		onlineUsers = onlineUsers.split('\n')
		onlineUsers = [line[line.index(' ')+1:].replace(', ',' ') for line in onlineUsers]
		usersList.extend(splitLinesIntoUsersObjectsList(onlineUsers))
	    elif wybor == ord(str(7)):
		stdscr.addstr(len(usersList)+15, 5, "Podaj id uzytkownika do edycji: ")
		curses.echo()
		editUserID=int(stdscr.getstr())
		u = User();

		stdscr.clear()
		
	 	stdscr.addstr(0, 0, "Podaj imie (enter jeżeli to samo ("+str(usersList[editUserID-1].name)+")): ")
		stdscr.clrtoeol()
		u.name = stdscr.getstr()
		if u.name.strip().rstrip() == "":
			u.name = usersList[editUserID-1].name
		stdscr.insertln()
		stdscr.addstr(1, 0, "Imię: " + u.name + "")

	 	stdscr.addstr(0, 0, "Podaj nazwisko:  (enter jeżeli to samo ("+str(usersList[editUserID-1].surname)+")): ")
		stdscr.clrtoeol()
		u.surname = stdscr.getstr()
		if u.surname.strip().rstrip() == "":
			u.surname = usersList[editUserID-1].surname
		stdscr.insertln()
		stdscr.addstr(1, 0, "Nazwisko: " + u.surname + "")

	 	stdscr.addstr(0, 0, "Podaj id:  (enter jeżeli to samo ("+str(usersList[editUserID-1].userID)+")): ")
		stdscr.clrtoeol()
		u.userID = stdscr.getstr()
		if u.userID.strip().rstrip() == "":
			u.userID = usersList[editUserID-1].userID
		stdscr.insertln()
		stdscr.addstr(1, 0, "ID: " + u.userID + "")

	 	stdscr.addstr(0, 0, "Podaj email:  (enter jeżeli to samo ("+str(usersList[editUserID-1].mail)+")): ")
		stdscr.clrtoeol()
		u.mail = stdscr.getstr()
		if u.mail.strip().rstrip() == "":
			u.mail = usersList[editUserID-1].mail
		stdscr.insertln()
		stdscr.addstr(1, 0, "Email: " + str(u.mail) + "")
		usersList[editUserID-1] = u
	    elif wybor == ord(str(8)):
		curses.init_pair(1, curses.COLOR_RED, curses.COLOR_BLACK,)
		curses.init_pair(2, curses.COLOR_CYAN, curses.COLOR_BLACK)
		curses.init_pair(3, curses.COLOR_GREEN, curses.COLOR_BLACK)
		stdscr.clear()
		height,width = stdscr.getmaxyx()
		curses.A_BOLD
		tableWidth = []
		for i in range(1,4):
		    tableWidth.append(round(width/4*i))
		tableWidth.append(0)
		tableIndexes = ['Imię','Nazwisko','Index','E-mail']
		tmp1=0
		for i in xrange(width):
		    if i in tableWidth:
			stdscr.addstr(1, i, "| ",curses.A_BOLD | curses.color_pair(1))
			stdscr.addstr(1, i+2, tableIndexes[tmp1],curses.A_BOLD | curses.color_pair(2))
			tmp1+=1
		    stdscr.addstr(1, 0, "|",curses.A_BOLD | curses.color_pair(1))
		    stdscr.addstr(1, width-1, "|",curses.A_BOLD | curses.color_pair(1))
		    stdscr.addstr(0, i, "-",curses.A_BOLD | curses.color_pair(1))
		    stdscr.addstr(2, i, "-",curses.A_BOLD | curses.color_pair(1))

		for j in range(len(usersList)):
		    jj = j
		    tmp2=0
		    for i in xrange(width):
			if i in tableWidth:
			    if tmp2==0:
				tmp3 = usersList[j].name
			    if tmp2==1:
				tmp3 = usersList[j].surname
			    if tmp2==2:
				tmp3 = usersList[j].userID
			    if tmp2==3:
				tmp3 = usersList[j].mail
			    stdscr.addstr(3+jj*2, i, "| ",curses.color_pair(1))
			    stdscr.addstr(3+jj*2, i+2, str(tmp3),curses.color_pair(3))
			    tmp2+=1
			stdscr.addstr(3+jj*2, 0, "|",curses.color_pair(1))
		        stdscr.addstr(3+jj*2, width-1, "|",curses.color_pair(1))
		        stdscr.addstr(4+jj*2, i, "-",curses.color_pair(1))    


		wait=stdscr.getch()	
	    else:
		return 0
	    #showUsers(usersList,stdscr)

wrapper(main)



















