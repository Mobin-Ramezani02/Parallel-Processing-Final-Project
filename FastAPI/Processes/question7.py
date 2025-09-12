from multiprocessing import get_context, current_process
from time import time
from datetime import datetime

def test_with_barrier(synchronizer, lock, log_q=None):
    name = current_process().name
    synchronizer.wait()
    now = time()
    line = f"process {name} - test_with_barrier ----> {datetime.fromtimestamp(now)}"
    if log_q is None:
        print(line)
    else:
        log_q.put(line)

def test_without_barrier(log_q=None):
    name = current_process().name
    now = time()
    line = f"process {name} - test_without_barrier ----> {datetime.fromtimestamp(now)}"
    if log_q is None:
        print(line)
    else:
        log_q.put(line)


def run_process_question_7(scenario: str):
    ctx = get_context("spawn")   # برای ویندوز
    log_q = ctx.Queue()

    if scenario == "1":
        # ----- سناریوی 1: فقط با Barrier -----
        synchronizer = ctx.Barrier(2)
        serializer   = ctx.Lock()

        p1 = ctx.Process(name='p1', target=test_with_barrier, args=(synchronizer, serializer, log_q))
        p2 = ctx.Process(name='p2', target=test_with_barrier, args=(synchronizer, serializer, log_q))

        p1.start()
        p2.start()
        p1.join()
        p2.join()

    elif scenario == "2":
        # ----- سناریوی 2: فقط بدون Barrier -----
        p3 = ctx.Process(name='p3', target=test_without_barrier, args=(log_q,))
        p4 = ctx.Process(name='p4', target=test_without_barrier, args=(log_q,))

        p3.start()
        p4.start()
        p3.join()
        p4.join()

    elif scenario == "3":
        # ----- سناریوی 3: هر دو حالت کنار هم -----
        barrier = ctx.Barrier(2)
        lock    = ctx.Lock()

        p1 = ctx.Process(name='p1', target=test_with_barrier, args=(barrier, lock, log_q))
        p2 = ctx.Process(name='p2', target=test_with_barrier, args=(barrier, lock, log_q))
        p3 = ctx.Process(name='p3', target=test_without_barrier, args=(log_q,))
        p4 = ctx.Process(name='p4', target=test_without_barrier, args=(log_q,))

        p1.start()
        p2.start()
        p3.start()
        p4.start()

        p1.join()
        p2.join()
        p3.join()
        p4.join()

    else:
        print("ورودی نامعتبر. فقط 1-3 مجاز است.")
        return

    # چاپ خروجی‌ها در والد تا UI ببیند
    while not log_q.empty():
        print(log_q.get())
