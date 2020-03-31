#!/usr/bin/env python

from datetime import date
from datetime import datetime

## Tarihler şifreleme için gerekeceğinden önemli bir adım.
today = str(date.today())
today2 = (date.today())
daynum = int(today2.strftime("%d"))


## Şifreleme bölümü (İsteğe göre şifreleme yöntemi değiştirilebilir)

crList = []
crDic = {"a": 1 + daynum,"b": 2 + daynum,"c": 3 + daynum,"ç": 4 + daynum,"d": 5 + daynum,"e": 6 + daynum,"f": 7 + daynum,"g": 8 + daynum,"ğ": 9 + daynum,"h": 10 + daynum,"i": 11 + daynum,"ı": 12 + daynum,"j": 13 + daynum,"k": 14 + daynum,"l": 15 + daynum,"m": 16 + daynum,"n": 17 + daynum,"o": 18 + daynum,"ö": 19 + daynum,"p": 20 + daynum, "r": 21 + daynum, "s": 22 + daynum, "ş": 23 + daynum, "t": 24 + daynum, "u": 25 + daynum, "ü": 26 + daynum, "v": 27 + daynum, "y": 28 + daynum, "z": 29 + daynum, ".": 30 + daynum, ",": 31 + daynum, " ": 0 + daynum} 

## Logo
logo_ascii = """

    _____                                                          
 .-~     ~.  |``````.  |       .'.       |`````````, ``..     ..'' 
:            |       | |     .''```.     |'''|'''''      ``.''     
:     _____  |       | |   .'       `.   |    `.           |       
 `-._____.'| |......'  | .'           `. |      `.         |       
                                                                                                     
"""
print(logo_ascii)

def print_menu():

	print(30 * "-" , "MENU" , 30 * "-")
	print("1. Create a diary entry")
	print("2. Append a diary entry")
	print("3. Read a diary entry")
	print("4. Add cryption to an entry")
	print("5. Exit")
	print(67 * "-")

loop = True


while loop:  ## Boolean değerimiz false olana kadar devam edecek.
    print_menu()
    choice = str(input("Enter your choice [1-5]: "))
     
    if choice == "1":     
        print("Creating a new diary entry:")
        diary = open("gunluk-" + today + ".md","w")
        d_text = input("")
        diary.write(d_text)
        print("Diary with the date " + today + " has been written into the folder.")
        loop=False
    
    elif choice == "2":
        print("Appending an existing entry:")
        diary = open("gunluk-" + today + ".md","a")
        loop=False
        dl_added_text = input("")
        diary.write(dl_added_text)
        print("Diary with the date " + today + " has been overwritten.")

    elif choice == "3":
        print("You decided to read a diary entry.")
        try:
            diary = open("gunluk-" + today + ".md","r")
            print(diary.read())
        except FileNotFoundError:
            print("The file you are looking for is not here.")
        loop=False
    elif choice == "4":
        diary_ready = open("gunluk-" + today + ".md","r")
        encryption_q = str(input("Do you want to cipher this entry? (Y/n): "))
        if encryption_q == "y":
            stb_ced_diary = open("gunluk-" + today + ".md","r+")
            crp = str(stb_ced_diary.read())
            crList = list(crp)
            print(crList)

            for x in crList:
                crList[crList.index(x)] = crDic[x]
            print(crList)
            diary = open("gunluk-" + today + ".md","+w")
            for number in crList:
                #diary.write(str(number)) ## Seperator write'la kullanılamadığı için şimdilik listeyi printle dosyaya yazacak.
                print(str(crList), file=open("gunluk-" + today + ".md", "w"), sep=",")
            print("Diary with the date " + today + " has been overwritten with encryption.")
        else:
            print("You've chosen not to cipher this entry.")
        loop=False
    elif choice == "5":
        print("You've decided to exit the program. Ba-bye.")
        loop=False # Boolean değerimizi false olarak değiştirecek.
    else:
        # 1-5 sayı değeri arasında bir değer girilmezse, hata mesajı verecek
        input("No valid option is selected. Press enter to try again.")
