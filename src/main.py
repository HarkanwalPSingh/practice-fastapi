from fastapi import FastAPI

from src.routers import user_router, collection_router, book_router

app = FastAPI()

app.include_router(user_router.router)
app.include_router(collection_router.router)
app.include_router(book_router.router)

# @app.get("/")
# async def root():
#     return {"message": "Hello World"}
#
#
# @app.get("/hello/{name}")
# async def say_hello(name: str):
#     return {"message": f"Hello {name}"}
