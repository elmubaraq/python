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
#(4)extract type hint from a function uisn typing.get_type_hints(func)
from typing import get_type_hints
def extractType(a:int, b:float, *args, **kwargs) -> bool:
    return
print(get_type_hints(extractType))

#(5) groupby
from itertools import groupby

iterDict = [{"name": "musa", "age":29},
            {"name": "Sulaiman", "age":20},{"name": "Ali", "age":29}, {"name": "James", "age":30},
            {"name": "Sam", "age":20}]
groupby_obj = groupby(iterDict, key =  lambda x: x["age"])
for key, value in groupby_obj : print(key, list(value))

anoda_group_by_list =[1,2,3,4,5,67,8,9,10,11,12]
groupby_obj2 = groupby(anoda_group_by_list, lambda x : x <8)
for key, value in groupby_obj2: print(key, list(value))

#6 count, cycle, repeat
from itertools import count, repeat, cycle
for num in count(10):
    #print(num)
    if num  == 30: break

#7 sorted, map, filter
sortedList = [(1,3), (6,3), (6,1), (9,5) ]    
sorted(sortedList, key = lambda x=sortedList: x[0] + x[1] )
def map_func(x):
    return x[0] + x[1]

map_try = map(map_func, sortedList)
print(list(map_try))

def filter_func(x):
    y = x[0] + x[1]
    return y %2 ==0 

filter_try = filter(filter_func, sortedList) 
print(list(filter_try))
#filter_listcomprehension = [x for  x in sortedList if x[0] + x[1] % 2 == 0]
#print(filter_listcomprehension)
