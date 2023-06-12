import collections
#  object                                     classname    varaiable's
ramesh = collections.namedtuple('pizza', ["name", "size", "crust"])

suresh = ("name", "size", "crust")    
print(suresh)

import collections
# OrderedDict is dict
Ramya=collections.OrderedDict()    
Ramya['name']="gudio van russam"  
Ramya['size']=  "big"   
Ramya['crust']= "freed"  
Ramya['bill']=883    
Ramya[2]=883

for k,v in Ramya.items():    
    print (k,v)


from collections import defaultdict      
number = defaultdict(int)      
number['one'] = 1      
number['two'] = 2
print("default dict",number['two'])
print("default dict",number['three'])



# Counter is dict
from collections import Counter      
c = Counter()    
list = [1,2,3,4,5,7,8,5,9,6,10]      
Counter(list)    
Counter({1:5,2:4})      
list = [1,9,4,7,5,1,6,7,6,9,1]      
c = Counter(list)# key , value pair based on  total count of the value    
print(c[1])


# deque is list
from collections import deque    
list = ["c","cpp","java"]    
deq = deque(list)    
print(deq)


from collections import ChainMap  
baseline = {'Name': 'Peter', 'Age': '14'}  #parent
adjustments = {'Age': '14', 'Roll_no': '0012'}#child
obj=ChainMap(adjustments, baseline)


