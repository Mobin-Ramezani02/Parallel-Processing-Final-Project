# import threading
# import time
# import random
#
# def function_A():
#     print(threading.current_thread().name + " --> starting")
#     time.sleep(random.uniform(0.1, 1))
#     print(threading.current_thread().name + " --> exiting")
#
# def function_B():
#     print(threading.current_thread().name + " --> starting")
#     time.sleep(random.uniform(0.1, 1))
#     print(threading.current_thread().name + " --> exiting")
#
# def function_C():
#     print(threading.current_thread().name + " --> starting")
#     time.sleep(random.uniform(0.1, 1))
#     print(threading.current_thread().name + " --> exiting")
#
# t1 = threading.Thread(name='function_A', target=function_A)
# t2 = threading.Thread(name='function_B', target=function_B)
# t3 = threading.Thread(name='function_C', target=function_C)
#
# t1.start()
# t2.start()
# t3.start()
#
# t1.join()
# t2.join()
# t3.join()


# ------------------------------------------------------------------------

# import threading
# import time
# import random
#
# def function_A():
#     print(threading.current_thread().name + " --> starting")
#     time.sleep(random.uniform(0.1, 1))
#     print(threading.current_thread().name + " --> exiting")
#
# def function_B():
#     print(threading.current_thread().name + " --> starting")
#     time.sleep(random.uniform(0.1, 1))
#     print(threading.current_thread().name + " --> exiting")
#
# def function_C():
#     print(threading.current_thread().name + " --> starting")
#     time.sleep(random.uniform(0.1, 1))
#     print(threading.current_thread().name + " --> exiting")
#
# t1 = threading.Thread(name='function_A', target=function_A)
# t2 = threading.Thread(name='function_B', target=function_B)
# t3 = threading.Thread(name='function_C', target=function_C)
#
# t1.start()
# t1.join()
#
# t2.start()
# t2.join()
#
# t3.start()
# t3.join()


# ------------------------------------------------------------------------


import threading
import time
import random

def function_A():
    print(threading.current_thread().name + " --> starting")
    time.sleep(random.uniform(0.1, 1))
    print(threading.current_thread().name + " --> exiting")

def function_B():
    print(threading.current_thread().name + " --> starting")
    time.sleep(random.uniform(0.1, 1))
    print(threading.current_thread().name + " --> exiting")

def function_C():
    print(threading.current_thread().name + " --> starting")
    time.sleep(random.uniform(0.1, 1))
    print(threading.current_thread().name + " --> exiting")

t1 = threading.Thread(name='function_A', target=function_A)
t2 = threading.Thread(name='function_B', target=function_B)
t3 = threading.Thread(name='function_C', target=function_C)

t1.start()
t2.start()
t3.start()


