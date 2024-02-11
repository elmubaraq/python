my_str='I, am, Almubaraq, Musa, Akinlaso'
my_list= my_str.split(', ')
#the delimitter will limit it by (', ')
#we only join list we split str
#delimitter comes first in join  ''.join(var)
#print(my_list)
my_str1='I, am, Almubaraq, Musa, Akinlaso'

my_list1=[]

for letter in my_str1:
    if letter in ", ":
        my_str1.strip(letter)
#print(my_str1)

for letter in my_str1:
    my_list1.append(letter)

#print(my_list1)    
my_str3=''.join(my_list1)


new_str=''
for letter in my_str3:
    if letter not in ', ':
        new_str+=letter
print(new_str)

class Car:
    def __init__(self, Make, Model, Year):
        self.Make = Make
        self.Model = Model 
        self.Year = Year
        self.engine_mode = False 

    def Reliability(self):
        if self.Make == "Toyata":
            print("This car is reliable")
        else:
            print("We would need some more information") 
    def engine_mode_check(func):
        def wrapper(self):
            if not self.engine_mode:
                return func
            else:
                return "The engine is already running"
    @engine_mode_check
    def start_engine(self):
        print("engine is now running")


        
             
var1 = Car("Toyota","Camry","2018")
var1.Reliability()
#var1.start_engine()

def decor(func):
    def wrapper(x,y):
        if x >  -1 and y  > 0:
            return func(x,y)
    return wrapper
    
@decor
def letsee1(a,b):
     print("it's all good!")
letsee1(1,1)

def see(func):
    def wrapper(value):
        if type(value) == str:
            return func(value)
    return wrapper
@see
def mubbs(ok):
    print(ok)
mubbs("hello") 


okay = lambda x="hello": """ The value is %s """%(x)
print(okay())