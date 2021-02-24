import timeit
import numpy as np

print('regular')
print(timeit.timeit(setup='myArray = range(1000)', stmt='[x ** 2 for x in myArray]', number=1000))


print('numpy')
otherArray = np.arange(1000)
obj = timeit.Timer(lambda: otherArray ** 2)

myCode = '''
otherArray = np.arange(1000)
otherArray ** 2
'''

print(timeit.timeit(setup='import numpy as np', stmt=myCode, number=1000))


