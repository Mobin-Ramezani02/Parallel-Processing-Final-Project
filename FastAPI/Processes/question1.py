import multiprocessing as mp
import time, random

def myFunc(n: int, scenario: str, q):
    q.put(f"calling myFunc from process n: {n}")
    for i in range(n):
        q.put(f"output from myFunc is :{i}")
        if scenario == "2":
            time.sleep(random.uniform(0.05, 0.2))

def run_process_question_1(scenario: str):
    ctx = mp.get_context("spawn")
    q = ctx.Queue()
    procs = []

    if scenario in ("1", "2"):
        for i in range(5):
            p = ctx.Process(target=myFunc, args=(i, scenario, q))
            procs.append(p)
            p.start()
        for p in procs:
            p.join()

    elif scenario == "3":
        for i in range(6):
            p = ctx.Process(target=myFunc, args=(i, scenario, q))
            p.start()
            p.join()
    else:
        print("ورودی نامعتبر. فقط 1-3 مجاز است.")
        return

    while not q.empty():
        print(q.get())
