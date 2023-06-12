class profit:
   def __init__(self ,v ):
     self.selling = v
     print(self.selling)

class gardenparty:
    __totalorders =0 # Encapsulation
    pt = profit(50) 
    offer = "50 off"
    def __init__(self , s ): # self :Customer
        self.size =s
        self.pt = profit(50) 
        gardenparty.__totalorders+=1
    def totalorder(self):
        print(gardenparty.__totalorders )

      
#customer reka  __totalorders is Encapsulation but still using method totalorder Abstraction
reka=gardenparty("big")
reka.totalorder()




