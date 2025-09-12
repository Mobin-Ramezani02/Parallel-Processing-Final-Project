# from multiprocessing import Process, current_process
# import time
#
# def myFunc():
#     proc = current_process()
#     print(f"Starting process name = {proc.name}")
#     time.sleep(0.5)
#     print(f"Exiting process name = {proc.name}")
#
# if __name__ == "__main__":
#     processes = []
#
#     for i in range(5):
#         p = Process(target=myFunc, name=f"Process-{i+1}")
#         processes.append(p)
#         p.start()
#
#     for p in processes:
#         p.join()


# ------------------------------------------------------------------------


# from multiprocessing import Process, current_process
# import time
# import random
#
# def myFunc():
#     proc = current_process()
#     print(f"Starting process name = {proc.name}")
#     time.sleep(random.uniform(0.05, 0.2))
#     print(f"Exiting process name = {proc.name}")
#
# if __name__ == "__main__":
#     processes = []
#
#     for i in range(5):
#         p = Process(target=myFunc, name=f"Process-{i+1}")
#         processes.append(p)
#         p.start()
#
#     for p in processes:
#         p.join()


# ------------------------------------------------------------------------


# from multiprocessing import Process, current_process
# import time
#
# def myFunc():
#     proc = current_process()
#     print(f"Starting process name = {proc.name}")
#     time.sleep(0.2)
#     print(f"Exiting process name = {proc.name}")
#
# if __name__ == "__main__":
#
#     for i in range(5):
#         p = Process(target=myFunc, name=f"Process-{i+1}")
#         p.start()
#         p.join()
