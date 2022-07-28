lst=['age',8,'name','Musa Almubaraq','course','ict']
lst1={lst[i]:lst[i+1] for i in range(0,len(lst),2)}
#print(lst1)


lst3=['Name','of student','Musa Almubaraq','course','of study','ICT','Academic','Qualification','B.Sc','Your','Age','20']

#list_conc=' '.join(str((lst3[i:i+2])).strip('[,]') + lst3[i+2] for i in range(0,len(lst3),3))
#print(list_conc)
lst4={str(lst3[i:i+2]).strip("[',]"):lst3[i+2] for i in range(0,len(lst3),3)}
print(lst4)
'''for i in range(0,len(lst3),3):
    lst4={str(lst3[i:i+2]).strip("[']"):lst3[i+2] }
    for letter in str(lst3[i:i+2]):
        if letter in "',":
            str(lst3[i:i+2]).strip(letter)
    
        print(lst4)'''


