football_results="footballresults.txt"

with open(football_results) as thefile:
    lines= thefile.readlines()
    #print(lines)
    #print(type(lines))
    counter=0
    club_names=[]
    for item in lines:
        #print (item)
        #print (type(item))
        #counter= counter + 1
        #print(counter)
        eachline=item.split()
        #print(eachline[:4])
        #print(eachline, len(eachline))
        for items in eachline[:4]:
            try:
                int(items)
                print(int(items))
               # print(items(0-3))
            except:
                club_name="".join(items)
                print(club_name)
                #pass
                #clubnames=clubname.append()
'''footballresults=open(football_results,'r')
print(footballresults.read())
readL= footballresults.readlines()'''