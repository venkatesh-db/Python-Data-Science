#OOPS
# Object oriented programming langauge
# customer  => Product
#  Product ==> Process OOPS

# Abstraction
# Encapsulation
# Inheritence
# Polymorphism

# Product  { Process + variety data  + what are u selling + logic  }
# Customer : hide's process of making pizza  { variety }

class gardenparty:
    __totalorders =0 # Encapsulation
    offer = "50 off"
    def __init__(self , s ): # self :Customer
        self.size =s
        gardenparty.__totalorders+=1
    def totalorder(self):
        print(gardenparty.__totalorders )
    @staticmethod
    def todayoffer( ):
      print(gardenparty.offer )
      
#customer reka  __totalorders is Encapsulation but still using method totalorder Abstraction
reka=gardenparty("big")
reka.totalorder()
gardenparty.todayoffer()


