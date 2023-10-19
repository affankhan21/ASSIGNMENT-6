#PROGRAM TO REVERSE A NUMBER USING RECURSION
def revnum(num,rev):

  if(num==0):
        return rev
  else:
     return revnum(num//10,rev*10+num%10)

a=int(input("ENTER NUMBER TO REVERSE:"))
rev=0
revnum(a,rev)
print(revnum(a,rev))
