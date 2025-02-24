from typing import Union

from fastapi import FastAPI

app = FastAPI()


@app.get("/")
#def read_root():
 #   a = [1, 2, 3, 4]
  #  b = [5, 6, 7, 8]
   # # TODO a + b
    #result = []
    #for i in range(len(a)):
     #   result.append(a[i], b[i])
    #return {"Hello": result}
        
    #result = list(zip(a,b))    
    #return {"Hello": result}
    
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

    result = list(x+y for x, y in zip(a, b))
    return {"result": result}


@app.get("/items/{item_id}")
def read_item(item_id: int, q: Union[str, None] = None):
    return {"item_id": item_id, "q": q}
