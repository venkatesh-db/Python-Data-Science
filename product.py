
name = "Margherita"
size   = "medium"
Crust = "new hand toosed"
customername = "srinivas"

def  pizza( ):
    name = "Margherita"
    size   = "medium"
    Crust = "new hand toosed"
    if (  name  =="Margherita" ):
          print( "u can order",  name )
    if (  name  == "gardenparty" ):
         print( "u can order",  name )
    if (  name  == "hawaiin" ):  
         print( "u can order",  name )
    return 0

         
#pizza()
#pizza()

def pizzvariety( name:str , size ,  crust ):
    if  isinstance(name ,str):
        print("name is string type")
    if (  name  =="Margherita"  and size  =="large" ):
          bill = 1000
          print( "u can order pay 1000", bill , name )
    elif (  name  == "gardenparty" ):
         print( "not avalable" )  #  Line : return bill
         return -1 # out of function
    elif (  name  == "hawaiin" ):  
         print( "only left with 2" )
    else:
         print( " first time i amhearing from u")
    print("i am out")
    return bill

bill= pizzvariety( "gardenparty", "large","new hand toosed")
print( "return value", bill)

# product different varity of product's
# Margherita , gardenparty , hawaiin

class piZZA:    
     # process of making product is method
     def  __init__(self):
          self.name= "Margherita"
          self.size   = "medium"
          self.Crust = "new hand toosed"
     # abstraction
     def buyvegitables(self):
           pass
     def bill(self):
           print( self.name)
     def cutvegitables(self):
          pass
     def  mixing(self):
           pass
     def addingspices(self):
          pass
     def freshproduct(self):
          pass
     def __del__(self):
         print("desturctor")
     
#cutomer  product

Ramesh= piZZA( ) #  when customer buys product invokes constructor
Suresh =piZZA( )
Naresh=piZZA( )
#process
Ramesh.buyvegitables()
Ramesh.cutvegitables

Ramesh.bill()
del Ramesh         # eat and throw the product


