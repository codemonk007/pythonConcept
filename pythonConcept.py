pip version freeze

pip install vertualenv

vertualenv venv --python=python3.5

source venv/bin/activate

python --version

pip install flast-restful

* import Flast,Resource,APi


class item{

    def get(self,name)
}


addresource(item,'/tere')



# defining a class
class A{
    constructor(self){

    }


    #all instance method should complasarily have (self) along with it .

}





#abstract method

from abc import ABC,abstract method.
class A(ABC){
    # canniot have construcotr
    constructor(self){}

}



# use pass for no implementation 
 def somemethod():
     pass


# important _init_ is the constructor

  def __init__(self, name, copies):
        self.name = name
        self.copies = copies


_repr_(self) is for TpString method





use @property for getter and 
@copies.setter for setter


try Execept e as error 
finally 


class A --> class B(A)  __init__ (){ super._init_}

when there is 



operator overload





for i in range(1,10):




if
elif
else:



partsing  int()



while i <10 :
    float 
    int
    bool
    str


list(map(lambda x: x.upper() ,words))
reduce(lambda x,y:x+y ,numbers )
filter(lambda x,y:x+y ,numbers )



tuple months = [('Jan',31),('Feb',28),('Mar',31)]


from collections import namedtuple
Point = namedtuple('Point',['x','y'])


os.system('clear')


for ch in message:
 print(ch)


class Currency(Enum):
    USD = 1
EUR = 2 INR = 3



duck typing







from abc import ABC,abstractclassmethod

class A(ABC):
    
    @abstractclassmethod
    def name(self):
        pass

class B(A):
    def getName(self):
        print(f'Hello')

    def name(self):
        print(f'hello ji')
        


check = B();

check.getName();


staticmethod
@staticmethod
    def static_method():
        print("I'm static")

static variable
Book.count = Book.count + 1