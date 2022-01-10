import random
print("Welcome to cows bulls game!!!")
list1=[0,1,2,3,4,5,6,7,8,9]
list2=random.sample(list1,5)
print(list2)
user=input("enter plyer name!!")
print('welcome',user)
def cows_bulls():
    i=0 
    while i<len(list2):
        j=0
        list3=[] 
        list4=[]
        while j<5:
            sec=int(input("enter a secret number!! "))
            possition=int(input("enter the position!! "))
            if list2[possition]==sec:
                if sec not in list3:
                    list3.append(sec)
                    print(list3)
                    print("....bull....")
                else:
                    print("....Already taken....")
            elif list2[possition]!=sec:
                list4.append(sec)  
                print(list4)  
                print("....cow....")
            else:
                print("....not existis....")   
            j+=1
        i+=1
cows_bulls()



    
