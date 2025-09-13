from multiprocessing import current_process, get_context
from multiprocessing import Process
import time, random

def myFunc(q=None, scenario=None):
    proc = current_process()
    start = f"Starting process name = {proc.name}"
    end = f"Exiting process name = {proc.name}"

    if q is None:
        print(start)
    else:
        q.put(start)

    if scenario == "2":
        time.sleep(random.uniform(0.05, 0.2))   # سناریوی 2: تاخیر تصادفی
    elif scenario == "3":
        time.sleep(0.2)                          # سناریوی 3: ترتیبی با 0.2
    else:
        time.sleep(0.5)                          # سناریوی 1: 0.5

    if q is None:
        print(end)
    else:
        q.put(end)

def run_process_question_2(scenario: str):
    ctx = get_context("spawn")
    q = ctx.Queue()
    procs = []

    if scenario in ("1", "2"):
        for i in range(5):
            p = ctx.Process(target=myFunc, name=f"Process-{i+1}", args=(q, scenario))
            procs.append(p)
            p.start()
        for p in procs:
            p.join()

    elif scenario == "3":
        for i in range(5):
            p = ctx.Process(target=myFunc, name=f"Process-{i+1}", args=(q, scenario))
            p.start()
            p.join()
    else:
        print("ورودی نامعتبر. فقط 1-3 مجاز است.")
        return

    while not q.empty():
        print(q.get())
