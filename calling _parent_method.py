class A:
    def name(self):
        print(f'hi');

class B(A):
    def name(self):
        A.name(self);
        print("india")

temp = B();
temp.name();