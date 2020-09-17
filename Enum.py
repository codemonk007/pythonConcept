from  enum import Enum
# Using enum class create enumerations
class Days(Enum):
   Sun = 1
   Mon = 2
print('enum member accessed by name: ')
print (Days['Mon'])
print('enum member accessed by Value: ')
print (Days(1))