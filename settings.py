from starlette.staticfiles import StaticFiles
from starlette.templating import Jinja2Templates

from init import app

templates = Jinja2Templates(directory="templates")
app.mount('/static', StaticFiles(directory='static'), name='static')