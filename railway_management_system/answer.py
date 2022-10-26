import random
from urllib.parse import uses_relative
n = int(input("ENTER NO. OF SEATS THAT SHOULD BE THERE IN TRAIN     :    "))
data = []
choices = ["c","a","r"]
for x in range(n):
    t = random.choice(choices)
    data.append(t)
ctr = 0
chk = True
while chk:
    ctr=0
    avs = []
    flag = True
    print("SEATS Available are")
    for x in data:
        ctr+=1
        
        if(x=="a" or x=="c"):
            flag=False
            print(ctr , end='  ')
            avs.append(int(ctr))
    if(flag==True):
        print("We don't have any seats  :(")
        break
    else :
        # print(avs)
        user = int(input("Out of Available seats which seat you want to buy    :  "))
        if user in avs:

            for x in avs:
                if user==x:
                    data[x-1]="r"
                    avs.remove(user)
                    ans = input("Do you want to buy another seat type (Y/N)     :   ")
                    if(ans=='Y'):
                        break
                    else :
                        chk=False
                        break
        else :
            print("Enter a valid input")
print()
print("Total Statistics of data after reservation")
ctr=0
for x in data:
    ctr+=1
    if(x=='c' or x=='a'):

        print("Seat No. ",ctr," : ","Available")
    else :
        print("Seat No. ",ctr," : ","Reserved")
