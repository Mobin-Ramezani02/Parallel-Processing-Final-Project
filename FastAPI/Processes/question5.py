from multiprocessing import get_context, Process
import time

class MyProcess(Process):
    def __init__(self, number):
        super().__init__(name=f"MyProcess-{number}")
        self.number = number
        # q و delay را بعد از ساخت در والد ست می‌کنیم تا امضای سازنده تغییر نکند

    def run(self):
        # ارسال خروجی به صف (در صورت وجود) یا چاپ مستقیم
        def emit(s: str):
            if getattr(self, "q", None) is not None:
                self.q.put(s)
            else:
                print(s)

        emit(f"called run method by {self.name}")
        time.sleep(getattr(self, "delay", 0.1))  # پیش‌فرض برای سناریوهای کوتاه


def run_process_question_5(scenario: str):
    ctx = get_context("spawn")   # سازگار با ویندوز
    q = ctx.Queue()

    if scenario == "1":
        # ----- سناریو 1: مثل کد اولت -----
        # n = 10 ، همه start سپس join ، delay = 0.5
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
        # ----- سناریو ۲: مثل کد دومت -----
        # n = 5 ، هرکدام start سپس بلافاصله join (ترتیبی)، delay = 0.1
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
        # ----- سناریو ۳: مثل کد سومت -----
        # n = 5 ، همه start و ذخیره در لیست؛ سپس join به صورت معکوس، delay = 0.1
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
