# import concurrent.futures

# def foo(bar):
#     print('hello {}'.format(bar))
#     return 'foo'

# with concurrent.futures.ThreadPoolExecutor() as executor:
#     future = executor.submit(foo, 'world!')
#     return_value = future.result()
#     print(return_value)


import time
from threading import Thread

time_stamp = time.time()
print(time_stamp)
print(type(time_stamp))

# custom thread
# class CustomThread(Thread):
#     # constructor
#     def __init__(self):
#         # execute the base constructor
#         Thread.__init__(self)
#         # set a default value
#         self.return_val = None

#     # function executed in a new thread
#     def run(self):
#         # store data in an instance variable
#         self.return_val = [1, 2, 3]

# # create a new thread
# # thread = CustomThread()

# quit = False
# while (quit == False):
#   time.sleep(2)
#   thread = CustomThread()
#   # start the thread
#   thread.start()
#   # wait for the thread to finish
#   thread.join()
#   # get the value returned from the thread
#   data = thread.return_val
#   print(data[0], data[1], data[2])