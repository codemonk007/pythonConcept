class Country:
    # def __init__(self):
      #  print('constuctor 1')
    def __init__(self, name="Default"):
        self.name = name
        print('constuctor 2')
    def instance_method(self):
        print('instance method')
default_country = Country()
india = Country('India')
print(default_country.name)
print(india.name)



class A:
    def __init__(self,name):
        self.names= name
        # simple method #ll
    def getnames(self): 
        print('Hi');

    def instance_method(self):
        print('instance method')
class B(A):
    def __init__(self):
        A.getnames(self);
        print('hi he') 

    def getnames(self): 
        print('Hi hello');


C=B();
C.getnames();