from aiohttp import web
from datetime import datetime
from aiohttp.web_request import Request
from aiohttp.web_response import Response

routes = web.RouteTableDef()


@routes.get('/time')  # A
async def time(request: Request) -> Response:
    today = datetime.today()

    result = {
        'month': today.month,
        'day': today.day,
        'time': str(today.time())
    }

    return web.json_response(result)  # B


app = web.Application()  # C
app.add_routes(routes)
web.run_app(app)
