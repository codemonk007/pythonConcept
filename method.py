class A:
    def __init__(self,name):
        print(f'check'+name)
        self.name = name
    def testmethod(self):
        print('inside method')
        print(f"____"+self.name)
test = A("Ganapati");
test.testmethod();