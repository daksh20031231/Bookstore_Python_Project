import pandas as pd
import matplotlib.pyplot as plt
import os
from time import sleep
import datetime

_ = os.system('cls')
print("----------------------------------------------")
print("----------------------------------------------")
print("         WELCOME TO XYZ BOOK STORE")
print("----------------------------------------------")
print("----------------------------------------------")
print("Please wait loading in prgress")
sleep(2)


def allbooks():
    bdf = pd.read_csv('Book.csv')
    print(bdf.to_string())


def chemistry():
    bdf = pd.read_csv('Book.csv')
    chem = (bdf.loc[[0, 1, 2, 10]])
    print(chem.to_string())


def physics():
    bdf = pd.read_csv('Book.csv')
    chem = (bdf.loc[[3, 4, 5]])
    print(chem.to_string())


def maths():
    bdf = pd.read_csv('Book.csv')
    chem = (bdf.loc[[6, 7, 8, 9]])
    print(chem.to_string())


def ip():
    bdf = pd.read_csv('Book.csv')
    chem = (bdf.loc[[11, 12, 13, 14]])
    print(chem.to_string())


def novel():
    bdf = pd.read_csv('Book.csv')
    chem = (bdf.loc[[15, 16, 17, 18]])
    print(chem.to_string())
def bidc():
    idfb = int(input("PLEASE ENTER BOOK ID = "))
    bdf = pd.read_csv('Book.csv')
    df = bdf.loc[bdf["BOOK ID"] == idfb]
    if df.empty:
        print("INVALID BOOK ID")
        print("please enter again")
        sleep(1)
        bidc()
    else:
        index = bdf.index
        condition = bdf["BOOK ID"] == idfb
        rowIndex = index[condition]

        quan = int(input("PLEASE ENTER BOOK QUANTITY = "))
        _ = os.system('cls')
        inp = input("Customer Name: ")
        mob = int(input("MOBILE NO: "))
        _ = os.system('cls')
        print("PLS WAIT WHILE THE MACHINE GENERATING THE INVOICE")
        sleep(2)
        _ = os.system('cls')
        print("--------------------------------------------------------------")
        print("--------------------------------------------------------------")
        print("                    XYZ BOOKSTORE INVOICE")
        print("--------------------------------------------------------------")
        print("--------------------------------------------------------------")

        x = datetime.datetime.now()
        print("NAME :",inp, "                             ", x.strftime("%x"))
        print("MOBILE NO:",mob)
        print("_______________________________________________________________")
        print("BOOK-ID    BOOKNAME             QTY      Unit-Price     TOTAL")
        print(idfb, " ", bdf.loc[rowIndex[0]][1], "      ", quan, "       ", bdf.loc[rowIndex[0]][5], "         ",
              bdf.loc[rowIndex[0]][5] * quan)
        sleep(10)


"""      FINAL     """

status = True
while status:
    _ = os.system('cls')

    print("Press 1 - To see all Books")
    print("Press 2 - To see  Chemistry Books")
    print("Press 3 - To see  Physics Books")
    print("Press 4 - To see  Maths Books")
    print("Press 5 - To see  IP Books")
    print("Press 6 - To see  Novel Books")
    print("Press 7 - Exit")
    print("----------------------------------------------")
    choice = int(input("ENTER YOUR CHOICE: "))
    print("----------------------------------------------")
    _ = os.system('cls')
    if choice == 1:
        allbooks()

    elif choice == 2:
        chemistry()

    elif choice == 3:
        physics()

    elif choice == 4:
        maths()

    elif choice == 5:
        ip()

    elif choice == 6:
        novel()
    elif choice == 7:
        status = False

    else:
        print("INVALID OPTION SELECTED")

    if choice >= 1 and choice <= 6:
        print("----------------------------------------------")
        print("----------------------------------------------")
        print("DO U WANT TO PURCHASE ANY BOOK?")
        print("PRESS 1 - YES")
        print("PRESS 2 - NO")
        print("----------------------------------------------")
        ans = int(input("ENTER YOUR CHOICE: "))
        print("----------------------------------------------")

        if ans == 1:
            bidc()
        elif ans == 2:
            print("THANK U FOR VISTING OUR BOOKSTORE")
        else:
            print("INVALID CHOICE")
    sleep(1)
