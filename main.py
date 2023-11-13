# This is a sample Python script.

# Press ⌃R to execute it or replace it with your code.
# Press Double ⇧ to search everywhere for classes, files, tool windows, actions, and settings.

from fastapi import FastAPI

from ecommerce.user import router as user_router

app = FastAPI(title="Ecommerce", version="0.0.1")

app.include_router(user_router.router)


