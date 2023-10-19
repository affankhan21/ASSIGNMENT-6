#DO SUM OF SERIES UPTO N NUM USING RECURSIVE FUNCTION
#1+2+3+4+5......N
#function declararion
def fact(n):
    f=1
    if(n==0):
        return 1
    else:
            
        return n*fact(n-1)


def sumseries(num):
    
    #this is a recursive function
    if(num==0):
        return 0
    else:
        return fact(num)+sumseries(num-1)



a=int(input("ENTER THE SUM OF SERIES UPTOWHICH NUMBER :"))
#FUNCTION CALL
b=sumseries(a)
print(b)