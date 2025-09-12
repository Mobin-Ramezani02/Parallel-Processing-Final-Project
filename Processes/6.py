# from multiprocessing import Process, Queue
# import time, random
#
# class Producer(Process):
#     def __init__(self, queue):
#         super().__init__()
#         self.queue = queue
#
#     def run(self):
#         for i in range(10):
#             item = random.randint(0, 256)
#             self.queue.put(item)
#             print(f"Process Producer : item {item} appended to queue {self.name}")
#             print(f"The size of queue is {self.queue.qsize()}")
#             time.sleep(0.3)
#
# class Consumer(Process):
#     def __init__(self, queue):
#         super().__init__()
#         self.queue = queue
#
#     def run(self):
#         while True:
#             if self.queue.empty():
#                 print("the queue is empty")
#                 break
#             else:
#                 time.sleep(0.2)
#                 item = self.queue.get()
#                 print(f"Process Consumer : item {item} popped from by {self.name}")
#                 time.sleep(0.1)
#
# if __name__ == "__main__":
#     queue = Queue()
#     p = Producer(queue)
#     c = Consumer(queue)
#
#     p.start()
#     c.start()
#     p.join()
#     c.join()


#------------------------------------------------------------


# from multiprocessing import Process, Queue
# import time, random
#
# class Producer(Process):
#     def __init__(self, name, queue):
#         super().__init__(name=name)
#         self.queue = queue
#
#     def run(self):
#         for i in range(5):
#             item = random.randint(0, 300)
#             self.queue.put(item)
#             print(f"Process Producer : item {item} appended to queue {self.name}")
#             print(f"The size of queue is {self.queue.qsize()}")
#             time.sleep(0.2)
#
# class Consumer(Process):
#     def __init__(self, queue, total_items):
#         super().__init__()
#         self.queue = queue
#         self.total_items = total_items
#
#     def run(self):
#         count = 0
#         while count < self.total_items:
#             if not self.queue.empty():
#                 item = self.queue.get()
#                 print(f"Process Consumer : item {item} popped from by {self.name}")
#                 count += 1
#                 time.sleep(0.2)
#         print("the queue is empty")
#
# if __name__ == "__main__":
#     queue = Queue()
#     total_items = 10
#
#     p1 = Producer("producer-1", queue)
#     p2 = Producer("producer-2", queue)
#     c = Consumer(queue, total_items)
#
#     p1.start()
#     p2.start()
#     p1.join()
#     p2.join()
#
#     c.start()
#     c.join()


#------------------------------------------------------------


# from multiprocessing import Process, Queue
# import time, random
#
# class Producer(Process):
#     def __init__(self, queue):
#         super().__init__()
#         self.queue = queue
#
#     def run(self):
#         for i in range(8):
#             item = random.randint(10, 99)
#             self.queue.put(item)
#             print(f"Process Producer : item {item} appended to queue {self.name}")
#             print(f"The size of queue is {self.queue.qsize()}")
#             time.sleep(random.uniform(0.2, 0.5))
#
# class Consumer(Process):
#     def __init__(self, queue):
#         super().__init__()
#         self.queue = queue
#
#     def run(self):
#         while True:
#             if self.queue.empty():
#                 print("the queue is empty")
#                 break
#             item = self.queue.get()
#             print(f"Process Consumer : item {item} popped from by {self.name}")
#             time.sleep(random.uniform(0.1, 0.3))
#
# if __name__ == "__main__":
#     q = Queue()
#
#     p = Producer(q)
#     c = Consumer(q)
#
#     p.start()
#     p.join()
#     c.start()
#     c.join()
