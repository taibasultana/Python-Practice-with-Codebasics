# for a given list numbers print square and cube of every numbers
# for example- Input: [2,3,8,9]
# output list: square: [4,9,64,81] & cube: [8,27,512,729]

import time
import threading

def calc_square(numbers) :
    print("calculate square numbers")
    for n in numbers:
         time.sleep(0.2)              
                         #Python time sleep function is used to add delay in the execution of a
                         # program. We can use python sleep function to halt the execution of the program for given time in seconds.
                         #    Notice that python time sleep function actually stops the execution of current thread only, not the 
                         # whole program.
        print('square:',n*n)

def calc_cube(numbers) :
    print("calculate cube numbers")
    for n in numbers:
        time.sleep(0.2)
        print('cube:',n*n*n)

arr = [2,3,8,9]

t = time.time()

t1= threading.Thread(target=calc_square,args=(arr,))
t2= threading.Thread(target=calc_cube,args=(arr,))

t1.start()
t2.start()

t1.join()
t2.join()

# calc_square(arr)
# calc_cube(arr)

print("done in :", time.time()-t)
print("Hah... I am done with all my work now!")

