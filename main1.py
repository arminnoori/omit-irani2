# pj avl
# tozih kol proj 
# byad tedadi khargosh v tdadi sang v havij ra dar jadval 10 da 10 bgozarim be tori ke be jay yek
# digar nkhoran.vakolshon namaysh dade besh
#start
import numpy as np
import random
# 2 skht arye 101 tayy behter ziba namysh dadn 101 shod
# a=[' ' for x in range(101)] 
a=np.arange(101)
a=[' ' for x in range(101)]
#halgh sakht s,c,R
for i in range(11):
            r2=random.randint(1,100)
            while a[r2]!=' ':
                r2=random.randint(1,100)
            a[r2]="s"
            while a[r2]!=' ':
                r2=random.randint(1,100)
            a[r2]="c"
#sakh khargosh 
# harf N do khar gosh shbihm dar yke  khane bodn nabod shodn
            randR=random.randint(1,3)
            if randR==1:
                rabit="Rm"
            elif randR==2:
                rabit="Rf"
            elif randR==3:
                rabit="R"
            r2=random.randint(1,100)
            while a[r2]=="s" or a[r2]=="c":
                 r2=random.randint(1,100)

            if a[r2]==" ":
                a[r2]=rabit
            elif a[r2]=="Rm" or a[r2]=="Rf":
                if a[r2]==rabit:
                    a[r2]="N"
                elif a[r2]!=rabit:
                    a[r2]="Rb"
            elif a[r2]=="Rb":
                continue
            elif a[r2]=="R":
                continue
        
           
#nmaysh jadval
ss=""
for s in range(1,101):
            if s%10==0:
                ss+="\t"+a[s]
                ss+="\n"
            else: 
                ss+="\t"+a[s]
print(ss)
#khoroji table
try:
    with open("test.bat","w") as f:
                f.write(ss)
                f.close()
except TypError:
    print("There was a type error!")

























# #1.2 frstadn arrye a be class pro
# d=pro(a)
# #1.3 farkhani method mohasbe 
# d.mohasbe()
###############################################################hazf shode
#2 sakht class pro1 
# class pro1():         
# #2.1 grftn vrodi 
#     def __init__(self,lis):
#         self.lis=lis
# #2.2 sakht method show
#     def show(self):
# #2.3 sakht skht string bary rekhtan arrye vorodi braye namayesh
#         ss=""
# #2.4 sakht halgh bar mortb rikhtn arrey be string
#         for s in range(1,101):
# #2.5 bary in ke 10 dar 10 besh age halge be s%10==0 rsid ber khat bad ba ezaf kardn \n
#             if s%10==0:
#                 ss+="\t"+self.lis[s]
#                 ss+="\n"
# #2.6 dar gher in sorat ba \t ezafe kone 
#             else: 
#                 ss+="\t"+self.lis[s]
# #2.7 dar akharm nmaysh
#         print(ss)
# #2.8sakht method save file 
#         with open("test.bat","w") as f:
#                 f.write(ss)
# # 3 sakht class pro
# class pro(pro1):
# # 4 da ebtada vrodi haro moshkas mikonim
#     def __init__(self,a):
#         self.a=a    
# # 5 method jaygozari khargosh va sang va havig ro misazim
#     def mohasbe(self):          

      
# #16 bro barye nmaysh class pro1 seda kon
#         n=pro1(self.a)
# #17 az method show barye namysh estfade kon
#         print(n.show())       
###############################################################hazf shode



#end
