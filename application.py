


football_result = "football-league-results.txt"
"""football_result = open(football_result, "r")
print(football_result.read())"""

with open(football_result) as thefile:
    lines = thefile.readlines()
    #print(type(lines))
    counter = 0
    club_names =[]
    for item in lines:
        eachline = item.split()
        #print(eachline[:4])
        eachline_3items = eachline[1:4]
        #print(eachline_3items)
        try:
            if int(eachline_3items[-1]):
                pass
            eachline_3items.remove(eachline_3items[-1])
        except:
            pass
        #print(eachline_3items)
        club_name = " ".join(eachline_3items)
        
        if len(club_name) > 0 :
            club_names.append(club_name)
        print(club_names)
    club_names.pop(0)
    #print(club_names)
        

            
