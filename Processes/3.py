from multiprocessing import Process, current_process
import time

def foo():
    name = current_process().name
    print("Starting %s" % name)
    if name == 'background_process':
        for i in range(5):
            print("---> %d" % i)
            time.sleep(0.2)
    else:
        for i in range(5, 10):
            print("---> %d" % i)
            time.sleep(0.2)
    print("Exiting %s" % name)

if __name__ == "__main__":
    NO_background_process = Process(name="NO_background_process", target=foo)
    NO_background_process.daemon = False

    NO_background_process.start()
    NO_background_process.join()


#------------------------------------------------------------


# from multiprocessing import Process, current_process
# import time
#
# def foo():
#     name = current_process().name
#     print("Starting %s" % name)
#     if name == 'background_process':
#         for i in range(5):
#             print("---> %d" % i)
#             time.sleep(0.3)
#     else:
#         for i in range(5, 10):
#             print("---> %d" % i)
#             time.sleep(0.3)
#     print("Exiting %s" % name)
#
# if __name__ == "__main__":
#     background_process = Process(name="background_process", target=foo)
#     background_process.daemon = True
#
#     NO_background_process = Process(name="NO_background_process", target=foo)
#     NO_background_process.daemon = False
#
#     background_process.start()
#     NO_background_process.start()
#
#     background_process.join()
#     NO_background_process.join()


#------------------------------------------------------------


# from multiprocessing import Process, current_process
# import time

# def foo():
#     name = current_process().name
#     print("Starting %s" % name)
#     if name == 'background_process':
#         for i in range(5):
#             print("---> %d" % i)
#             time.sleep(0.3)
#     else:
#         for i in range(5, 10):
#             print("---> %d" % i)
#             time.sleep(0.3)
#     print("Exiting %s" % name)

# if __name__ == "__main__":
#     background_process = Process(name="background_process", target=foo)
#     background_process.daemon = True

#     NO_background_process = Process(name="NO_background_process", target=foo)
#     NO_background_process.daemon = False

#     background_process.start()
#     background_process.join()

#     NO_background_process.start()
#     NO_background_process.join()
