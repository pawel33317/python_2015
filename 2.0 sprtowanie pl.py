# -*- coding: utf-8 -*-
import locale
locale.setlocale(locale.LC_ALL, '')

user = []
dlugoscListy=int(raw_input('Podaj dlugosc Listy:'))
for i in range(dlugoscListy):
    ob=raw_input('Podaj imie i nazwisko:')
    user.append([ob[:ob.index(' ')], ob[ob.index(' '):]])
  
print "1 - sortowanie po imionach"
print "2 - sortowanie po nazwiskach"

wybor=int(raw_input('Wybierz: '))

if wybor == 1:
    user.sort(key=lambda x: locale.strxfrm(x[0]))
else:
    user.sort(key=lambda x: locale.strxfrm(x[1]))
    
for i in range(dlugoscListy):
    print user[i][0] + " " + user[i][1]
