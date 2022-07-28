my_list=list(range(10,100,10))

my_list.append(int('10'))

print(my_list)
my_list[-1]=100
print(my_list[:])
my_name="hello world"
print(my_name[6:])
my_Strings=['q','w','e','r','t','y','a']

my_Strings.sort()
my_Strings.pop(4)

print(my_Strings)
def list_check(list_item):
    if 'a' not in list_item:
        list_item.append('a')
    else:
        list_item.remove('a')
    return list_item
print(list_check(my_Strings))
print(my_name.find('o'))
print(my_list.index(30))
my_list.append('when')
#index(value) on list to get index
#find(value) on a string for find position
# in and not in could be used for both list and String
#str has no sort
#for loops through both str and list
print('n' in 'hello')
print ('n' not in  my_list)
print('this a slice', my_list[:], my_name[:], len(my_list), len(my_name))


try:
    print(my_name.find('w'))
    pass
except:
    pass

print(dir())
namez=['Zamani','Almubaraq','Musa','Akinlaso','Peace']
namez[0] in 'AEIUO'


        
       

    

    
    

