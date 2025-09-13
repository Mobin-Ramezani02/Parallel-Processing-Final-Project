from multiprocessing import get_context
import time

def foo(q=None, scenario=None):
    if q is None:
        print("Starting function")
    else:
        q.put("Starting function")

    if scenario == "1":
        time.sleep(5)

    elif scenario == "2":
        for i in range(10):
            line = f"--> {i}"
            if q is None:
                print(line)
            else:
                q.put(line)
            time.sleep(0.5)

    elif scenario == "3":
        for i in range(5):
            line = f"--> {i}"
            if q is None:
                print(line)
            else:
                q.put(line)
            time.sleep(1)

    if q is None:
        print("Finished function")
    else:
        q.put("Finished function")


def run_process_question_4(scenario: str):
    ctx = get_context("spawn")
    q = ctx.Queue()

    if scenario == "1":
        p = ctx.Process(target=foo, args=(q, scenario))

        print("Process before execution:", p, p.is_alive())
        p.start()
        print("Process running:", p, p.is_alive())

        time.sleep(1)  # خیلی سریع terminate
        p.terminate()
        print("Process terminated:", p, p.is_alive())

        p.join()

        while not q.empty():
            print(q.get())

        print("Process joined:", p, p.is_alive())
        print("Process exit code:", p.exitcode)

    elif scenario == "2":
        p = ctx.Process(target=foo, args=(q, scenario))

        print("Process before execution:", p, p.is_alive())
        p.start()
        print("Process running:", p, p.is_alive())

        time.sleep(2)  # اجازه بده چند iteration انجام بشه
        p.terminate()
        print("Process terminated:", p, p.is_alive())

        p.join()

        while not q.empty():
            print(q.get())

        print("Process joined:", p, p.is_alive())
        print("Process exit code:", p.exitcode)

    elif scenario == "3":
        p = ctx.Process(target=foo, args=(q, scenario))

        print("Process before execution:", p, p.is_alive())
        p.start()
        print("Process running:", p, p.is_alive())

        p.join()  # بدون terminate

        while not q.empty():
            print(q.get())

        print("Process joined:", p, p.is_alive())
        print("Process exit code:", p.exitcode)

    else:
        print("ورودی نامعتبر. فقط 1-3 مجاز است.")
