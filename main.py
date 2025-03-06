from typing import Union
from fastapi import FastAPI
import random
import numpy as np
import time
import matplotlib.pyplot as plt
import requests
import csv
import os
from datetime import datetime

app = FastAPI()

N = 10**5

@app.get("/")
def read_root():
    a = [1, 2, 3, 4]
    b = [5, 6, 7, 8]

    result = []
    for i in range(len(a)): # zip(a, b)
        result.append(a[i] + b[i])
        
    return {"Hello": result}


@app.get("/two-dimensional-array") #a[0][1]
def two_dimensional_array():
    a = [
        [1, 2, 3],
        [4, 5, 6],
        [7, 8, 9]
    ]

    b = [
        [9, 8, 7],
        [6, 5, 4],
        [3, 2, 1]
    ]
    
    result = a + b
    return {"result": result}

@app.get("/add-large-arrays")
def add_large_arrays():
    array_creation_time, addition_time = add_arrays(N, gen_r_array_randint, plus_py)
    return {
        "array_creation_time": array_creation_time,
        "addition_time": addition_time
        }
    
@app.get("/add-large-arrays-choices")
def add_large_arrays_choices():
    array_creation_time, addition_time = add_arrays(N, gen_r_array_choices, plus_py)
    return {
        "array_creation_time": array_creation_time,
        "addition_time": addition_time
        }
    
@app.get("/add-large-arrays-numpy")
def add_large_arrays_numpy():
    array_creation_time, addition_time = add_arrays(N, gen_r_array_numpy, plus_numpy)
    return {
        "array_creation_time": array_creation_time,
        "addition_time": addition_time
        }

def gen_r_array_randint(N):
    a = [random.randint(0, 100) for _ in range(N)]
    b = [random.randint(0, 100) for _ in range(N)]
    return a,b

def gen_r_array_choices(N):
    a = random.choices(range(101), k=N)
    b = random.choices(range(101), k=N)
    return a,b

def gen_r_array_numpy(N):
    a = np.random.randint(1, 101, size=N)  # 1 이상 100 이하의 정수
    b = np.random.randint(1, 101, size=N)
    return a,b

def plus_py(a, b):
    result = []
    for x, y in zip(a, b):
        result.append(x + y)
    return result

def plus_numpy(a, b):
    return a + b

def add_arrays(N, fun, fun_plus):
    # 랜덤한 1차원 배열 2개 생성
    start_creation_time = time.time()
    a, b = fun(N)
    end_creation_time = time.time()
    
    # 실행 시간 측정 시작
    add_start_time = time.time()
    # 요소별 덧셈
    result = fun_plus(a, b)
     
    # 실행 시간 측정 종료
    add_end_time = time.time()
    
    # 수행 시간 리턴
    # 리턴값: 배열 생성 시간(array_creation_time)과 덧셈 수행(addition_time) 시간을 각각 리턴
    array_creation_time = end_creation_time - start_creation_time
    addition_time = add_end_time - add_start_time
    return array_creation_time, addition_time

@app.get("/items/{item_id}")
def read_item(item_id: int, q: Union[str, None] = None):
    return {"item_id": item_id, "q": q}

@app.get("/nginx_status")
def get_nginx_status():
    res = requests.get("http://localhost:8949/nginx_status")
    text = res.text

    # ac
    a_conn = text.split("\n")[0]
    aa_conn = a_conn.split(": ")
    ac = aa_conn[1].strip()

    # ahr
    b = text.split("\n")[2]
    bb = b.split()
    ahr = ['accepts', 'handled', 'requests']
    ahr_values = bb 
    ahr_result = dict(zip(ahr, ahr_values))

    # rww
    rww = text.split("\n")[3]
    rww_parts = rww.split() 
    rww_data = {rww_parts[i].strip(":"): rww_parts[i+1] for i in range(0, len(rww_parts), 2)}

    return {
        "ac": ac,
        "accepts": ahr_result["accepts"], 
        "handled": ahr_result["handled"],
        "requests": ahr_result["requests"],
        "Reading": rww_data["Reading"],
        "Writing": rww_data["Writing"],
        "Waiting": rww_data["Waiting"]
    }

def write_to_csv(filename, data):
    fieldnames = ["timestamp", "ac", "accepts", "handled", "requests", "Reading", "Writing", "Waiting"]

    if not os.path.exists(filename):
        with open(filename, mode='w', newline='') as file:
            writer = csv.DictWriter(file, fieldnames=fieldnames)
            writer.writeheader()

    timestamp = datetime.now().strftime("%Y-%m-%d %H:%M:%S")

    with open(filename, mode='a', newline='') as file:
        writer = csv.DictWriter(file, fieldnames=fieldnames)
        row = {
            "timestamp": timestamp,
            "ac": data["ac"],
            "accepts": data["accepts"],
            "handled": data["handled"],
            "requests": data["requests"],
            "Reading": data["Reading"],
            "Writing": data["Writing"],
            "Waiting": data["Waiting"]
        }
        writer.writerow(row)

def main():
    filename = "nginx_status_data.csv"
    while True:
        status_data = get_nginx_status()  
        write_to_csv(filename, status_data)  
        time.sleep(10)  

if __name__ == "__main__":
    main()
