#!/usr/bin/env python3

from japronto import Application


def handle(request):
    try:
        a, b = request.query['a'], request.query['b']
    except:
        return request.Response(text=str(''))
    return request.Response(text=str(float(a)/float(b))) if a and b else request.Response(text=str(''))


app = Application()
app.router.add_route('/', handle)
app.run(debug=False, port=9099)
