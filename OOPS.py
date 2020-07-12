class LandAnimal:
    def swim(self):
        print('swimtest')
class WaterAnimal:
    def swim(self):
        print('swimTestttt')
class Amphibian(LandAnimal, WaterAnimal):
    pass
frog = Amphibian()
frog.swim()
# frog.walk()