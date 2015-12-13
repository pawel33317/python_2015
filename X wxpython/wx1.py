# -*- coding: cp1250 -*-
import locale, time
import urllib2,io
import wx
import locale
import wx.lib.mixins.listctrl as listmix
locale.setlocale(locale.LC_ALL, '')


class User:
    def __init__(self, name=None, surname=None, userID=None, mail=None):
        self.name = name
        self.surname=surname
        self.userID=userID
        self.mail=mail


        
class HandleUser: 
    def readFromFile(self,fileName):
        f = io.open(fileName, encoding="utf8")
        lineList = f.read().split("\n")
        f.close()
        return lineList
    def splitLinesIntoUsersObjectsList(self,lineList):
        if hasattr(self, 'usersList'):
            pass
        else:
            self.usersList = []
            
        for i in range(len(lineList)):
            splitedUserLine = lineList[i].strip().rstrip().split(' ')
            if(len(splitedUserLine) == 4):
                nowy = User(splitedUserLine[0].strip().rstrip(), splitedUserLine[1].strip().rstrip(), splitedUserLine[2].strip().rstrip(),splitedUserLine[3].strip().rstrip())
            else:
                nowy = User(splitedUserLine[0].strip().rstrip(), splitedUserLine[1].strip().rstrip(), None, None)
            self.usersList.append(nowy)
    def readFromNet(self):
        onlineUsers = urllib2.urlopen('http://mmajchr.kis.p.lodz.pl/pwjs/zadania/lista.txt').read().strip()
        onlineUsers = onlineUsers.split('\n')
        onlineUsers = [line[line.index(' ')+1:].replace(', ',' ') for line in onlineUsers]
        self.splitLinesIntoUsersObjectsList(onlineUsers)
    def sortName(self):
        self.usersList.sort(key=lambda x: locale.strxfrm(x.name.encode('utf8')))
    def sortSurname(self):
        self.usersList.sort(key=lambda x: locale.strxfrm(x.surname.encode('utf8')))
    def saveToFile(self):
        f = io.open('db2.txt',mode='w',encoding="utf8")
        fileBuffer = []
        for user in self.usersList:
            uid = '' if user.userID == None else ' '+user.userID
            umail= '' if user.mail == None else ' '+user.mail
            fileBuffer.append(user.name+' '+user.surname+uid+umail)
        f.write('\n'.join(fileBuffer))
        f.close()



class MyFrame(wx.Frame):
    def __init__(self, parent, title):
        super(MyFrame, self).__init__(parent, title=title, size=(655, 555))
        
        self.b9 = wx.Button(self, 9, 'Załaduj plik', (10, 400),(200, -1))
        self.b1 = wx.Button(self, 1, 'Sortowanie po imionach',(220, 400),(200, -1))
        self.b2 = wx.Button(self, 2, 'Sortowanie po nazwiskach',(430, 400),(200, -1))
        
        self.b3 = wx.Button(self, 3, 'Dodanie użytkownika', (10, 440),(200, -1))
        self.b4 = wx.Button(self, 4, 'Zapisz do pliku', (220, 440),(200, -1))
        self.b5 = wx.Button(self, 5, 'Pobierz z internetu', (430, 440),(200, -1))
        
        self.b7 = wx.Button(self, 7, 'Usunięcie użytkownika',(10, 480),(200, -1))
        self.b8 = wx.Button(self, 8, 'Edycja użytkownika',(220, 480),(200, -1))
        self.b6 = wx.Button(self, 6, 'Wyjdź',(430, 480),(200, -1))

        sizer = wx.BoxSizer(wx.VERTICAL)
        panel = wx.Panel(self, -1, size=(650,390), style=wx.BORDER_RAISED)
        sizer.Add(panel)
        self.list_ctrl = wx.ListCtrl(panel, size=(632,384),style=wx.LC_REPORT|wx.BORDER_SUNKEN)
        self.list_ctrl.InsertColumn(0, 'ID', width=30)
        self.list_ctrl.InsertColumn(1, 'Imię', width=150)
        self.list_ctrl.InsertColumn(2, 'Nazwisko', width=150)
        self.list_ctrl.InsertColumn(3, 'Numer', width=145)
        self.list_ctrl.InsertColumn(4, 'E-mail', width=150)

        self.Bind(wx.EVT_LIST_ITEM_SELECTED, self.OnClick, self.list_ctrl)
        
        self.b1.Bind(wx.EVT_BUTTON, self.nameSort,id=1)
        self.b2.Bind(wx.EVT_BUTTON, self.surnameSort,id=2)
        self.b3.Bind(wx.EVT_BUTTON, self.userAdd,id=3)
        self.b4.Bind(wx.EVT_BUTTON, self.saveFile,id=4)
        self.b5.Bind(wx.EVT_BUTTON, self.fetchFromNet,id=5)
        self.b6.Bind(wx.EVT_BUTTON, self.bye,id=6)
        self.b7.Bind(wx.EVT_BUTTON, self.removeUser,id=7)
        self.b8.Bind(wx.EVT_BUTTON, self.editUser,id=8)
        self.b9.Bind(wx.EVT_BUTTON, self.loadFile,id=9)
        
        self.Show()
    def fillList(self):     
        self.index = 0
        self.list_ctrl.DeleteAllItems()
        for i, user in enumerate(self.uHandler.usersList):
            uid = ' ' if user.userID == None else user.userID
            umail= ' ' if user.mail == None else user.mail
            self.list_ctrl.InsertStringItem(self.index, str(self.index+1))
            self.list_ctrl.SetStringItem(self.index, 1, user.name)
            self.list_ctrl.SetStringItem(self.index, 2, user.surname)
            self.list_ctrl.SetStringItem(self.index, 3, uid)
            self.list_ctrl.SetStringItem(self.index, 4, umail)
            self.index += 1
    def OnClick(self, event):
        print event.GetText()
    def userAdd(self):
        pass
    def saveFile(self,event):
        self.uHandler.saveToFile()
    def fetchFromNet(self,event):
        self.uHandler.readFromNet()
        self.fillList()
    def removeUser(self):
        pass
    def editUser(self):
        pass
    def nameSort(self, event):
        self.uHandler.sortName()
        self.fillList()
    def surnameSort(self, event):
        self.uHandler.sortSurname()
        self.fillList()
        #self.SetTitle("frame title")#self.SetTitle(self.listBox1.GetStringSelection())
    def bye(self, event):
        self.Close()
    def loadFile(self,event):
        self.uHandler = HandleUser()
        tmp = self.uHandler.readFromFile('db.txt')
        print tmp
        self.uHandler.splitLinesIntoUsersObjectsList(tmp)
        self.fillList()
        
if __name__ == '__main__':
    app = wx.App()
    MyFrame(None, title='Baza użytkowników')
    app.MainLoop()

#wrapper(main)















