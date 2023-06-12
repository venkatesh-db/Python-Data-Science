#OOPS
# Object oriented programming langauge
# customer  => Product
#  Product ==> Process OOPS

# Encapsulation
# Abstraction
# Inheritence
# Polymorphism

# Product  Paramter's
# 1. process of making product { method's  : boilng , mixing }
# 2. product variable , data
# 3. variety of product { gardenparty }
# 4. price , offer , Logic
# 5. Locations

class piZZA:
     # process of making product is method
     def  __init__(self):
          self._name= "Margherita"  # protected
          self._size   = "medium"      # protected
          self.__Crust = "new hand toosed" # private
     def pizzvariety( name:str ,size,crust):
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
     def feedback(self):  # Polymorphism
          print("taste of the product")
     def __del__(self):
         print("desturctor")

# CustomerParamter's 
# 1. customer can order variety of product  listed by product
# 2. customer may ask unknown product { Validation : chillbyte}
# 3. customer details phonennum , email id ,Address {  Validation : chillbyte}
# 4. bill details customername ,product u buyed , emaild 
# 5. Feedback

class customerdetails(piZZA ):   # inheritence
    avgrating = 0
    def __init__(self , pno , eid ,add  ):
         piZZA.__init__(self)         # inheritence
         self.phoneno = pno
         self.emailid = eid
         self.address = add
         self.rating =0
    def billdetails(self):
         print( self._name , self._size )
    def feedback(self ,rat ):       #Polymorphism
         self.rating =rat

#cutomer  product

Ramesh= customerdetails( pno=9900367097 , eid="stay@gmail.com",add="london" ) #  when customer buys product invokes constructor
Suresh =customerdetails(8900367097 , "uare@gmail.com","india" )
Naresh=customerdetails(9900367099 , "fine@gmail.com","us" )

#process

Ramesh.billdetails()
Ramesh.feedback(4)



    
