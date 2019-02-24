#random function outputs a number between 0 and 1
import random
import pickle
import datetime
instances = 1
#define criteria for creating several instances
for n in range(instances):
    #define a function so that it can be called several times
    def my_func():
        rows = 32
        for r in range(rows):
            #set conditions to create a matrix (dataset)
            w, h = 16, 1;
            Matrix = [[random.random() for x in range(w)] for y in range(h)]
            dt = str(datetime.datetime.now())
            print(dt)
            def convert(Matrix): #convert Matrix to tuple
                return tuple(Matrix)
            if (Matrix.count('err')) == 0:
                print(Matrix)
                print(r)
            else:
                print("error found")
                print("Error is on cluster", (r))
        row = 1
        for r in range(row):
            w, h = 16, 1;
            Matrix = ['err' for x in range(w) for y in range(h)]
            print(Matrix)
            def convert(Matrix):
                return tuple(Matrix)
            if (Matrix.count('err')) == 0:
                print(r + 32)
                print(Matrix)
            else:
                print("Error found")
                print("Error is on cluster no.", (r + 32)) #Printing cluster with error
                print('Error is on sensor no. ', ((Matrix.index('err'))) + 1) #first instance of err found in tuple
                print("Error occured at", dt) #timestamp
    pickle.dump(my_func, open('my_func.dat', 'wb'))
    my_func()