
class climax:
    def __init__ (self):
         print("constructor")
    def display(self):
         print("display")
         return "jvt"
    def __iadd__(self ,other):
         other()
         print("plus")

def works():
     return climax()

obj =climax().display()
print("way1 value ", obj)

obj1=works().display()
print("way2  value ",obj1)

def works1( ):
      return climax().display()

ret =works1()
print("way3 value",ret)

class codeseeker :
       pass

obj3 =climax()+ \
         codeseeker()


