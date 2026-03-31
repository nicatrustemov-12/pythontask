"""x= 7.5
y= 9
s= x*y
print(s)"""   #1


"""x=7.5
y=9
z=5
s=x*y*z
print(s)"""   #2


"""x=7.5
y=9
z=5
s=2*(x*y+x*z+y*z)
print(s)"""     #3


"""a=9.5
s=a**3
print(s)"""     #4


"""import math
h=10
r=5
s=math.pi*r**2*h
print(s)"""    #5



"""h=8.5
a=10
s=a*h/2
print(s)"""    #6



"""import math
a=25
b=17
bucaq=30
#radiana cevirek
r=math.radians(bucaq)
s=0.5*a*b*math.sin(r)
print(f"{s: .2f}")"""    #7



"""import math
x1=float(input("x1: "))
x2=float(input("x2: "))
x3=float(input("x3: "))
y1=float(input("y1: "))
y2=float(input("y2: "))
y3=float(input("y3: "))
a=math.sqrt((x1-x2)**2+(y2-y2)**2)
b=math.sqrt((x1-x3)**2+(y2-y3)**2)
c=math.sqrt((x2-x3)**2+(y2-y3)**2)
p=(a+b+c)/2
S=math.sqrt(p*(p-a)*(p-b)*(p-c))
print(f"Sahe = {S: .2f}")"""      #8


"""x=float(input("x:  "))
y=float(input("y:  "))
z=float(input("z:  "))
c=x+y+z
h=x*y*z
e_o=c/3
print(c,h,e_o,sep=",")"""     #9


"""import math
x1=float(input("x1:  "))
y1=float(input("y1:  "))
x2=float(input("x2:  "))
y2=float(input("y2:  "))
AB=math.sqrt((x2-x1)**2+(y2-y1)**2)
print(f"AB parcasinin uzunlugu = {AB: .2f}")"""    #10


"""import random
n = random.randint(1000,9999)
print("eded",n)
a=n//1000
b=(n//100)%10
c=(n//10)%10
d=n%10

#kvadratlari ferqi
ferq=a**2-b**2-c**2-d**2
#reqemlerinin hasili
hasil=a*b*c*d
print(hasil,ferq)"""        #11


"""import random
a = random.uniform(6.5,10.5)
b = random.uniform(6.5,10.5)
h=a*b
print(f"a= {a: .2f}")
print(f"b= {b: .2f}")
print(f"hasil = {h: .2f}")"""        #12


"""import random
n = random.randint(10000,99999)
print("eded:",n)
for r in str(n):
    r= int(r)
    print(r,   r*r)"""      #13



"""import math
import random
x=random.uniform(0,1)
y=random.uniform(0,1)

s=math.sqrt(1+y**2)*math.sin(x**2/(1+abs(y)))
print(f"x = {x: .3f}")
print(f"y = {y: .3f}")
print(f"s = {s: .3f}")"""     #14

'''n=int(input())
onluq=0
p=0
while n>0:
    r=n%10
    onluq=onluq+r*2**p
    p+=1
    n//=10
print(onluq)'''            #2-10


'''n=int(input())
onluq=0
p=0
while n>0:
    r=n%10
    onluq+=r*8**p
    p+=1
    n//=10
print(onluq)'''          #8-10


'''n=int(input())
ikilik=0
p=1
while n>0:
    r=n%2
    ikilik+=r*p
    p*=10
    n//=2
print(ikilik)'''            #10-2



"""from random import *
for i in range(5):
    for j in range (10):
        n=randint(1,100)
        print(n,end=" ")
    print()          """               #setir sutun




'''from random import *
for i in range(5):
    min=101
    max=0
    for j in range (10):
        n=randint(1,100)
        print(n,end=' ')
        if n<min:
            min=n
        if n>max:
            max=n
    print(min,max)'''            #setir sutun max min


"""from random import *
for i in range(5):
    c=0
    for j in range (10):
        n=randint(1,100)
        print(n,end=" ")
        c+=n
    print("cem",c)"""             #setir sutun cem



"""def f():
    
    cem=0
    while True:
        x=int(input())
        if x==-1:
            break
        cem+=x

    if cem %2==0:
        return("cut")
    else:
        return('tek')

print(f())"""                   #L5,1





"""def f(a,b):
    if b==0:
        return False
    qismet=a//b
    if qismet %2==0:
        return True
    else:
        return False
a=int(input())
b=int(input())
print(f(a,b))"""                #L5,2





"""def f(k,n):
    if k**k==n:
        return True
    else:
        return False
k=int(input())
n=int(input())
print(f(k,n))"""                    #L5,3




"""def f(x):
    n=0
    while n*(n+1)<= x:
        if n*(n+1)==x:
            return "pronic"
        n+=1
    return "heteromec"
x=int(input())
print(f(x))"""                      #L5,4




