import logging
import argparse
import plaster
import hupper

logger = logging.getLogger(__name__)


class Command(object):
    """command of wsgiserve"""

    def __init__(self, config, reload, config_vars=[]):
        self.config = config
        self.reload = reload
        self.config_vars = config_vars

    def get_defaults(self):
        """get default values from config_vars"""
        return dict(c.split("=", 1) for c in self.config_vars if "=" in c)

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
        defaults = self.get_defaults()
        self.run_wsgi(loader, defaults)

    def run_wsgi(self, loader, defaults):
        """serve wsgi app with loader"""
        app = loader.get_wsgi_app(defaults=defaults)
        server = loader.get_wsgi_server(defaults=defaults)
        server(app)


def setup_arguments(parser):
    """setup arguments for parser"""
    parser.add_argument("config",
                        help="A path to the configuration file")
    parser.add_argument("--reload", action="store_true",
                        help="Use auto-restart file monitor")
    parser.add_argument("config_vars", nargs="*",
                        help="Variables required by the config file.")


def main():
    """main procedure"""
    parser = argparse.ArgumentParser()
    setup_arguments(parser)
    args = parser.parse_args()
    command = Command(args.config, args.reload, args.config_vars)
    command.run()
