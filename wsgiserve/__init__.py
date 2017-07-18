import logging
import argparse
import plaster
import hupper

logger = logging.getLogger(__name__)


class Command(object):
    """command of wsgiserve"""

    def __init__(self, config, reload):
        self.config = config
        self.reload = reload

    def setup_logging(self):
        """call setup_logging for self's config"""
        plaster.setup_logging(self.config)

    def setup_reloader(self):
        """setup reloader if reload option specified"""
        if self.reload:
            reloader = hupper.start_reloader("wsgiserve.main")
            reloader.watch_files([self.config])

    def get_wsgi_loader(self):
        """get wsgi loader from self's config"""
        loader = plaster.get_loader(self.config, protocols=["wsgi"])
        return loader

    def run(self):
        """run command"""
        self.setup_logging()
        self.setup_reloader()
        loader = self.get_wsgi_loader()
        self.run_wsgi(loader)

    def run_wsgi(self, loader):
        """serve wsgi app with loader"""
        app = loader.get_wsgi_app()
        server = loader.get_wsgi_server()
        server(app)


def setup_arguments(parser):
    """setup arguments for parser"""
    parser.add_argument("config",
                        help="A path to the configuration file")
    parser.add_argument("--reload", action="store_true",
                        help="Use auto-restart file monitor")


def main():
    """main procedure"""
    parser = argparse.ArgumentParser()
    setup_arguments(parser)
    args = parser.parse_args()
    command = Command(args.config, args.reload)
    command.run()
