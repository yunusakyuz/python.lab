sudoku cuzumleri 
1)

ns=“”
y = 0
for n in sudoku:
    x=0
    if y == 0 or y == 4 or y== 8:
        ns += 21*“-”+ “\n”
        y = y + 1
    while x<3:
        ns += str(n[x]) + ” ”
        x += 1
    ns += “|”+” ”
    while x < 6:
        ns += str(n[x]) + ” ”
        x += 1
    ns += “|”+” ”
    while x < 9:
        ns += str(n[x]) + ” ”
        x += 1
    ns += “\n”
    ns +=“”
    y = y + 1
ns += 21*“-”+ “\n”
print(ns)

2)

sudoku = [
    [0, 0, 0, 0, 6, 4, 0, 0, 0],
    [7, 0, 0, 0, 0, 0, 3, 9, 0],
    [8, 0, 0, 0, 0, 0, 0, 0, 0],
    [0, 0, 0, 5, 0, 2, 0, 6, 0],
    [0, 8, 0, 4, 0, 0, 0, 0, 0],
    [3, 5, 0, 6, 0, 0, 0, 7, 0],
    [0, 0, 2, 0, 0, 0, 1, 0, 3],
    [0, 0, 1, 0, 5, 9, 0, 0, 0],
    [0, 0, 0, 0, 0, 0, 7, 0, 0]
]
def display(x) :
    for i in range(len(x)+4) :
        if i % 4 == 0 :
            x.insert(i, [(("-")*21)])
    for j in range(13) :
        if j % 4 != 0 :
            x[j].insert(3, "|")
            x[j].insert(7, "|")
    for ii in x :
        if len(ii) == 1 :
            print(ii[0])
        elif len(ii) == 11 :
            for iii in range(11):
                print(ii[iii] , end = " ")
            print("")
display(sudoku)

E2158 - Serdar  2 minutes ago
try:
    sudoku = [
        [0, 0, 0, 0, 6, 4, 0, 0, 0],
        [7, 0, 0, 0, 0, 0, 3, 9, 0],
        [8, 0, 0, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 5, 0, 2, 0, 6, 0],
        [0, 8, 0, 4, 0, 0, 0, 0, 0],
        [3, 5, 0, 6, 0, 0, 0, 7, 0],
        [0, 0, 2, 0, 0, 0, 1, 0, 3],
        [0, 0, 1, 0, 5, 9, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 7, 0, 0]
    ]
    for i in sudoku:
        if sudoku.index(i)%3 == 0: print("- "*13)
        count=0
        for j in i:
            count +=1
            [print(j, " | ", end=" ") if count==3 or count==6 else print(j, end=" ")]
        print() 
except:
    print("Du har et problem, dessverre. Kan du sjekke din kode?")
else:
    pass
finally:
    print("- "*13)

E2202 - Emre  2 minutes ago
print(*"-"*11)
for i in range(0,len(sudoku)):
    print( *sudoku[i][0:3], "|", *sudoku[i][3:6], "|", *sudoku[i][6:9] )# for every 9 list in sudoku list, write 3 of value and add "|".
    if (i+1)%3==0:# used for add "-" end of first three list values
        print(*"-"*11)
    else:
        pass

E2457 - Ipek  2 minutes ago
sudoku = [
    [0, 0, 0, 0, 6, 4, 0, 0, 0],
    [7, 0, 0, 0, 0, 0, 3, 9, 0],
    [8, 0, 0, 0, 0, 0, 0, 0, 0],
    [0, 0, 0, 5, 0, 2, 0, 6, 0],
    [0, 8, 0, 4, 0, 0, 0, 0, 0],
    [3, 5, 0, 6, 0, 0, 0, 7, 0],
    [0, 0, 2, 0, 0, 0, 1, 0, 3],
    [0, 0, 1, 0, 5, 9, 0, 0, 0],
    [0, 0, 0, 0, 0, 0, 7, 0, 0]
]
print(* '-------------')
a = 0
while a < len(sudoku) :
    for i in sudoku[a :(a + 3)]:
        print(* i[0:3], ' | ', * i[3:6], ' | ', * i[6:9])
    print(* '-------------')
    a += 3

E2008 - Emre  2 minutes ago
sudoku = [    [0, 0, 0, 0, 6, 4, 0, 0, 0],    [7, 0, 0, 0, 0, 0, 3, 9, 0],    [8, 0, 0, 0, 0, 0, 0, 0, 0],    [0, 0, 0, 5, 0, 2, 0, 6, 0],    [0, 8, 0, 4, 0, 0, 0, 0, 0],    [3, 5, 0, 6, 0, 0, 0, 7, 0],    [0, 0, 2, 0, 0, 0, 1, 0, 3],    [0, 0, 1, 0, 5, 9, 0, 0, 0],    [0, 0, 0, 0, 0, 0, 7, 0, 0]]
for i in range(len(sudoku)):    if i % 3 == 0:        print (*"-"*15)        print((*sudoku[i][:3]), "\b|",*sudoku[i][3:6], "\b|",*sudoku[i][6:], sep = "  ")    else:        print(*sudoku[i][:3], "\b|",*sudoku[i][3:6], "\b|",*sudoku[i][6:], sep = "  ")print (*"-"*15)

