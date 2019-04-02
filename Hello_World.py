print("Hello World")
print("\nEnter a Number:")
n = int(input())
if n==1:
    print("One")
else:
    print("Not One")
a,b,c = 10,20,"I am the best"
#del b
print(a,c)
str = 'Hellow World!'
print(str)
print(str[0])
print(str[2:5])
print(str[2:])
print(str*2)
print(str+'UTKARSH')
listm = ['abcd',123,33.34,12034900,3+4j,'jain']
print(listm)
print(listm[0])
print(listm[2:6])
listm[2] = 124
print(listm)
tuplet = (1,99.96,'Utkarsh Jain',3+4j)
print(tuplet)
dictd = {}
dictd[1] = "One"
dictd['two'] = 2
print(dictd)
print(dictd.keys())
print(dictd.values())
print("My Values are %d and %d"%(a,b))
print("----------------Date and Time-------------------------")
import time
import calendar
t = time.time()
print(t)
print(time.localtime(time.time()))
print(time.altzone)
print(time.asctime(time.localtime(time.time())))
#print(time.clock())
print(time.ctime())
print(time.sleep(2))
print(time.ctime())
tx = (2019,3,23,15,34,40,6,12,0)
print(time.mktime(tx))
print(time.strftime("%b %d %Y %H:%M:%S",time.gmtime(time.mktime(tx))))
print(calendar.month(2019,3))
print("----------------Functions------------------------------")
def changename(arg):
    "This List changes the object passed"
    arg = [2,3,4]
    print("inside: ",arg)
    return

List = [10,20,30]
changename(List)
print("OUTSIDE:",List)

def Required(str):
    print(str)
    return
str = 'UTKARSH'
Required(str)

def Keyword(str1,num1):
    print(str1)
    num1 = num1 + 3
    print(num1)
Keyword(num1=10,str1='utkarsh')

def Default(name,age=25):
    print(name)
    print(age)
Default("Utkarsh")

def VariableLength(arg1, *argtuple):
    print(arg1)
    for i in argtuple:
        print(i)
VariableLength("UJAIN")
VariableLength("UJAIN",10,20,30)

sum = lambda arg1,arg2: arg1**arg2;
print("Lambda Function: ",sum(10,arg2=3))

total = 0
def Scope(a,b):
    total = a+b
    print("local",total)
    return
Scope(10,5)
print("GLOBAL: ",total)

print('----------------------Modules----------------------------')
from Trial import countFreq
import math
print("Truly new")
strL = [1,2,3,4,1,2,1,'abc','def','abc','xyz']
countFreq(strL)

Money = 2000
def AddMoney():
   # Uncomment the following line to fix the code:
   global Money
   Money = Money + 1

print(Money)
AddMoney()
print(Money)
content = dir(math)
print(content)

print("----------------------File I/O----------------------------")
f = open("foo.txt","w")
print("Name: ",f.name)
print("Closed or not: ",f.closed)
n = int(input("Enter the number: "))


