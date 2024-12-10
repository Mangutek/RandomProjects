import numpy as np
tekst = open("gra.txt.txt").readlines()
data = []
for line in tekst:
    data.append([])
for y in range(len(tekst)):
    for x in range(len(tekst[0])-1):
        data[y].append(tekst[y][x])
def copymatrix(new, old):
    for z in range(len(old)):
        new.append([])
    for y in range(len(old)):
        for x in range(len(old[y])):
             new[y].append(old[y][x])
def game_of_life(dane):
    tab = []
    tab.clear()
    copymatrix(tab, dane)
    for y in range(len(dane)):
        for x in range(len(dane[y])):
            ile = 0
            try:
                if dane[y-1][x-1] == 'X': ile=ile+1
            except:
                print('NIE')
            try:
                if dane[y-1][x] == 'X': ile=ile+1
            except:
                print('NIE')
            try:
                if dane[y-1][x+1] == 'X': ile=ile+1
            except:
                print('NIE')
            try:
                if dane[y][x-1] == 'X': ile=ile+1
            except:
                print('NIE')
            try:
                if dane[y][x+1] == 'X': ile=ile+1
            except:
                print('NIE')
            try:
                if dane[y+1][x-1] == 'X': ile=ile+1
            except:
                print('NIE')
            try:
                if dane[y+1][x] == 'X': ile=ile+1
            except:
                print('NIE')
            try:
                if dane[y+1][x+1] == 'X': ile=ile+1
            except:
                print('NIE')
            if dane[y][x] == 'X' and (ile == 2 or ile == 3):
                tab[y][x] = 'X'
            elif dane[y][x] == '.' and ile == 3:
                tab[y][x] = 'X'
            else:
                tab[y][x] = '.'
            
            print(np.matrix(tab))
    return tab

    
            
print(np.matrix(game_of_life(data)))
        