E2175 - Mevlüt  2 minutes ago
sudoku = [
    [0, 0, 0, 0, 6, 4, 0, 0, 0],
    [7, 0, 0, 0, 0, 0, 3, 9, 0],
    [8, 0, 0, 0, 0, 0, 0, 0, 0],
    [0, 0, 0, 5, 0, 2, 0, 6, 0],
    [0, 8, 0, 4, 0, 0, 0, 0, 0],
    [3, 5, 0, 6, 0, 0, 0, 7, 0],
    [0, 0, 2, 0, 0, 0, 1, 0, 3],
    [0, 0, 1, 0, 5, 9, 0, 0, 0],
    [0, 0, 0, 0, 0, 0, 7, 0, 0]
]
count = 0
count_2 = 0
print("- " * 15)
for i in sudoku:
    if sudoku[count_2] == i :
        for ii in i:
            count += 1
            print(ii, end="  ")
            if count == 3 :
                print("|", end=" ")
            elif count == 6:
                print("|", end=" ")
        count = 0
    print("")
    count_2 += 1
    if count_2 == 3:
        print("- " * 15)
    elif count_2 == 6:
        print("- " * 15)
    elif count_2 == 9:
        print("- " * 15)

E2060 - Fatih  2 minutes ago
for i in sudoku:
    if sudoku.index(i) % 3 == 0:
        print("\n"+ 11 * "- ")
    else:
        print()
    for x in range(len(i)):
       if x in [2 ,5]:
           print(f"{i[x]} |", end = " ")
       else:
           print(i[x], end = " ")
print("\n"+ 11 * "- ")

E2037 - Can  2 minutes ago
minuses = "- - - - - - - - - - - - - -"
print(minuses)
for x in range(0,9,3):
    for i in range(x, x+3):
        k = [str(k) for k in sudoku[i]]
        print("  ".join(k[0:3]) + " | " + "  ".join(k[3:6]) + " | " + "  ".join(k[6:]))
    print(minuses)

E2465 - Gülin  1 minute ago
for i in range(len(sudoku)+4):
    if i == 0 or i%4==0:
        sudoku.insert(i,("-"*11))
    else:
        sudoku[i].insert(3, "|"), sudoku[i].insert(7, "|")
    print(*sudoku[i])

E2159 - Mehmet  1 minute ago
for i in range(len(sudoku)):
    line = ""
    if i % 3 == 0:
        print("---------------------")
    for j in range(len(sudoku[i])):
        if j == 3 or j == 6:
            line += "| "
        line += str(sudoku[i][j])+" "
    print(line)
print("---------------------")

E2486 - Furkan  1 minute ago
counter = 0
for i in sudoku:
    if not counter % 3:
        print("- - - - - - - - - - - - - - - ")
    counter += 1
    for j in range(len(i)):
        print(i[j], end = "  ")
        if not (j + 1) % 3 and j < len(i)-1:
            print("|", end = " ")
    print("")
print("- - - - - - - - - - - - - - - ")

E2451- Sirius  1 minute ago
sudoku = [x[0:3]+["|"]+x[3:6]+["|"]+x[6:] for x in sudoku]
count=0
for i in sudoku:
    if count%3==0:
        print(21*"-")
    for ii in range(len(sudoku)+2):
        print(i[ii],end=" ")
    print("\r")
    count+=1
print(21*"-")

E2214 - Mirza  1 minute ago
sudoku = [
    [0, 0, 0, 0, 6, 4, 0, 0, 0],
    [7, 0, 0, 0, 0, 0, 3, 9, 0],
    [8, 0, 0, 0, 0, 0, 0, 0, 0],
    [0, 0, 0, 5, 0, 2, 0, 6, 0],
    [0, 8, 0, 4, 0, 0, 0, 0, 0],
    [3, 5, 0, 6, 0, 0, 0, 7, 0],
    [0, 0, 2, 0, 0, 0, 1, 0, 3],
    [0, 0, 1, 0, 5, 9, 0, 0, 0],
    [0, 0, 0, 0, 0, 0, 7, 0, 0]
]
for i in range(len(sudoku)+1):
    print('\n')
    if i % 3 == 0:
        for k in range(len(sudoku)):
            print('-  ', end = ' ')
            if k > 0 and k % 8 == 0:
                print('\n')
    if i == 9:
        break
    else:
        for j in range(len(sudoku[i])):
            print(sudoku[i][j], end = '  ')
            if j is 2 or j is 5:
                print(' | ', end= ' ')

E2004 - Ali Feyzi  1 minute ago
i=0
while i<9:
    if i%3==0:
        print("-"*25)
    print(*sudoku[i][0:3]," | ",*sudoku[i][3:6]," | ", *sudoku[i][6:9])
    i+=1
print("-"*25)

E2103 - Huseyin  < 1 minute ago
a=len(sudoku)
for j in range(a):
    if j %3==0:
        print("- "*15)
    for i in range(a):
        if i in (3,6):
            print("|",end=" ")
        print(sudoku[j][i],end="  ")
    print("")
print("- "*15)


E2316 - Yusuf  < 1 minute ago
counter = 0
print(*(11 * '-')) 
for i in sudoku:
    counter += 1
    print(i[0],i[1],i[2],'|',i[3],i[4],i[5],'|',i[6],i[7],i[8])
    if (counter % 3 == 0):
        print(*(11 * '-'))


E2134-Fazilet  3 minutes ago
print('-'*21)
for i in range(len(b)) :
    if i==3 or i==6:
        print('-'*21)
    for j in range(len(b[i])+2) :
        if j==3 or j==7:
            b[i].insert(j, '|')
        print(b[i][j], end=" ")
    print()
print('-'*21)


