# import threading
# import time
# import random
#
# class Box:
#     def __init__(self):
#         self.lock = threading.RLock()
#         self.total_items = 0
#
#     def execute(self, value):
#         with self.lock:
#             self.total_items += value
#
#     def add(self):
#         with self.lock:
#             self.execute(1)
#
#     def remove(self):
#         with self.lock:
#             self.execute(-1)
#
# def adder(box, items):
#     print(f"N° {items} items to ADD")
#     while items > 0:
#         box.add()
#         print(f"ADDED one item -->{box.total_items} item to ADD")
#         items -= 1
#         time.sleep(0.1)
#
# def remover(box, items):
#     print(f"N° {items} items to REMOVE")
#     while items > 0:
#         box.remove()
#         print(f"REMOVED one item -->{box.total_items} item to REMOVE")
#         items -= 1
#         time.sleep(0.1)
#
# box = Box()
#
# items_to_add = 16
# items_to_remove = 1
#
# t1 = threading.Thread(target=adder, args=(box, items_to_add))
# t2 = threading.Thread(target=remover, args=(box, items_to_remove))
#
# t1.start()
# t2.start()
#
# t1.join()
# t2.join()


# ------------------------------------------------------------------------


# import threading
# import time
# import random
#
# class Box:
#     def __init__(self):
#         self.lock = threading.RLock()
#         self.total_items = 0
#
#     def execute(self, value):
#         with self.lock:
#             self.total_items += value
#
#     def add(self):
#         with self.lock:
#             self.execute(1)
#
#     def remove(self):
#         with self.lock:
#             self.execute(-1)
#
# def adder(box, items):
#     print(f"N° {items} items to ADD")
#     while items > 0:
#         box.add()
#         print(f"ADDED one item -->{box.total_items} item to ADD")
#         items -= 1
#         time.sleep(0.1)
#
# def remover(box, items):
#     print(f"N° {items} items to REMOVE")
#     while items > 0:
#         box.remove()
#         print(f"REMOVED one item -->{box.total_items} item to REMOVE")
#         items -= 1
#         time.sleep(0.1)
#
# box = Box()
#
# items_to_add = 16
# items_to_remove = 5
#
# t1 = threading.Thread(target=adder, args=(box, items_to_add))
# t2 = threading.Thread(target=remover, args=(box, items_to_remove))
#
# t1.start()
# t1.join()
#
# t2.start()
# t2.join()



# ------------------------------------------------------------------------


import threading
import time
import random

class Box:
    def __init__(self):
        self.lock = threading.RLock()
        self.total_items = 0

    def execute(self, value):
        with self.lock:
            self.total_items += value

    def add(self):
        with self.lock:
            self.execute(1)

    def remove(self):
        with self.lock:
            self.execute(-1)

def adder(box, items):
    print(f"N° {items} items to ADD")
    while items > 0:
        box.add()
        print(f"ADDED one item -->{box.total_items} item to ADD")
        items -= 1
        time.sleep(0.1)

def remover(box, items):
    print(f"N° {items} items to REMOVE")
    while items > 0:
        box.remove()
        print(f"REMOVED one item -->{box.total_items} item to REMOVE")
        items -= 1
        time.sleep(0.1)

box = Box()

items_to_add = 16
items_to_remove = 5

t1 = threading.Thread(target=adder, args=(box, items_to_add))
t2 = threading.Thread(target=remover, args=(box, items_to_remove))

t1.start()
t2.start()

t2.join()
t1.join()
