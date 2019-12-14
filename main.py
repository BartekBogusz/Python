

x = 5
y = "Bartek"
y = 6
print("liczba:",x,y)

print(2 ** 8)
a = 3
if a > 3:
    print("a jest większe od 3")
elif a<3:
    print("a jest mniejsze od 3")
else:
    print("a jest równe 3 ")



def znakLiczby(x):
    if x > 0 :
        print("liczba", x, "jest dodatnia")
    elif x < 0:
        print("liczba", x, "jest ujemna")
    else:
        print("licbza", x, "jest równa 0 ")

znakLiczby(55)
znakLiczby(-55)
znakLiczby(0)

def poleKola(r):
    return 3.1415 * r**2.0

print(poleKola(4))
print(poleKola(5))


for i in range(1,10,2):
    print(i)
    print(i)
    print(i)
    print()


for r in range(1,10):
    print(r,poleKola(r))


def monzenie(x):
    for i in range(1,11):
        print(x,"*",i,"=",i*x, end =",")
    print()

monzenie(3)


def tabliczkaMnozenia():
    for i in range(1,11):
        for j in range(1,11):
            print(j * i,"", end = "")
        print()

tabliczkaMnozenia()


#
##
###
#####

def schodki(n):
    for i in range(1,n+1):
        for j in range(1,i+1):
            print("#", end = "")
        print()
schodki(10)


   #
  ###
 #####
#######


def piramidka(n):
    for i in range(1,n+1):
        for j in range(1,n-i+1):
            print(" ", end = "")
        for j in range(1,i*2):
            print("#", end = "")
        print()


piramidka(4)
piramidka(15)


























