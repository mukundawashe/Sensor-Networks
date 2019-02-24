#random function outputs a number between 0 and 1
import random
import pickle
import datetime
instances = 4
#define criteria for creating several instances
for n in range(instances):
    #define a function so that it can be called several times
    def my_func():
        rows = 32
        for r in range(rows):
            #set conditions to create a matrix (dataset)
            w, h = 16, 1;
            Matrix = [[random.random() for x in range(w)] for y in range(h)]
            print(r + 1)
            dt = str(datetime.datetime.now())
            print(dt)
            print(Matrix)
            print(type(Matrix))
    #pickle.dump(my_func, open('my_func.dat', 'wb'))
    my_func()
