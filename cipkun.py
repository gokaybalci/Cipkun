from datetime import date

## Tarihler şifreleme için gerekeceğinden önemli bir adım.
today = str(date.today())


def print_menu():
    print(30 * "-" , "DIARY MENU" , 30 * "-")
    print("1. Create a diary entry")
    print("2. Append a diary entry")
    print("3. Read a diary entry")
    print("4. Exit")
    print(67 * "-")

loop = True


while loop:          ## Boolean değerimiz false olana kadar devam edecek.
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
        print("You decided to read a diary entry. Here it is: ")
        diary = open("gunluk-" + today + ".md","r")
        loop=False
        print(diary.read())

    elif choice == "4":
        print("You've decided to exit the program. Ba-bye.")
        loop=False # Boolean değerimizi false olarak değiştirecek.
    else:
        # 1-4 sayı değeri arasında bir değer girilmezse, hata mesajı verecek
        input("No valid option is selected. Press enter to try again.")

	




