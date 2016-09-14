import re


Queue=['A19','B28','C23','D4','E78','F90','G32','H54','I32','J12','J67','L90','M87','N6','O36','P12','Q24']


j=0
z=[]
for i in Queue:
    if int(i[1:]) < 18:
        print ("This person is not allowed ",i)

    else:
        j=j+1
        z.append(i)
        print(i)
        
    

    
print(z)
