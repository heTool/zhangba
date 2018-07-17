#!/usr/bin/env python3
# -*- coding: utf-8 -*-

__author__ = 'He Tao'

'''
async web application.
'''

import logging; logging.basicConfig(level=logging.INFO)

import asyncio, os, json, time
from datetime import datetime

from aiohttp import web

def index(request):
    return web.Response(body=b'<h1\>Awesome22\<\/h1\>')

@asyncio.coroutine
def init(loop):
    app=  web.Application(loop=loop)
    app.router.add_route('GET','/',index)
    srv=yield from loop.create_server(app.make_handler(),'127.0.0.1',9013)
    logging.info('server started ad http://127.0.0.1:9013')
    return srv

loop = asyncio.get_event_loop()
loop.run_until_complete(init(loop))
loop.run_forever()