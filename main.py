from fastapi import FastAPI, Request
from fastapi.responses import HTMLResponse
from fastapi.staticfiles import StaticFiles
from fastapi.templating import Jinja2Templates

app = FastAPI()

# Montar carpeta de archivos estáticos (imágenes, CSS, música)
app.mount("/static", StaticFiles(directory="static"), name="static")

# Configurar carpeta de plantillas HTML
templates = Jinja2Templates(directory="templates")

# Ruta principal
@app.get("/", response_class=HTMLResponse)
async def mostrar_pagina(request: Request):
    return templates.TemplateResponse("index.html", {"request": request})