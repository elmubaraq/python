
name1='fish'
name2=name1*10
print(name2)



name="almubaraq"
print(type(name))
age=8
print(isinstance(age, str))
print(age)
num='90'
numINt=int(num)
#this is casting
print(numINt)
print(type(numINt))
name=str(name)
print('My name is'+ ' ' +name )
name+= ' '+ ' is my name.'
print(name)
myNum= 8
reminant= myNum %2
print(reminant)
Ab=isinstance(myNum, int)
print(type(Ab))
print(Ab)

print(Ab,  "True" or "False")
print( '"True" or "False"',Ab)

Condition1=True
Condition2=False
Condition3= Condition1 and Condition2
Condition4=Condition1 or Condition2
print('mubbs' or False)
print('mubbs' or True) #none is false, hence it takes mubbs
print('mubbs' or 'Mubbs')
print('mubbs' or 'True')
print(0 or 1)
print(1 or 20)
# or takes any value that is not falsy, if both are not falsy,
#  it takes the first value 
print(0 or False)
print(0 or [] or False or '') #falsy values
#and
#if the first condition is True it evalutes rhe 2nd, if it's true
#it takes that
#if the first condition is false it wont't evalaute the second, 
#it takes the first
#last true first false
print(False or 0)# it returns the last value of all false collection
print('mubbs' and True) #none is false, hence it takes mubbs
print('first True' and 'second True')
print('mubbs' and 'True')
print(0 and 1)
print(1 and 20)
print(0 and [] and False and '')
#OR if x is false, then y, else x
#ANDif x is false, then x, else y
def is_adult(age):
    if age >= 18:
     return True
    if  age<18 and age>=13:
        return False, 'You are an underage teenage, you are ' + str(age) +'!'
# i just concatenated an int into a string
    else:    
        return False, 'underage'
         
print(is_adult(17))

print('''how
are 
you''')

def almubby():
    AbS={'age':10, 'name':[{'surname':'Musa', 'FirstName':'Almubaraq Musa  '}]}
    Abs='welcome to daylong, your best style, no wahala.'
    x=Abs.split(', ')
    strIp='      welcome    to daylong, your best style, no     wahala.   '
    print(Abs.upper())
    print(Abs.title())
    print('newList:',strIp.strip(' '))
    print('strIp=',strIp.replace(' ', ''))
    print(x)
    return AbS
print(len(almubby()))


def length(password):
    length=len(password)
    for x in password:
        if x.isdigit():
            x=True
        print(x)
    
    
    if  True in [y.isalpha() for y in password]:
        y=True
    print(y)
        
    if ( length>=8 and x and y ):
        return 'Strong password'
    else:
        return 'weak password'
print(length('2s6535631334yeurkjqwet243858'))


def test(case):
    for i in case:
      if  i.isdigit():
        return True
    else:
        return False

print(test('gfdsfha1'))

name='hello'
print("e" not in name)
print("p" in name)
if 'banana' in 'bananarama':
    print( 'I miss the 80s')

    