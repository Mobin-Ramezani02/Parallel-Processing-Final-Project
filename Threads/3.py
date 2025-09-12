import time
import os
import random
from threading import Thread

class MyThread(Thread):
    def __init__(self, number, duration):
        super().__init__()
        self.name = f"Thread#{number}"
        self.duration = duration

    def run(self):
        print(f"---> {self.name} running, belonging to process ID {os.getpid()}")
        time.sleep(self.duration)
        print(f"---> {self.name} over")

start_time = time.time()

threads = []
for i in range(1, 10):
    t = MyThread(i, random.uniform(0.1, 1))
    threads.append(t)

for t in threads:
    t.start()

for t in threads:
    t.join()

print("End")
print("--- %.4f seconds ---" % (time.time() - start_time))


# ------------------------------------------------------------------------


# import time
# import os
# import random
# from threading import Thread
#
# class MyThread(Thread):
#     def __init__(self, number, duration):
#         super().__init__()
#         self.name = f"Thread#{number}"
#         self.duration = duration
#
#     def run(self):
#         print(f"---> {self.name} running, belonging to process ID {os.getpid()}")
#         time.sleep(self.duration)
#         print(f"---> {self.name} over")
#
# start_time = time.time()
#
# for i in range(1, 10):
#     t = MyThread(i, random.uniform(0.1, 1))
#     t.start()
#     t.join()
#
# print("End")
# print("--- %.4f seconds ---" % (time.time() - start_time))



# ------------------------------------------------------------------------


# import time
# import os
# import random
# from threading import Thread
#
# class MyThread(Thread):
#     def __init__(self, number, duration):
#         super().__init__()
#         self.name = f"Thread#{number}"
#         self.duration = duration
#
#     def run(self):
#         print(f"---> {self.name} running, belonging to process ID {os.getpid()}")
#         time.sleep(self.duration)
#         print(f"---> {self.name} over")
#
# start_time = time.time()
#
# threads = []
#
# for i in range(1, 10):
#     t = MyThread(i, 1)
#     threads.append(t)
#
# for t in threads:
#     t.start()
#
# for t in threads:
#     t.join()
#
# print("End")
# print("--- %.4f seconds ---" % (time.time() - start_time))
