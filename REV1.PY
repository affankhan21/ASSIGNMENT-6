# Write Python Program to Reverse Number Using Recursion
result = 0
def rev_number(n):
    global result
    if n > 0:
        result = (result * 10) + (n % 10)
        rev_number(n // 10)
    return result
    
n = int(input(" ENTER NUMBER :"))
ans = rev_number(n)
print(f'Reverse of {n} = {ans}')