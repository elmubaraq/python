names=['Musa','Almubaraq','Zamani','Peace','Akinlaso','ppp']

for i in names:
        #print(names[i])
        if i[0] in 'AEIOU':
            print([i],'starts with a vowel')
        else:
            print([i],'starts with a consonant')
            

   
   
   
            
i=0           
while i < len(names):
    

    print(names[i])
    i+=1
    
for i in range(len(names)):
    print(names[i])
print(type(range(len(names))))

print((range(len(names))))


print(range(6))

my_list=[]
while i < len(names):
    my_list.append(names)
    i +=1
print(my_list)


counter=0
for item in names:
    counter +=1
print(counter)

#sentence=' '.join(names)
sentence=''
for i in names:
    sentence= sentence+i#+' '
    sentence+=' '
print(sentence)
print(int('01010111',2))

sentence2='Four score and Seven years ago'
sentence_with_vowel=''
for letter in sentence2:
    if letter not in 'aeuioAEIOU':
        sentence_with_vowel+= letter
print(sentence_with_vowel)
