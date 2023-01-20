from time import *
from datetime import *

def horloge():
    while True:
        print(str(datetime.now())[11:19])
        sleep(1)
horloge()

def afficher_heure(H, M, S):
    liste = [0,1,2,3,4,5,6,7,8,9]
    while True:
        S = S+1
        if S == 60:
            M = M+1
            S = 0
        if M == 60:
            H = H+1
            M = 0
            S = 0
        if H == 24:
            H = 0
        if H in liste or M in liste or S in liste:
            h = str(H)
            m = str(M)
            s = str(S)
            if H in liste:
                h = "0"+h
            if M in liste:
                m = "0"+m
            if S in liste:
                s = "0"+s
            print(h+":"+m+":"+s)
        else:
            print(str(H)+":"+str(M)+":"+str(S)) 
        sleep(1)
afficher_heure(7, 35, 3)

def alarme(h, m, s):
    while True:
        print(str(datetime.now())[11:19])
        sleep(1)
        if int(str(datetime.now())[11:13]) == h and int(str(datetime.now())[14:16]) == m and int(str(datetime.now())[17:19]) == s:
            print("C'est l'heure")
alarme(14, 53, 00)
