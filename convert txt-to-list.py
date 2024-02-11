from distutils.command.clean import clean


raw_file='footballresults.txt'

with open(raw_file) as raw_data:
    lines=raw_data.readlines()
    #print(lines)
clean_club=[]
for items in lines:
    each_line= items.split()
    #print(each_line)
    #['8.', 'Port', 'Harcourt', 'Sharks', '38', '12', '14', '12', '46', '-', '47', '50']
    fetch_index_1_to_minus3= each_line[1:-3]
    #print(fetch_index_1_to_minus3)
    #['Port', 'Harcourt', 'Sharks', '38', '12', '14', '12', '46']
    for each_item in fetch_index_1_to_minus3:
       del(fetch_index_1_to_minus3[3:-1])
    #print(fetch_index_1_to_minus3)
    
    try:
        if int(fetch_index_1_to_minus3[-2]):
         pass
        fetch_index_1_to_minus3.remove(fetch_index_1_to_minus3[-2])
    
    except:
        pass
    
    club_name=' '.join(fetch_index_1_to_minus3)
    
    if len(club_name) >0:
        clean_club.append(club_name)
        
clean_club.pop(0)
#print(type(clean_club))
def Split_by_num(lst):
        if True in [lst[i].isdigit() for i in lst]:
           lst.split()[0]
            
            
print(Split_by_num(clean_club))
    
    
        

    

            
    
   
   