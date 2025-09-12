# Processes/question3.py

from multiprocessing import Process, current_process, get_context
import time

def foo(q=None, scenario=None):
    name = current_process().name
    # delay مطابق هر سناریو
    delay = 0.2 if scenario == "1" else 0.3

    # ارسال خروجی‌ها به صف (برای UI) یا چاپ مستقیم
    def emit(s: str):
        if q is not None:
            q.put(s)
        else:
            print(s)

    emit(f"Starting {name}")

    if name == "background_process":
        rng = range(5)         # 0..4
    else:
        rng = range(5, 10)     # 5..9

    for i in rng:
        emit(f"---> {i}")
        time.sleep(delay)

    emit(f"Exiting {name}")

def run_process_question_3(scenario: str):
    ctx = get_context("spawn")
    q = ctx.Queue()

    if scenario == "1":
        # فقط NO_background_process (non-daemon) — start سپس join
        NO_background_process = ctx.Process(name="NO_background_process", target=foo, args=(q, scenario))
        NO_background_process.daemon = False
        NO_background_process.start()
        NO_background_process.join()

    elif scenario == "2":
        # هر دو همزمان — هر دو start سپس هر دو join
        background_process = ctx.Process(name="background_process", target=foo, args=(q, scenario))
        background_process.daemon = True

        NO_background_process = ctx.Process(name="NO_background_process", target=foo, args=(q, scenario))
        NO_background_process.daemon = False

        background_process.start()
        NO_background_process.start()

        background_process.join()
        NO_background_process.join()

    elif scenario == "3":
        # ترتیبی — اول background بعد NO_background (هرکدام start سپس join)
        background_process = ctx.Process(name="background_process", target=foo, args=(q, scenario))
        background_process.daemon = True
        background_process.start()
        background_process.join()

        NO_background_process = ctx.Process(name="NO_background_process", target=foo, args=(q, scenario))
        NO_background_process.daemon = False
        NO_background_process.start()
        NO_background_process.join()

    else:
        print("ورودی نامعتبر. فقط 1-3 مجاز است.")
        return

    # والد چاپ می‌کند تا run_and_capture ببیند
    while not q.empty():
        print(q.get())
