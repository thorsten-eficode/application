# pylint: disable=F0001

"""
documentation
"""

from typing import Optional
from fastapi import FastAPI

app = FastAPI()

@app.get("/")
def read_root():
    """ docstring """
    return {"Hello": "World"}

@app.get("/items/{item_id}")
def read_item(item_id: int, query: Optional[str] = None):
    """ docstring """
    return {"item_id": item_id, "q": query}
