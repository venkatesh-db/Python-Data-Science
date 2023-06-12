#  Data  | gossip 
#  Visulaisation 
#  Relationship | Dependancy
#  Construction | Material | Interior { experience }
#  Product knowledge { pizza }
#  Buy product  - cusomer behaviour
#  Different FileSystem


https://www.chartjs.org/docs/next/samples/line/line.html
ggplot

from plotnine.data import economics
from plotnine import ggplot, aes, geom_line

(
    ggplot(economics)  # What data to use
    + aes(x="date", y="pop")  # What variable to use
    + geom_line()  # Geometric object to use for drawing
)

ggplot(mpg) + aes(x="class") + geom_bar()

ggplot(huron) + aes(x="level") + geom_histogram(bins=10)


https://pymotw.com/2/contents.html


def Arg2(*args):  
    print("arg2",type(args))
    for arg in args:  # args[0] -> 6pointers ,  args[1] -> 6pointers  
        print (arg[0],arg[1]) 
    
Arg2( ('Wave', 'In', 'to', 1 ,2.3 ,True ) , ['Code', 'Seeker', 'JVT', 1 ,2.3 ,True ]  )  


def Commandline( **kwargs ):  
    print(type(kwargs))
    print("only keys")
    for arg in kwargs:  
        print (arg) 
    print("end keys")   
    print("only values")
    for arg in kwargs['first']:  
        print (arg) 
    print("end keys")
    for key, value in kwargs.items(): 
        print ("%s == %s" %(key, value)) 
  

Commandline( first ='code', mid ='seeker', last='jvt' )


class Vehicle:
    kind = 'car'

    def __init__(self, manufacturer, model):
        self.manufacturer = manufacturer
        self.model_name = model

    @property
    def name(self):
        print("property")
        return "%s %s" % (self.manufacturer, self.model_name)

    def __repr__(self):
        print("repr")
        return "<%s>" % self.name  # invokes property

    def dis(self):
          print("jvt")
    
car = Vehicle('Toyota', 'Corolla')
car.names



import re
txt = "The rain in Spain u Spain"


# ^     Starts with	                                             "^hello"
# $      Ends with	                                             "world$"
# .      Any character (except newline character)	 "he..o"
# []     A set of characters	"[a-m]"


x = re.search("^The.*Spain$", txt)
if (x):
  print("YES! We have a match!")
else:
  print("No match")



def pizza(  name = "gardenparty" , size ="medium"  ):
    print( name )


pizza( name = "chillpizza", "large" )