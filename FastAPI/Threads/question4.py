import threading
import time
import os
import random


def run_thread_question_4(scenario: str):
    if scenario == "1":
        lock = threading.Lock()

        def thread_task(n, duration):
            with lock:
                print(f"---> Thread#{n} running, belonging to process ID {os.getpid()}")
                time.sleep(duration)
                print(f"---> Thread#{n} over")

        threads = []
        start_time = time.time()

        for i in range(1, 10):
            duration = random.uniform(0.5, 1.5)
            t = threading.Thread(target=thread_task, args=(i, duration))
            threads.append(t)
            t.start()

        for t in threads:
            t.join()

        print("End")
        print("--- %.4f seconds ---" % (time.time() - start_time))

    elif scenario == "2":
        lock = threading.Lock()

        def thread_task(n, duration):
            with lock:
                print(f"---> Thread#{n} running, belonging to process ID {os.getpid()}")
                time.sleep(duration)
                print(f"---> Thread#{n} over")

        start_time = time.time()

        for i in range(1, 10):
            duration = random.uniform(0.5, 1.5)
            t = threading.Thread(target=thread_task, args=(i, duration))
            t.start()
            t.join()

        print("End")
        print("--- %.4f seconds ---" % (time.time() - start_time))

    elif scenario == "3":
        lock = threading.Lock()

        def thread_task(n, duration):
            with lock:
                print(f"---> Thread#{n} running, belonging to process ID {os.getpid()}")
                time.sleep(duration)
                print(f"---> Thread#{n} over")

        threads = []
        start_time = time.time()

        for i in range(1, 10):
            t = threading.Thread(target=thread_task, args=(i, 1))
            threads.append(t)
            t.start()

        for t in threads:
            t.join()

        print("End")
        print("--- %.4f seconds ---" % (time.time() - start_time))

    else:
        print("ورودی نامعتبر. فقط 1-3 مجاز است.")
