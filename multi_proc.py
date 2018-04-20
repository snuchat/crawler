from multiprocessing import Pool
import time

start_time = time.time()

def fibo(n):
	if n == 0:
		return 0
	elif n == 1:
		return 1
	else:
		return fibo(n-1) + fibo(n-2)

def print_fibo(n):
	print(fibo(n))

num_list = [31, 32, 33, 34]

pool = Pool(processes=4)
pool.map(print_fibo, num_list)

print("--- %s seconds ---" % (time.time() - start_time))