"""def f(n):
    if n==0:
        return 1
    n=abs(n)
    say=0
    while n>0:
        say+=1
        n//=10
    return say
print(f(int(input())))"""          #L5,5




"""def f(x):
    copy=x
    t=x
    say=0
    while t>0:
        say+=1
        t//=10
    cem=0
    while x>0:
        reqem=x%10
        cem+=reqem**say
        say-=1
        x//=10
    return copy==cem
print(f(int(input())))"""               #L5,6





"""def f(x):
    f=1
    k=1
    while True:
        f*=k
        if f%x==0:
            return k
        k+=1
print(f(int(input())))"""               #L5,8




"""def sade(x):
    if x<2:
        return False
    for i in range(2,int(x**0.5)+1):
        if x%i==0:
            return False
            
        
    return True
def f(a):
    cem=0
    copy=a
    while copy>0:
      
        cem+= copy%10
        copy//=10
    if a%cem ==0 and sade(a//cem):
        return True
    else:
        return False
print(f(int(input())))"""              #L5,9
    
        
        

"""def f(x):
    son = x%10
    ilk=x
    while ilk>=10:
        ilk//=10
    cem=ilk +son
    if cem**0.5>3:
        return True
    else:
        return False
print(f(int(input())))"""               #L5,10,11




"""def ebob(a,b):
    while b!=0:
        a,b=b,a%b
    return a
def q_sade(a,b):
    return ebob(a,b) == 1
a=int(input())
b=int(input())
print(q_sade(a,b))"""            # L5,12


'''def sade(n):
    if n < 2:
        return False
    for i in range(2,int(n**0.5)+1):
        if n%i==0:
            return False
    return True
def hipersade(n):
    
    while n>0:
        if not sade(n):
            return False
        n//=10
    return True
n=int(input())
if hipersade(n):
    print("hipersadedir")
else:
    print("hipersade deyil.")'''                    #L5,13







'''def ebob(a,b):
    while b:
        a,b=b,a%b
    return a
def ekob(a,b):
    return a*b//ebob(a,b)
a=int(input())
b=int(input())
print('ebob:',ebob(a,b))
print('ekob:',ekob(a,b))'''               #L5,14





'''def f(a,b,c):
    if a>b:
        a,b=b,a
    if b>c:
        b,c=c,b
    if a>c:
        a,c=c,a
    return a,b,c
a,b,c=map(int,input().split())
x,y,z=f(a,b,c)
print(x,y,z)'''                     #L5,15




'''def ebob(a,b):
    while b:
        a,b=b,a%b
    return a
def f(m,n):
    k=ebob(m,n)
    return  m//k,n//k
m,n=map(int,input().split())
x,y=f(m,n)
print(x,y)'''               #L5,16




'''def t(n):
    ters=0
    while n>0:
        ters=ters*10+n%10
        n//=10
    return ters
n=int(input())
print(t(n))'''              #L5,17


"""
for i in range(1, 6):
    print(" "*(6-i), end="")
    for j in range(1, i+1):
        print(j,end="")
    print()"""


"""
for i in range(1, 5):
    print(" "*(5-i), end="")
    for j in range(1, i+1):
        print(j,end=" ")
    print()"""

"""
for i in range(1, 7):
    print("* " * i)
print()
for i in range(6, 0, -1):
    print("* " * i)
"""


"""from random import*
A =[randint(1,50) for i in range(1,12)]
print(A)
tapilan = []
istifade = []

for x in A:
    if x in istifade and x not in tapilan:
        tapilan.append(x)
    istifade.append(x)

if tapilan:
    print("Tapildi:", *tapilan)
else:
    print("Tapilmadi")"""


"""from random import*
a = [randint(1,50) for i in range(1,19)]
print(a)


# 1-ci maksimumu tapırıq
max1 = a[0]
for x in a:
    if x > max1:
        max1 = x

# max1-in bütün tekrarlarını silirik
while max1 in a:
    a.remove(max1)

# 2-ci maksimumu tapırıq
max2 = a[0]
for x in a:
    if x > max2:
        max2 = x

print("Maksimum:", max1)
print("2-ci maksimum:", max2)"""


"""from random import*
a = [randint(-10,10) for i in range(1,18)]
print(a)
b=[]
for x in a:
    if x<0 and x%2==0:
        b.append(x)
print(b)"""



"""from random import*
def sade(x):
    if x<2:
        return False 
    for i in range(2,int((x**0.5)+1)):
        if x%i==0:
            return False
    return True
a=[randint(0,100) for i in range(1,14)]
print(a)
b=[]
for c in a:
    if sade(c):
        b.append(c)
print(b)"""




