# from multiprocessing import Pool
#
# def square(n):
#     return n * n
#
# if __name__ == "__main__":
#     numbers = list(range(100))
#     with Pool(processes=8) as pool:
#         result = pool.map(square, numbers)
#     print("Pool:", result)

#------------------------------------------------------------

# from multiprocessing import Pool
#
# def square(n):
#     return n * n
#
# if __name__ == "__main__":
#     numbers = list(range(100))
#     with Pool(processes=8) as pool:
#         async_results = [pool.apply_async(square, (num,)) for num in numbers]
#         result = [res.get() for res in async_results]
#     print("Pool:", result)


#------------------------------------------------------------

# from multiprocessing import Pool
#
# def square(n):
#     return n * n
#
# if __name__ == "__main__":
#     numbers = list(range(100))
#     with Pool(processes=8) as pool:
#         result = list(pool.imap(square, numbers))
#     print("Pool:", result)
