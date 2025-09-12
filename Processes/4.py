# from multiprocessing import Process
# import time
#
# def foo():
#     print("Starting function")
#     time.sleep(5)  # فقط یک sleep طولانی به جای loop
#     print("Finished function")
#
# if __name__ == "__main__":
#     p = Process(target=foo)
#
#     print("Process before execution:", p, p.is_alive())
#     p.start()
#     print("Process running:", p, p.is_alive())
#
#     time.sleep(1)  # خیلی سریع terminate
#     p.terminate()
#     print("Process terminated:", p, p.is_alive())
#
#     p.join()
#     print("Process joined:", p, p.is_alive())
#     print("Process exit code:", p.exitcode)


#------------------------------------------------------------


# from multiprocessing import Process
# import time
#
# def foo():
#     print("Starting function")
#     for i in range(10):
#         print(f"--> {i}")
#         time.sleep(0.5)
#     print("Finished function")
#
# if __name__ == "__main__":
#     p = Process(target=foo)
#
#     print("Process before execution:", p, p.is_alive())
#     p.start()
#     print("Process running:", p, p.is_alive())
#
#     time.sleep(2)  # اجازه بده چند iteration انجام بده
#     p.terminate()
#     print("Process terminated:", p, p.is_alive())
#
#     p.join()
#     print("Process joined:", p, p.is_alive())
#     print("Process exit code:", p.exitcode)



#------------------------------------------------------------


from multiprocessing import Process
import time

def foo():
    print("Starting function")
    for i in range(5):
        print(f"--> {i}")
        time.sleep(0.5)
    print("Finished function")

if __name__ == "__main__":
    p = Process(target=foo)

    print("Process before execution:", p, p.is_alive())
    p.start()
    print("Process running:", p, p.is_alive())

    p.join()  # بدون terminate
    print("Process joined:", p, p.is_alive())
    print("Process exit code:", p.exitcode)
