
def win( sal):
    if sal >0 :
        print("recursion")
        win(sal-1)  // Line 2

win(10)

"recusive   Vs Generatr "


def  database( ):
     print("first phase ")
     yield 
     print("second phase ")
     yield

gen=database( )  # generator object
next(gen) // Line 13
next(gen) // Line 14

" Co routine "

def print_name(prefix):
    print("Searching prefix:{}".format(prefix))
    print( "coroutine")
    while True:
        print("while loop")
        name = (yield)
        print("first yield")
        if prefix in name:
            print(name)
 
# calling coroutine, nothing will happen
corou = print_name("jvt")
 
# This will start execution of coroutine and
# Prints first line "Searchig prefix..."
# and advance execution to the first yield expression
corou.__next__()
 
# sending inputs
corou.send("pyton")
print("coroutine never die's")
corou.send("Dear jvt")

"clojure"

def hack( ):
   def secret( ):
       print("ur cracked password ")
   return secret

ret= hack( )
ret()


import dis
dis.dis(hack)


class piZZA:
     # process of making product is method
     def  __init__(self):
          self._name= "Margherita"  # protected
          self._size   = "medium"      # protected
          self.bill = "new hand toosed" # bill =>Method      @bill.setter
     @property
     def bill(self ):
           print("get ")
           return self._bill
     @bill.setter
     def bill(self ,val):
           print("set ")
           self._bill = val
     def __str__(self):
        print("object representation")
        return self._bill
     def __add__(self , val):
        print("object addition")
        return self._bill
     def __sub__(self , val):
        print("sub method")
        return self._bill
     def __iter__(self , val):
        print("sub method")
        return self._bill

Ramesh= piZZA( ) #  

#process

ret = Ramesh.bill

print(ret)

suresh= piZZA( ) 

print(Ramesh+suresh)

print(Ramesh-suresh)

# Method's

( ) 
= 
del
Object
object.__code__
      -__class__

" EXample __class __ "

class pizza:
    def __init__(self, p):
        print("inside pizza __init__()")
        self.p = p
  
    def __str__(self):
        print("inside __str__()")
        print("value of p:", str(self.p))
  
    def __call__(self):
        res = 0
        print("inside __call__()")
        print("adding 2 to the value of p")
        res = self.p + 2
        return res
          
# declaration of instance of class A
a = pizza(3)
  
# calling __str__() for a
a.__str__()
  
# calling __call__() for a 
r = a()
print(r)
  
# declaration of another instance
# of class A
b = pizza(10)
  
# calling __str__() for b
b.__str__()
  
# calling __call__() for b
r = b()
print(r)



https://pymotw.com/2/sys/tracing.html



import sys

def trace_lines(frame, event, arg):
    if event != 'line':
        return
    co = frame.f_code
    func_name = co.co_name
    line_no = frame.f_lineno
    filename = co.co_filename
    print ( '%s line %s' % (func_name, line_no))

def trace_calls(frame, event, arg):
    if event != 'call':
        return
    co = frame.f_code
    func_name = co.co_name
    if func_name == 'write':
        # Ignore write() calls from print statements
        return
    line_no = frame.f_lineno
    filename = co.co_filename
    print ('Call to %s on line %s of %s' % (func_name, line_no, filename))
    if func_name in TRACE_INTO:
        # Trace into this function
        return trace_lines
    return

def c(input):
    print ('input =', input )
    print ('Leaving c()')

def b(arg):
    val = arg * 5
    c(val)
    print ('Leaving b()')

def a():
    b(2)
    print ('Leaving a()')
    
TRACE_INTO = ['b']

sys.settrace(trace_calls)
a()