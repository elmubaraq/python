from timeit import default_timer as timer

#(1)decimal places with f-string

def checkFloat(func):
    def wrapper(x):
        if type(x) == float:
            return func(x)
        else:
            raise TypeError("x is not a float")
    return wrapper
@checkFloat
def decimalPlaces(x):
    print(f"The value of x in 2 decimal places is {x:.2f}")
decimalPlaces(454.675)
valueTest = 8
def recursion():
   for num in range(valueTest): print("hello"), print("Done"), print("hello")
   

#(2) Padding and formating f-string
padding = lambda *args, **kwargs: [print(f"{arg:-^20}") for arg in args]
padding("hello","hey")
mapList= ['a','b','c']
myFstring = "Hello"
print("{} {} {}".format(myFstring, myFstring, myFstring), "%s"  %  myFstring)


#(3) type vs isinstance
start = timer()
type(mapList)
stop =timer()
print(stop-start)
start = timer()
isinstance(mapList, list)
stop =timer()
print(stop-start)