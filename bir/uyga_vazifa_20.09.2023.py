import os
os.system("cls")


#************************* 1 - Problem ********************

class kitob:
    def __init__(self,nomi,mualif,narxi,nashriyoti):
        self.kitob_nomi=None
        self.kitob_muallifi=None
        self.kitob_narxi=None
        self.kitob_nasriyoti=None

    def chiqar(k):
        print("{:10s} {:-10s} {:-10d} {:10s}".format(k.kitob_nomi,k.kitob_muallifi,k.kitob_narxi,k.kitob_nasriyoti))


n=int(input("Nechta kitob kiritasiz : "))
Kitoblar=list()
for i in range(1,n+1):
    nomi=input(f"{i} kitobni nomini kiritng  : ")
    mualif = input(f"{i} kitobni mualifini kiritng  : ")
    narxi = int(input(f"{i} kitobni narxini kiritng  : "))
    nashriyoti=input(f"{i} kitobni nashriyotini kiritng  : ")
    book=kitob(nomi,mualif,narxi,nashriyoti)
    Kitoblar.append(book)

for j in Kitoblar:
   j.chiqar()


