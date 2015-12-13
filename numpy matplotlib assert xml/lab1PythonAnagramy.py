

if __name__ == '__main__':
    slownik = open('slowa-win.txt', 'rb')
    
    anagram = "szalik"
    sortAnagram = sorted(anagram)
    for line in slownik.readlines():
        wyraz = ''.join(line)
        if sorted(wyraz.strip().rstrip()) == sortAnagram:
            print line.strip().rstrip()

    
    # print(slownik.read())
    
    
    
