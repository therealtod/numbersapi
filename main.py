import tornado.ioloop
import tornado.web
from tornado.web import URLSpec as Url
from handlers.aggregate_numbers import AggregateNumbersHandler

import logging

logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)

PORT = 8080


def make_app():
    return tornado.web.Application([
        Url(pattern=r"/aggregate",
            handler=AggregateNumbersHandler,
            name="aggregate"),
    ])


if __name__ == "__main__":
    logger.info(f"Starting the server, listening at port: {PORT}")
    app = make_app()
    app.listen(PORT)
    tornado.ioloop.IOLoop.current().start()
