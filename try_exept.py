import sys
class A:
    def name(self):
        try:
            print("hello world i am safe")
        except Exception as e:
            pass
    def nameTry(self):
        try:
            b = 1/0;
            print(b)
        except Exception as e:
            print("i am not safe")
temp = A();
temp.nameTry();