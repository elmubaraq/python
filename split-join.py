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
        
        