# import threading
# import logging
# import time
# import random
#
# logging.basicConfig(level=logging.INFO, format="%(asctime)s %(threadName)-17s %(levelname)-8s %(message)s")
#
# item = 0
# semaphore = threading.Semaphore(0)
#
# def consumer():
#     global item
#     logging.info('Consumer is waiting')
#     semaphore.acquire()
#     logging.info('Consumer notify: item number {}'.format(item))
#
#
# def producer():
#     global item
#     time.sleep(1.5)
#     item = random.randint(100, 1000)
#     logging.info('Producer notify: item number {}'.format(item))
#     semaphore.release()
#
#
# for i in range(10):
#     t1 = threading.Thread(target=consumer, name=f"Thread-{2 * i + 1}")
#     t2 = threading.Thread(target=producer, name=f"Thread-{2 * i + 2}")
#
#     t1.start()
#     t2.start()
#
#     t1.join()
#     t2.join()


#---------------------------------------------------------------------------------------------


# import threading
# import logging
# import time
# import random
#
# logging.basicConfig(level=logging.INFO, format="%(asctime)s %(threadName)-17s %(levelname)-8s %(message)s")
#
# item = 0
# semaphore = threading.Semaphore(0)
#
# def consumer():
#     global item
#     logging.info('Consumer is waiting')
#     semaphore.acquire()
#     logging.info('Consumer notify: item number {}'.format(item))
#
# def producer():
#     global item
#     time.sleep(1.5)
#     item = random.randint(100, 1000)
#     logging.info('Producer notify: item number {}'.format(item))
#     semaphore.release()
#
# threads = []
#
# for i in range(10):
#     t1 = threading.Thread(target=consumer, name=f"Thread-{2 * i + 1}")
#     t2 = threading.Thread(target=producer, name=f"Thread-{2 * i + 2}")
#     threads.extend([t1, t2])
#
# for t in threads:
#     t.start()
#
# for t in threads:
#     t.join()


#---------------------------------------------------------------------------------------------


# import threading
# import logging
# import time
# import random
#
# logging.basicConfig(level=logging.INFO, format="%(asctime)s %(threadName)-17s %(levelname)-8s %(message)s")
#
# item = 0
# semaphore = threading.Semaphore(0)
#
# def consumer():
#     global item
#     logging.info('Consumer is waiting')
#     semaphore.acquire()
#     logging.info('Consumer notify: item number {}'.format(item))
#
# def producer():
#     global item
#     time.sleep(1.5)
#     item = random.randint(100, 1000)
#     logging.info('Producer notify: item number {}'.format(item))
#     semaphore.release()
#
# for i in range(10):
#     t1 = threading.Thread(target=consumer, name=f"Thread-{2 * i + 1}")
#     t2 = threading.Thread(target=producer, name=f"Thread-{2 * i + 2}")
#     t1.start()
#     t2.start()
#
