import ezgmail
import time

print("Kies ontvanger:")
ont = input()
print("Onderwerp?")
ond = input()
print("Text:")
text = input()
print("CC?")
CX = input()


def stuur():
    ezgmail.send(ont, ond, text,cc=CX)
    #print ("SPam")
    time.sleep(30)


def een():
 print ("Een keer")
 stuur()


def vijf():
    print ("Vijf keer")
    for X in range(0,5):
     stuur()


def tien():
    print ("Tien keer")
    for X in range(0,10):
     stuur()

def keuzes():
 K = 0
 while K != 1 and K != 5 and K!= 10 :
  K = int (input("Hoeveel keer? Kies 1-5-10!!"))
 if K == 1:
     een()
 elif K == 5:
     vijf()
 elif K == 10:
     tien()
 else:
   print("Kies 1-5-10!!")


keuzes()
