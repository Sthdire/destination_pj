import time
from threading import Thread

from fastapi import FastAPI
from starlette.requests import Request
from starlette.staticfiles import StaticFiles
from starlette.templating import Jinja2Templates

from doc_save import save_db_values
from init import app, UV
from main import main_bot
from matplot import graf_img

templates = Jinja2Templates(directory="templates")
app.mount('/static', StaticFiles(directory='static'), name='static')


@app.get("/")
async def main(request: Request):
    return templates.TemplateResponse('index.html', {'request': request})


def run_app():
    UV.run(app)


def autoupdate():
    while True:
        save_db_values()
        graf_img()
        time.sleep(60)
    pass


if __name__ == '__main__':
    Thread(target=autoupdate).start()
    Thread(target=run_app).start()
    Thread(target=main_bot).start()

