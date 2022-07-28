





raw_file='footballresults.txt'

with open(raw_file) as raw_data:
    lines=raw_data.readlines()
    #print(lines)
    clean_club=[]
    club_name=[]
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
        #print(fetch_index_1_to_minus3)


        if len(fetch_index_1_to_minus3) >0:
            club_name.append(fetch_index_1_to_minus3)
            
            
    club_name.pop(0)   
    
print(club_name)

#print({str(club_name[i:i+2]):club_name[i+2] for i in range(0,len(club_name),3)})

    
   



        


            
    
   
   