from fastapi import FastAPI, Body
from gemini_client import get_answer_from_gemini
from db import Base, engine
from contextlib import asynccontextmanager

@asynccontextmanager
async def lifespan(app: FastAPI):
    Base.metadata.create_all(engine)
    print("все таблицы созданы")
    yield


app = FastAPI(lifespan=lifespan)

@app.get("/requests")
def get_my_requests():
    return "HellO"
@app.post("/requests")
def send_prompt(
        prompt: str = Body(embed=True)):
    answer = get_answer_from_gemini(prompt)
    return {"answer": answer}
