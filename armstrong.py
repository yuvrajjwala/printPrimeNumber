num= int(input("Enter any numbe: "))
nn=num
s=0
r=0
while(nn!=0):
   r=nn%10
   s=s+(r*r*r)
   nn=nn//10
if(s==num):
    print(num," is an armstrong number")
else:
    print(num," is not an armstrong number ")
