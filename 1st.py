#print length a word
a="khushi"
print(len(a))

#prg to check a number is pallindrome or not
num=int(input("enter a number:"))
sum=0
temp=num
while(num>0):
    rem=num%10
    sum=sum*10+rem
    num//=10
if(temp==sum):
    print("pallindrome")
else:
    print("not pallindrome")


#prg to print sum of first and last digit
num=int(input("enter a number:"))
i=0
while(num!=0):
    if(i==0):
        last=num%10
        i=i+1
    rem=num%10
    num=num//10
print("first digit:",rem)
print("last digit:",last)
sum=rem+last
print(sum)

#prg to print only odd position letter from a word
a="khushi"
for i in range(0,len(a)):
    if(i%2!=0):
        print(a[i])