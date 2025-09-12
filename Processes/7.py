# from multiprocessing import Process, Barrier, Lock, current_process
# from time import time
# from datetime import datetime
#
# def test_with_barrier(synchronizer, lock):
#     name = current_process().name
#     synchronizer.wait()
#     now = time()
#     with lock:
#         print(f"process {name} - test_with_barrier ----> {datetime.fromtimestamp(now)}")
#
# if __name__ == "__main__":
#     synchronizer = Barrier(2)
#     serializer = Lock()
#
#     p1 = Process(name='p1', target=test_with_barrier, args=(synchronizer, serializer))
#     p2 = Process(name='p2', target=test_with_barrier, args=(synchronizer, serializer))
#
#     p1.start()
#     p2.start()
#     p1.join()
#     p2.join()



#------------------------------------------------------------


# from multiprocessing import Process, current_process
# from time import time
# from datetime import datetime
#
# def test_without_barrier():
#     name = current_process().name
#     now = time()
#     print(f"process {name} - test_without_barrier ----> {datetime.fromtimestamp(now)}")
#
# if __name__ == "__main__":
#     p3 = Process(name='p3', target=test_without_barrier)
#     p4 = Process(name='p4', target=test_without_barrier)
#
#     p3.start()
#     p4.start()
#     p3.join()
#     p4.join()


#------------------------------------------------------------


from multiprocessing import Process, Barrier, Lock, current_process
from time import time
from datetime import datetime

def test_with_barrier(sync, lock):
    name = current_process().name
    sync.wait()
    now = time()
    with lock:
        print(f"process {name} - test_with_barrier ----> {datetime.fromtimestamp(now)}")

def test_without_barrier():
    name = current_process().name
    now = time()
    print(f"process {name} - test_without_barrier ----> {datetime.fromtimestamp(now)}")

if __name__ == "__main__":
    barrier = Barrier(2)
    lock = Lock()

    p1 = Process(name='p1', target=test_with_barrier, args=(barrier, lock))
    p2 = Process(name='p2', target=test_with_barrier, args=(barrier, lock))
    p3 = Process(name='p3', target=test_without_barrier)
    p4 = Process(name='p4', target=test_without_barrier)

    p1.start()
    p2.start()
    p3.start()
    p4.start()

    p1.join()
    p2.join()
    p3.join()
    p4.join()
