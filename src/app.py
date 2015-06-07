__author__ = 'liuchang'

from tornado.web import RequestHandler, Application
import tornado
from tornado import gen
from tornado.options import define
import tornado.options

import os
from core import clan

class IndexHandler(RequestHandler):

    def get(self, *args, **kwargs):
        return self.render('index.html')

    @gen.coroutine
    def post(self, *args, **kwargs):
        kw = self.get_argument("kw", clans = None)
        res = yield clan.service.search(kw)
        self.render('index.html', clans = res)
        self.finish()

class ClanApplication(Application):
    def __init__(self):
        handlers = [
            (r'/', IndexHandler),
            (r'/clan', IndexHandler)
        ]

        settings = dict(
            template_path = os.path.join(os.path.dirname(__file__), "templates"),
            static_path = os.path.join(os.path.dirname(__file__), "static"),
            debug = True,
            title = 'Clan Of CCCCC'
        )
        super(ClanApplication, self).__init__(handlers, **settings)

def main():
    tornado.options.parse_command_line()
    app = ClanApplication()
    app.listen(8088)
    tornado.ioloop.IOLoop.current().start()

if __name__ == "__main__":
    main()