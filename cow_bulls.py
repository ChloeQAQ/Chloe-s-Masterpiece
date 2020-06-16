import random
num1=random.randint(1,9)
num2=random.randint(1,9)
num3=random.randint(1,9)
num4=random.randint(1,9)
numlist=[num1,num2,num3,num4]

print("Welcome to Cows and Bulls")



GNum=input("Guess what the four numbers are:")

GList=[]
for i in range(4):
    GList.append(int(GNum[i]))


end=0

enter=input("print H to start")
    
if enter=="H" :
    while end != 1:
        if GList == numlist:
            end=1
            print("Your answer is correct.the number is ",GNum)
            break
        cows=0
        for i in range(4):
            
            if GList[i] == numlist[i]:
               cows=cows+1
        print("There are",cows,"cows")
        bulls=0
        for i in range(4):
            for j in range(4):
                if GList[i] == numlist[j] and GList[i] != numlist[i]:
                    bulls=bulls+1
        
        print("There are ",bulls,"bulls")
    
        enter=input("print H to try it again")
        
        GNum=input("Guess what the four numbers are:")
        GList=[]
        for i in range(4):
                GList.append(int(GNum[i]))


 

