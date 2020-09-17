class Parent:
    def __init__(self):
        print("parent");
    def method1(self):
        print("method1")
class Parent2:
    def __init__(self):
        print("parent");
    def method1(self):
        print("method2")
class child(Parent2,Parent):
    def __init__(self):
        print("child")
        
temp = child();
temp.method1();