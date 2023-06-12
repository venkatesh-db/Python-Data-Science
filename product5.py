#Data structure List Methods

'''
0. Get value         [0]
1. Adddata          append  insert    extend 
2. Removedata     pop      remove   clear
3. Searching        index    count
3. Sort                sort  
4. Reverse           reverse
5. Copy               copy

#Data structure Dict  Methods

0. List ,value              fromkeys  create new dictonary
1. Adddata
    setdefault             new variable { coloumn }
    update                  new variable { coloumn , data }
2. Removedata          pop  popitem { one column} clear
3. Searching
  1. get specific value     get
  2. items                      all value's
  3. key                        all variable's
  4. values                    all value's
4. Copy                        copy


" Product owner pizaahut customer insights "
" Getting customer insights "
" Customer choice's "
'''
ci =[ { "bill": [1000,1001,2001,2003] , "date":[ "03-07-2021","04-07-2021","05-07-2021","06-07-2021",
"07-07-2021","08-07-2021","09-07-2021"  ]}]

ci[0].update({"name":["c","cpp","java" ]})


cii =[ { "bill": 1000,"date": "03-07-2021" }, { "bill": 500,"date": "04-07-2021" } ]
cii[0].update({"name": "c"})

# Rules' dont write  class , method's
#1. LIST Adddata          append  insert    extend 
#2. Removedata     pop      remove   clear
#3. Searching        index    count
#3. Sort                sort  
#4. Reverse           reverse
#5. Copy               copy
#1. DICT Adddata append  insert    extend 
#2. Removedata     pop      remove   clear
#3. Searching        index    count
#3. Sort                sort  
#4. Reverse           reverse
#5. Copy               copy
# Ms office software to open xl sheet
# Library{ pandas , csv } to open Xl sheet

import csv

#Logic

# "bill" >=1000                                        it will show 4 records

# "date" =="5-07-2021"    "bill">=1000   it will show 4 records

# copy concept's big elephant , small elephant

# remove collums , add collomn's

# Data cleaning

# Data visulation Date vs price

# statistic's mean , median , 

#  datastructure's Machine learning Linear regression

#  customer data till date

# Tom data can do predication yesterday last 3 year


