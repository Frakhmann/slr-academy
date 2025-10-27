from fastapi import FastAPI
from fastapi.staticfiles import StaticFiles
from fastapi.templating import Jinja2Templates
from app.routers import pages

app = FastAPI(title="SLR Academy")

# Подключаем статические файлы (css, изображения)
app.mount("/static", StaticFiles(directory="app/static"), name="static")

# Подключаем шаблоны
templates = Jinja2Templates(directory="app/templates")

# Подключаем роутеры
app.include_router(pages.router)

# Проверка доступности
@app.get("/health")
async def health_check():
    return {"status": "ok"}
