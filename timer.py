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