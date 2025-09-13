from multiprocessing import Process

def myFunc(n):
    print(f"calling myFunc from process n: {n}")
    for i in range(n):
        print(f"output from myFunc is :{i}")

if __name__ == "__main__":
    processes = []
    for i in range(5):
        p = Process(target=myFunc, args=(i,))
        processes.append(p)
        p.start()

    for p in processes:
        p.join()


# ------------------------------------------------------------------------


# from multiprocessing import Process
# import time
# import random
#
# def myFunc(n):
#     print(f"calling myFunc from process n: {n}")
#     for i in range(n):
#         print(f"output from myFunc is :{i}")
#         time.sleep(random.uniform(0.05, 0.2))
#
# if __name__ == "__main__":
#     processes = []
#     for i in range(5):
#         p = Process(target=myFunc, args=(i,))
#         processes.append(p)
#         p.start()
#
#     for p in processes:
#         p.join()


# ------------------------------------------------------------------------


# from multiprocessing import Process
#
# def myFunc(n):
#     print(f"calling myFunc from process n: {n}")
#     for i in range(n):
#         print(f"output from myFunc is :{i}")
#
# if __name__ == "__main__":
#     processes = []
#     for i in range(6):
#         p = Process(target=myFunc, args=(i,))
#         processes.append(p)
#         p.start()
#         p.join()
