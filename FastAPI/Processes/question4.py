from multiprocessing import get_context
import time

def foo(q=None, scenario=None):
    # مستقیماً مثل کدهای خودت چاپ می‌کنیم، فقط اگر q هست به صف می‌ریزیم
    if q is None:
        print("Starting function")
    else:
        q.put("Starting function")

    if scenario == "1":
        # سناریوی 1: یک sleep طولانی
        time.sleep(5)

    elif scenario == "2":
        # سناریوی 2: حلقه 10تایی با تاخیر 0.5
        for i in range(10):
            line = f"--> {i}"
            if q is None:
                print(line)
            else:
                q.put(line)
            time.sleep(0.5)

    elif scenario == "3":
        # سناریوی 3: حلقه 5تایی با تاخیر 1
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
        # ----------------- دقیقاً به ترتیب سناریو 1 -----------------
        p = ctx.Process(target=foo, args=(q, scenario))

        print("Process before execution:", p, p.is_alive())
        p.start()
        print("Process running:", p, p.is_alive())

        time.sleep(1)  # خیلی سریع terminate
        p.terminate()
        print("Process terminated:", p, p.is_alive())

        p.join()

        # اول خروجی‌های فرزند، سپس joined/exitcode (نزدیک به رفتار واقعی کنسول)
        while not q.empty():
            print(q.get())

        print("Process joined:", p, p.is_alive())
        print("Process exit code:", p.exitcode)

    elif scenario == "2":
        # ----------------- دقیقاً به ترتیب سناریو 2 -----------------
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
        # ----------------- دقیقاً به ترتیب سناریو 3 -----------------
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
