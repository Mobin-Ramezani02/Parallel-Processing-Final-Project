# from multiprocessing import Process
# import time
#
# class MyProcess(Process):
#     def __init__(self, number):
#         super().__init__(name=f"MyProcess-{number}")
#         self.number = number
#
#     def run(self):
#         print(f"called run method by {self.name}")
#         time.sleep(0.5)
#
# if __name__ == "__main__":
#     n = 10
#     processes = []
#
#     for i in range(1, n + 1):
#         p = MyProcess(i)
#         p.start()
#         processes.append(p)
#
#     for p in processes:
#         p.join()


#------------------------------------------------------------


# from multiprocessing import Process
# import time
#
# class MyProcess(Process):
#     def __init__(self, number):
#         super().__init__(name=f"MyProcess-{number}")
#         self.number = number
#
#     def run(self):
#         print(f"called run method by {self.name}")
#         time.sleep(0.1)
#
# if __name__ == "__main__":
#     n = 5
#     for i in range(1, n + 1):
#         p = MyProcess(i)
#         p.start()
#         p.join()


#------------------------------------------------------------

from multiprocessing import Process
import time

class MyProcess(Process):
    def __init__(self, number):
        super().__init__(name=f"MyProcess-{number}")
        self.number = number

    def run(self):
        print(f"called run method by {self.name}")
        time.sleep(0.1)

if __name__ == "__main__":
    n = 5
    processes = []

    for i in range(1, n + 1):
        p = MyProcess(i)
        p.start()
        processes.append(p)

    for p in reversed(processes):
        p.join()
