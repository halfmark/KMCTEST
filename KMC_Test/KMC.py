import re
import queue

inputs=['A19','B28','C23','D4','E78','F90','G32','H54','I32','J12','J67','L90','M87','N6','O36','P12','Q24']

#sort the inputs **All the older people must enter the premises first**

inputs=sorted(inputs,key=lambda x:int(re.findall(r'\d+$',x)[0]))
inputs.reverse()
print(inputs)


#People must stand in a queue
q=queue.Queue()

#filter the queue by alphebet
for x in range(len(inputs)-1):
    print(inputs[x])
    
    if int(inputs[x][1:])==int(inputs[x+1][1:]):
        
        
        s=[]
        s.append(inputs[x])
        s.append(inputs[x+1])

        #sort by Alphabet
        s.sort()
        print(s)
        inputs[x]=s[0]
        inputs[x+1]=s[1]
            

print(inputs)


z=[]
for i in inputs:
    #**No under 18 persons are allowed**
    #select the age of the person and check if the person is allowed or not
    if int(i[1:]) < 18:
        print ("This person is not allowed ",i)

    else:
        #All those who are allowed
        q.put((int(i[1:]),i))
        z.append(i)
       #print(i)
        
    

    
print(z)
#
while not q.empty():
    
    print(q.get())
