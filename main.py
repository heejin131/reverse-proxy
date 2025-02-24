from typing import Union

from fastapi import FastAPI

app = FastAPI()


@app.get("/")
def read_root():
    a = [1, 2, 3, 4]
    b = [5, 6, 7, 8]
    # TODO a + b
    result = []
    for x, y in zip(a, b):
        result.append(x + y)
  
    return {"Hello": result}

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

    result = []
    for row_a, row_b in zip(a, b):
        row_result = []
        for x, y in zip(row_a, row_b):
            row_result.append(x + y)
        result.append(row_result)

    return {"result": result}

@app.get("/add-large-arrays")
def add_large_arrays():
    N = 10**6  # 100만 개 요소

    # 랜덤한 1차원 배열 2개 생성
    a = [random.randint(0, 100) for _ in range(N)]
    b = [random.randint(0, 100) for _ in range(N)]
    # 실행 시간 측정 시작
    start_time = time.time()
    
    # 요소별 덧셈
    result = []
    for x, y in zip(a, b):
        result.append(x + y)
     
    # 실행 시간 측정 종료
    end_time = time.time()
    
    # 수행 시간 리턴
    return {"execution_time": end_time - start_time}

@app.get("/items/{item_id}")
def read_item(item_id: int, q: Union[str, None] = None):
    return {"item_id": item_id, "q": q}
