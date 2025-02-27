from fastapi import FastAPI, Request
from fastapi.responses import HTMLResponse
from fastapi.staticfiles import StaticFiles
from fastapi.templating import Jinja2Templates

app = FastAPI()

app.mount("/static", StaticFiles(directory="static"), name="static")


templates = Jinja2Templates(directory="templates")


@app.get("/items/{id}", response_class=HTMLResponse)
async def read_item(request: Request, id: str):
    return templates.TemplateResponse(
        request=request, name="item.html", context={"id": id}
    )

@app.get("/items/add/{id}", response_class=HTMLResponse)
async def add_item1(request: Request, id: str):
    newid = int(id) + 1
    return templates.TemplateResponse(
        request=request, name="item.html", context={"id": newid}
    )

@app.post("/items/{id}", response_class=HTMLResponse)
async def add_item2(request: Request, id: str):
    new_id = int(id) + 1
    return templates.TemplateResponse(
        request=request, name="item.html", context={"id": new_id}
    )

