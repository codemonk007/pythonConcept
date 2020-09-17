class P:
    def __init__(self,x):
        self.x = x
    @property
    def x(self):
        return self.__x

    @x.setter
    def x(self, x):
        if x < 0:
            self.__x = 0
        elif x > 1000:
            self.__x = 10000000
        else:
            self.__x = x
p1 = P(1001)


p1.x =2000;
print(f'kjj',p1.x)