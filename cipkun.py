from datetime import date

## Tarihler şifreleme için gerekeceğinden önemli bir adım.
today = str(date.today())


## Şifreleme bölümü (İsteğe göre şifreleme yöntemi değiştirilebilir)

alf = {"a" = 1, "b" = 2, "c" = 3, "d" = 4}

def print_menu():
    print(30 * "-" , "DIARY MENU" , 30 * "-")
    print("1. Create a diary entry")
    print("2. Append a diary entry")
    print("3. Read a diary entry")
    print("4. Add cryption to an entry")
    print("5. Exit")
    print(67 * "-")

loop = True


while loop:  ## Boolean değerimiz false olana kadar devam edecek.
    print_menu()
    choice = str(input("Enter your choice [1-4]: "))
     
    if choice == "1":     
        print("Creating a new diary entry:")
        diary = open("gunluk-" + today + ".md","w+")
        loop=False
        d_text = input("")
        diary.write(d_text)
        print("Diary with the date " + today + " has been written into the folder.")
        loop=True
    
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
        print(diary_ready)
        encryption_q = str(input("Do you want to cipher this entry? (Y / n) :"))
        if encryption_q == "Y"
            with open("gunluk-" + today + ".md","r+") as f:
                old = f.read()
                f.seek(0)
                f.write()
        else
            print("You've chosen not to cipher this entry.")
    elif choice == "5":
        print("You've decided to exit the program. Ba-bye.")
        loop=False # Boolean değerimizi false olarak değiştirecek.
    else:
        # 1-5 sayı değeri arasında bir değer girilmezse, hata mesajı verecek
        input("No valid option is selected. Press enter to try again.")
