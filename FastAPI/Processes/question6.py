from multiprocessing import get_context, Process
import time, random

# ---------- سناریو 1 ----------
class Producer_S1(Process):
    def __init__(self, queue):
        super().__init__()
        self.queue = queue
        self.log_q = None
    def run(self):
        emit = (lambda s: self.log_q.put(s)) if self.log_q else print
        for _ in range(10):
            item = random.randint(0, 256)
            self.queue.put(item)
            emit(f"Process Producer : item {item} appended to queue {self.name}")
            emit(f"The size of queue is {self.queue.qsize()}")
            time.sleep(0.3)

class Consumer_S1(Process):
    def __init__(self, queue):
        super().__init__()
        self.queue = queue
        self.log_q = None
    def run(self):
        emit = (lambda s: self.log_q.put(s)) if self.log_q else print
        while True:
            if self.queue.empty():
                emit("the queue is empty")
                break
            time.sleep(0.2)
            item = self.queue.get()
            emit(f"Process Consumer : item {item} popped from by {self.name}")
            time.sleep(0.1)

# ---------- سناریو 2 ----------
class Producer_S2(Process):
    def __init__(self, name, queue):
        super().__init__(name=name)
        self.queue = queue
        self.log_q = None
    def run(self):
        emit = (lambda s: self.log_q.put(s)) if self.log_q else print
        for _ in range(5):
            item = random.randint(0, 300)
            self.queue.put(item)
            emit(f"Process Producer : item {item} appended to queue {self.name}")
            emit(f"The size of queue is {self.queue.qsize()}")
            time.sleep(0.2)

class Consumer_S2(Process):
    def __init__(self, queue, total_items):
        super().__init__()
        self.queue = queue
        self.total_items = total_items
        self.log_q = None
    def run(self):
        emit = (lambda s: self.log_q.put(s)) if self.log_q else print
        count = 0
        while count < self.total_items:
            if not self.queue.empty():
                item = self.queue.get()
                emit(f"Process Consumer : item {item} popped from by {self.name}")
                count += 1
                time.sleep(0.2)
        emit("the queue is empty")

# ---------- سناریو 3 ----------
class Producer_S3(Process):
    def __init__(self, queue):
        super().__init__()
        self.queue = queue
        self.log_q = None
    def run(self):
        emit = (lambda s: self.log_q.put(s)) if self.log_q else print
        for _ in range(8):
            item = random.randint(10, 99)
            self.queue.put(item)
            emit(f"Process Producer : item {item} appended to queue {self.name}")
            emit(f"The size of queue is {self.queue.qsize()}")
            time.sleep(random.uniform(0.2, 0.5))

class Consumer_S3(Process):
    def __init__(self, queue):
        super().__init__()
        self.queue = queue
        self.log_q = None
    def run(self):
        emit = (lambda s: self.log_q.put(s)) if self.log_q else print
        while True:
            if self.queue.empty():
                emit("the queue is empty")
                break
            item = self.queue.get()
            emit(f"Process Consumer : item {item} popped from by {self.name}")
            time.sleep(random.uniform(0.1, 0.3))

def run_process_question_6(scenario: str):
    ctx   = get_context("spawn")   
    dataQ = ctx.Queue()            # صف داده بین Producer/Consumer
    logQ  = ctx.Queue()            # صف لاگ برای برگرداندن خروجی به والد

    if scenario == "1":
        Producer = Producer_S1
        Consumer = Consumer_S1

        p = Producer(dataQ)
        p.log_q = logQ
        c = Consumer(dataQ)
        c.log_q = logQ

        p.start()
        c.start()
        p.join()
        c.join()

    elif scenario == "2":
        Producer = Producer_S2
        Consumer = Consumer_S2

        total_items = 10
        p1 = Producer("producer-1", dataQ); p1.log_q = logQ
        p2 = Producer("producer-2", dataQ); p2.log_q = logQ
        c  = Consumer(dataQ, total_items); c.log_q  = logQ

        p1.start(); p2.start()
        p1.join();  p2.join()

        c.start()
        c.join()

    elif scenario == "3":
        Producer = Producer_S3
        Consumer = Consumer_S3

        p = Producer(dataQ); p.log_q = logQ
        c = Consumer(dataQ); c.log_q = logQ

        p.start(); p.join()
        c.start(); c.join()

    else:
        print("ورودی نامعتبر. فقط 1-3 مجاز است.")
        return

    while not logQ.empty():
        print(logQ.get())

