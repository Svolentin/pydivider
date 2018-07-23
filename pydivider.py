#!/usr/bin/env python3

from aiohttp import web


async def handle(request):
    a, b = request.rel_url.query['a'], request.rel_url.query['b']
    return web.Response(text=str(float(a) / float(b)))

app = web.Application()
app.add_routes([web.get('/', handle)])

web.run_app(app, port=9099)
