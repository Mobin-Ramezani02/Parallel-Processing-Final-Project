from multiprocessing import get_context

def square(n):
    return n * n

def run_process_question_8(scenario: str):
    ctx = get_context("spawn")
    numbers = list(range(100))

    if scenario == "1":
        # map
        with ctx.Pool(processes=8) as pool:
            result = pool.map(square, numbers)
        print("Pool:", result)

    elif scenario == "2":
        # apply_async + get
        with ctx.Pool(processes=8) as pool:
            async_results = [pool.apply_async(square, (num,)) for num in numbers]
            result = [res.get() for res in async_results]
        print("Pool:", result)

    elif scenario == "3":
        # imap
        with ctx.Pool(processes=8) as pool:
            result = list(pool.imap(square, numbers))
        print("Pool:", result)

    else:
        print("ورودی نامعتبر. فقط 1-3 مجاز است.")
