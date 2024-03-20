import timeit
dict1 = {"First Name":"Almubaraq", "Last Name": "Musa", "Profession":"Python Programmer"}
dict1["Email"] = "musa.almubaraq@gmail.com"
print(dict1.get("Email"))
start = timeit.default_timer()
list2 = [item for key_value in dict1.items() for item in key_value]
stop = timeit.default_timer()
print(stop-start)
start2 = timeit.default_timer()
list3 = []
for key,value in dict1.items(): 
    list3.append(key)
    list3.append(value)
stop2 = timeit.default_timer()
print(stop2-start2)
print(list2,list3)
for key in dict1:
    #print(key)
    for value in dict1.values():
        #print(key, value)
        for key, value in dict1.items():
            pass#print(key,value)

def checkList(func):
    def wrapper(x):
        if type(x) == list:
            print("list")
        elif type(x) == dict:
            print("dict")
            return func(x)
    return wrapper
@checkList
def check(x):
    
    return "hello"
check(['hey'])

class carSystem:
    def __init__(self,make, model, year, color, engine_mode = False):
        self.make = make
        self.model = model
        self.year = year
        self.color = color
        self.engine_mode = engine_mode
    def carCheck(self):
        print(f"This car's make is {self.make}, model is {self.model}, year of make is {self.year}, and color is {self.color}")
    def startIgnition(self):
        if not self.engine_mode:
            self.engine_mode = True
            return "Engine Started!  Zoommmmmmmmmmm!"
        if self.engine_mode:
            return "Engine already running" 

MubbyCar = carSystem("Honda", "accord", "2014", "white", engine_mode=True,)
MubbyCar.carCheck()
print(MubbyCar.startIgnition())
