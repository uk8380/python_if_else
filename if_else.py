#if,else,elif,nested
#syntax if(condition):
a=int(input("enter the value"))
print(a)
if(a>=10):
    print("hello love")
#else
else:
    print("vampire diaries")

#-----------------------------------------------------------------------
#elif
b=int(input("enter the value"))
if(b==3):
    print("three")
elif(b==2):
    print("two")
elif(b<=1):
    print("bye love")
else:
    print("poo")
#--------------------------------------------------------------------------
#nested
x=int(input("enter"))
if(x<=10):
    xy=int(input("enter bro"))
    if(xy>=10):
        print("assam")
    else:
        print("sambar")
else:
    print("enter valid value")
