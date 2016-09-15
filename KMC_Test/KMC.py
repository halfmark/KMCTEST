import re
import queue


class WhooziJuicy:

    def _init_(self,people):
        self.lists=people
        
    def Entry_Rules(self):
        #filter by digits next to alphabet ***Elders must enter the premises first*
        New_sorted_List=sorted(self.lists,key=lambda x:int(re.findall(r'\d+$',x)[0]))
        New_sorted_List.reverse()

        #People must stand in a queue
        Q_IN_queue=queue.Queue()

        #filter the queue by alphebet
        for item in range(len(New_sorted_List)-1):
            
            
            if int(New_sorted_List[item][1:])==int(New_sorted_List[item+1][1:]):
                
                array=[]
                array.append(New_sorted_List[item])
                array.append(New_sorted_List[item+1])

                #sort by Alphabet
                array.sort()
                New_sorted_List[item]=array[0]
                New_sorted_List[item+1]=array[1]
                    

        
        
        for item in New_sorted_List:
            #**No under 18 persons are allowed**
            #select the age of the person and check if the person is allowed or not
            if int(item[1:]) < 18 :
                print ("This person is not allowed ",item)
            elif int(item[1:]) == 90 :
                 print ("This nightclub is not able to assist this person",item)
            else:
                #All those who are allowed
                Q_IN_queue.put(item)
               
               
                
        while not Q_IN_queue.empty():
            print("Person ",Q_IN_queue.get(),"Enters the premises")
   
        
        
        
