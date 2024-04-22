# -*- coding: utf-8 -*-
"""
Created on Mon Apr 22 18:33:46 2024

@author: lenovo
"""
"""
print(1)
print(2)
print(3)

for i in range(3): # 0 1 2
    print(i+1)
  """
"""
*
**
***
****



"""
"""

print("*")
for i in range(1):
    print("*",end="")
print()
           
print("*")
for i in range(2):
    print("*",end="")
print()   

print("*")
for i in range(3):
    print("*",end="")
print()
 
"""

#Üçgen Yapımı 


for k in range(1, 5, 1):  # 1'den 5'e kadar (dahil değil) olan sayılar için
    for i in range(k):
        print("*", end=" ")
    print()

# Ters Üçgen Yapımı

for k in range (5,0,-1):
    for i in range (k):
        print("*",end=" ")
    print()


 # Taş-Kağıt-Makas Oyunu
import random

def blgsyr_secimi_uret():
    n = random.randint(1, 3)
    if n == 1:
        return "Tas"
    elif n == 2:
        return "Kagıt"
    else:
        return "Makas"
     
skor_kullanici = 0
skor_blgsyr = 0

while True:     
    kullanici_secimi = input("Tas? Kagıt? Makas? (Çıkmak için 'q' basın): ")
    if kullanici_secimi.lower() == 'q':
        break
    blgsyr_secimi = blgsyr_secimi_uret()
  
    print("Bilgisayar: ", blgsyr_secimi)
         
    if(blgsyr_secimi == kullanici_secimi):
        print("Berabere")
    elif blgsyr_secimi == "Tas" and kullanici_secimi == "Kagıt":
        skor_kullanici += 1
        print("Siz Kazandınız")
    elif blgsyr_secimi == "Kagıt" and kullanici_secimi == "Makas":
        skor_kullanici += 1
        print("Siz Kazandınız")
    elif blgsyr_secimi == "Makas" and kullanici_secimi == "Tas":
        skor_kullanici += 1
        print("Siz Kazandınız")
    else:
        skor_blgsyr += 1
        print("Kaybettiniz")
    
print("Siz: ", skor_kullanici, "VS", "Bilgisayar: ", skor_blgsyr)

    
 
 
 