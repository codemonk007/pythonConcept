from abc import ABC
class A(ABC):
    def __init__(self):
        print("name is Ganapati")
    @abstractmethod
    def getName(self):
        pass

class child(A):
    def __init__(self):
        pass
    def getName(self):
        pass
        
temp = child()
temp.getName()
