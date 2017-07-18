import logging
import argparse
import plaster
import hupper

logger = logging.getLogger(__name__)


class Command(object):
    def __init__(self, config, reload):
        self.config = config
        self.reload = reload

    def setup_logging(self):
        plaster.setup_logging(self.config)

    def setup_reloader(self):
        if self.reload:
            reloader = hupper.start_reloader("wsgiserve.main")
            reloader.watch_files([self.config])

    def get_wsgi_loader(self):
        loader = plaster.get_loader(self.config, protocols=["wsgi"])
        return loader
    
    def run(self):
        self.setup_logging()
        self.setup_reloader()
        loader = self.get_wsgi_loader()
        self.run_wsgi(loader)
        
    def run_wsgi(self, loader):
        app = loader.get_wsgi_app()
        server = loader.get_wsgi_server()
        server(app)


def setup_arguments(parser):
    parser.add_argument("config",
                        help="A path to the configuration file")
    parser.add_argument("--reload", action="store_true",
                        help="Use auto-restart file monitor")


def main():
    parser = argparse.ArgumentParser()
    setup_arguments(parser)
    args = parser.parse_args()
    command = Command(args.config, args.reload)
    command.run()
