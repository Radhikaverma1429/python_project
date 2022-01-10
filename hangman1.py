import random
def hangman():
    list_of_word=["shushree","shivani","computer","supriti"]
    word=random.choice(list_of_word)
    turn=10
    gussesmade=" "
    valid_entry=("abcdefghijklmnopqrstvwxyz")
    while len(word)>0:
        main_word=" "
        for letter in word:
            if letter in word:
                main_word=main_word+letter
            else:
                main_word+="_ "
        if main_word==word:
            print(main_word)
            print("you win!!!")
            break
        print("guess the words ",main_word) 
        guess=input()
        if guess in valid_entry:
            gussesmade=gussesmade+guess
        else:
            print("enter valid character ")
        if guess not in word:
            turn=turn-1
            if turn==9:
                print("9 turn lest!!!")
                print("--------------")
            if turn==8:
                print("8 turn lest!!!")
                print("--------------")
                print("      o       ")
            if turn==7:
                print("7 turn lest!!!")
                print("--------------")
                print("      o       ")
                print("      |       ")
            if turn==6:
                print("6 turn lest!!!")
                print("--------------")
                print("      o       ")
                print("      |       ")
                print("     /        ")
            if turn==5:
                print("5 turn lest!!!")
                print("--------------")
                print("      o       ")
                print("      |       ")
                print("     / \      ")
            if turn==4:
                print("4 turn lest!!!")
                print("--------------")
                print("     \o       ")
                print("      |       ")
                print("     / \      ")
            if turn==3:
                print("3 turn lest!!!")
                print("--------------")
                print("     \o/      ")
                print("      |       ")
                print("     / \      ")      
            if turn==2:
                print("2 turn lest!!!")
                print("--------------")
                print("     \o/  |   ")
                print("      |       ")
                print("     /|\      ")    
            if turn==1:
                print("1 turn lest!!!")
                print("--------------")
                print("     \o/__|   ")
                print("      |       ")
                print("     /|\      ")    
            if turn==0:
                print("you loose")
                print("you let a good man die")
name=input("enter your name :-")
print("Welcome",name,"!")
print("-------------------")
print("try gusees the word in less than 10 attempts ")
hangman()





