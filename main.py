from fastapi import FastAPI
from pydantic import BaseModel

app = FastAPI()

# Модель данных для POST
class Prompt(BaseModel):
    prompt: str

# Временная функция, чтобы Swagger не ломался
def get_answer_from_gemini(prompt: str) -> str:
    return f"Ты отправил: {prompt}"

@app.get("/requests")
def get_my_requests():
    return "Hello world"

@app.post("/requests")
def send_prompt(data: Prompt):
    answer = get_answer_from_gemini(data.prompt)
    return {"answer": answer}
