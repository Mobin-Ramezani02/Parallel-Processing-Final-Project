from multiprocessing import get_context, Process
import time

class MyProcess(Process):
    def __init__(self, number):
        super().__init__(name=f"MyProcess-{number}")
        self.number = number
        
    def run(self):
        def emit(s: str):
            if getattr(self, "q", None) is not None:
                self.q.put(s)
            else:
                print(s)

        emit(f"called run method by {self.name}")
        time.sleep(getattr(self, "delay", 0.1))


def run_process_question_5(scenario: str):
    ctx = get_context("spawn")   # سازگار با ویندوز
    q = ctx.Queue()

    if scenario == "1":
        n = 10
        processes = []
        for i in range(1, n + 1):
            p = MyProcess(i)
            p.q = q
            p.delay = 0.5
            p.start()
            processes.append(p)

        for p in processes:
            p.join()

        while not q.empty():
            print(q.get())

    elif scenario == "2":
        n = 5
        for i in range(1, n + 1):
            p = MyProcess(i)
            p.q = q
            p.delay = 0.1
            p.start()
            p.join()

        while not q.empty():
            print(q.get())

    elif scenario == "3":
        n = 5
        processes = []
        for i in range(1, n + 1):
            p = MyProcess(i)
            p.q = q
            p.delay = 0.1
            p.start()
            processes.append(p)

        for p in reversed(processes):
            p.join()

        while not q.empty():
            print(q.get())

    else:
        print("ورودی نامعتبر. فقط 1-3 مجاز است.")
