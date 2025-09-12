# import threading
# import time
# import random
#
# def my_func(n):
#     print(f"my_func called by thread N{n}")
#
# threads = []
#
# for i in range(10):
#     t = threading.Thread(target=my_func, args=(i,))
#     threads.append(t)
#     t.start()
#
# for t in threads:
#     t.join()


# ------------------------------------------------------------------------


# import threading
# import time
# import random
#
# def my_func(n):
#     print(f"my_func called by thread N{n}")
#
# for i in range(10):
#     t = threading.Thread(target=my_func, args=(i,))
#     t.start()
#     t.join()


# ------------------------------------------------------------------------


# import threading
# import time
# import random
#
# def my_func(n):
#     time.sleep(random.uniform(0.1, 1))
#     print(f"my_func called by thread N{n}")
#
# for i in range(10):
#     t = threading.Thread(target=my_func, args=(i,))
#     t.start()
#
# time.sleep(3)
