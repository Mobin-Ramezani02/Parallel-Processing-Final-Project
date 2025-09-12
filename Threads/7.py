# import threading
# import time
# import random
#
# barrier = threading.Barrier(3)
#
# def racer(name):
#     time.sleep(random.uniform(1, 3))
#     print(f"{name} reached the barrier at: {time.ctime()}")
#     barrier.wait()
#
# print("START RACE!!!!")
#
# names = ['Dewey', 'Huey', 'Louie']
# threads = []
#
# for name in names:
#     t = threading.Thread(target=racer, args=(name,))
#     threads.append(t)
#     t.start()
#
# for t in threads:
#     t.join()
#
# print("Race over!")


#---------------------------------------------------------------------------------------------------

# import threading
# import time
# import random
#
# barrier = threading.Barrier(3)
#
# def racer(name):
#     print(f"{name} reached the barrier at: {time.ctime()}")
#     barrier.wait()
#
# print("START RACE!!!!")
#
# names = ['Dewey', 'Huey', 'Louie']
# threads = []
#
# for name in names:
#     t = threading.Thread(target=racer, args=(name,))
#     threads.append(t)
#     t.start()
#
# for t in threads:
#     t.join()
#
# print("Race over!")


#---------------------------------------------------------------------------------------------------


# import threading
# import time
# import random
#
# barrier = threading.Barrier(3)
#
# def racer(name):
#     time.sleep(random.uniform(1, 3))
#     print(f"{name} reached the barrier at: {time.ctime()}")
#     barrier.wait()
#
# print("START RACE!!!!")
#
# names = ['Dewey', 'Huey', 'Louie']
#
# for name in names:
#     t = threading.Thread(target=racer, args=(name,))
#     t.start()
#
# time.sleep(5)
#
# print("Race over!")

