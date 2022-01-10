import json
import os
dic={}
dic1={}
userdetail=[]
choose=int(input("....if you want to login for 1/singup for 2...."))
username=input("....enter user name....")
if choose==1:
    password1=input("....enter your password....")
    if len(password1)>=6:
        upper,digit,lower,sepcial=0,0,0,0
        for i in password1:
            if (i.isupper()):
                upper+=1
            if (i.isdigit()): 
                digit+=1 
            if (i.islower()):  
                lower+=1
            if(i=='@'or i=='$' or i=='_' or i=='#' or i=="!" or i=="%" or i=="^" or i=="&" or i=="*" or i=="(" or i==")"):
                sepcial+=1
                total=upper+digit+lower+sepcial
            if upper>=1 and digit>=1 and lower>=1 and sepcial>=1:
                pss="strong password "
        print(pss)
    password2=input("....enter your confirm password....") 
    if password1==password2:
        print("....singup....")
        print("....Both possword should be same....")
    elif password1!=password2:
        print("....Both password are not same....") 
    elif password1!=4: 
        print("....your password is weeak....")                  
    hobby=input("....enter your hobby....")
    dob=input("....enter your date of birth....")
    gender=input("....enter your gender....") 
    # userdetail.append(username)
    # userdetail.append(password1) 
    dic["username"]=username
    dic["password"]=password1
    dic["dob"]=dob
    dic["gender"]=gender  
    dic["hobby"]=hobby
    # dic1["user"]=userdetail
    dic1["profile"]=dic 
    with open("userdetails.json","a+") as f:
        f.write(json.dumps(dic1,indent=4))
        f.close() 
    print("congrats",username,"you are singed up succesfully") 
if choose==2:
        user1=input("....enter user name....")
        password3=input("....enter your password for log in ....")
        with open("userdetails.json","r") as f:
            main1=json.load(f)
            if main1==user1 and main1==password3:
                print("....congratse you scccessfully login....")






        

