import logging


logger = logging.getLogger(__name__)


class Application:
    def __init__(self, message):
        self.message = message

    def __call__(self, environ, start_response):
        logger.debug("accessed")
        start_response(
            "200 OK",
            [('Content-type', 'text/plain;charset=utf8')])
        return [self.message.encode('utf-8')]


def main(global_conf, **app_conf):
    logger.debug("app_conf %s", app_conf)
    app = Application(app_conf["message"])
    return app
