#  OOPS
#  Object oriented programming langauge
#  Product     ==>  Process Pizza
#  customers  ==>  Endless 

prpizza= { "bill": 1000, "date" : "5-07-2021", "name ": "Margherita" ,  "size": "medium" ,  "Crust":"new hand toosed"}

'''
for i in prpizza:
      print(i)

for i in prpizza.values():
    print(i)
'''

Many= [{ "bill": 1000, "date" : "5-07-2021", "name ": "Margherita" ,  "size": "medium" ,  "Crust":"new hand toosed"},
       { "bill": 500, "date" : "3-07-2021", "name ": "gardenpizza" ,  "size": "small" ,  "Crust":"new hand toosed"},
       { "bill": 1300, "date" : "1-07-2021", "name ": "tingtong" ,  "size": "large" ,  "Crust":"new hand toosed"},
        { "bill": 700, "date" : "3-07-2021", "name ": "gardenpizza" ,  "size": "small" ,  "Crust":"new hand toosed"},
       { "bill": 900, "date" : "1-07-2021", "name ": "tingtong" ,  "size": "large" ,  "Crust":"new hand toosed"},
        { "bill": 1500, "date" : "3-05-2021", "name ": "gardenpizza" ,  "size": "small" ,  "Crust":"new hand toosed"},
       { "bill": 900, "date" : "12-06-2021", "name ": "tingtong" ,  "size": "large" ,  "Crust":"new hand toosed"},
        { "bill": 500, "date" : "13-07-2021", "name ": "gardenpizza" ,  "size": "small" ,  "Crust":"new hand toosed"},
       { "bill": 900, "date" : "1-07-2021", "name ": "tingtong" ,  "size": "large" ,  "Crust":"new hand toosed"},
        { "bill": 800, "date" : "3-07-2021", "name ": "gardenpizza" ,  "size": "small" ,  "Crust":"new hand toosed"},
       { "bill": 1900, "date" : "1-07-2021", "name ": "tingtong" ,  "size": "large" ,  "Crust":"new hand toosed"}  
       ]

# customer logic

vip=0
mt=0
sm=0
for i in Many:
     if i["bill"]>=1000:
         vip=vip+1
     elif i["bill"]>500 and i["bill"]<=1000:
         mt=mt+1
     elif i["bill"]  <= 500:
         sm=sm+1
     else:
        print("low profile customer")

print( "customer list   vip", vip) 
print( "customer list   mt", mt)
print( "customer list   sm", sm)


td=0
yd=0
pd=0
for i in Many:
     if i["date"] =="5-07-2021":
          if i["bill"]>=1000:
            vip=vip+1
          elif i["bill"]>500 and i["bill"]<=1000:
            mt=mt+1
          elif i["bill"]  <= 500:
            sm=sm+1
          td=td+1
     elif i["date"]=="3-07-2021":
         yd=yd+1
     elif i["date"]  =="1-07-2021":
         pd=pd+1
     else:
        print("no date checking customer")

print( "customer list   td", td) 
print( "customer list   yd", yd)
print( "customer list   pd", pd)         

custup= [ ("9900367097", "venkatesh.db@gmail.com","bangalore"),  ("8900367097", "victory.db@gmail.com","malayasia")    ]


# Product , customer stored in datastruture can stored in afile  xl , csv 
# customer has own choice what customer buys more DataAnalytic's
