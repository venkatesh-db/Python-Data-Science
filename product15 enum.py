from enum import Enum, auto
class Mood(Enum):
     FUNKY = 1
     HAPPY = 3

     def describe(self):
         # self is the member here
         return self.name, self.value

     def __str__(self):
        print("winning")
        return 'my custom str! {0}'.format(self.value)

     @classmethod
     def favorite_mood(cls):
         # cls here is the enumeration
        return cls.HAPPY
        
obj =Mood(1)
tup=obj.describe()
tup=obj.favorite_mood()
print(tup)
print(obj)