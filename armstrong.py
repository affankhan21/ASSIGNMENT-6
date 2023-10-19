def armstrong(num,count,sum1,temp):
    if(num==0):
        if(temp==sum1):
            print(temp,"is armstrong")
        else:
               print(temp,"is not  armstrong")

        return 
    else:
      
        return armstrong(num//10,count,sum1+(pow(num%10,count)),temp)




num=int(input("ENTER NUMBER TO CHECK IF ARMSTRONG OR NOT:"))
temp=num
count=0
while(temp!=0):
    temp=temp//10
    count+=1
print("COUNT =",count)    
temp=num
sum1=0
armstrong(num,count,sum1,temp)
