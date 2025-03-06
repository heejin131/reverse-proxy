import time

def square(x):
    return x**2

def double(x):
    return x*2

nums = [1,2,3,4,5]

def num_square(nums):
    # 리스트 각각의 값에 제곱을 하여 프린트
    start_time = time.time() 
    print([square(x) for x in nums])
    end_time = time.time()
    print(end_time - start_time)
    
def num_double(nums):
    # 리스트 각각의 값에 2 곱하여 프린트
    start_time = time.time() 
    print([double(x) for x in nums])
    end_time = time.time()
    print(end_time - start_time)

num_square(nums) 
num_double(nums) 

#num_cal(nums, square)
#num_cal(nums, double)
def num_cal(data, fun):
    start_time = time.time()
    print([fun(x) for x in data])
    end_time = time.time()
    print(end_time - start_time)
    
num_cal(nums, square)
num_cal(nums, double)
