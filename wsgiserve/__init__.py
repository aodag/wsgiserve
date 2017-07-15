import argparse
import plaster
import hupper


def main():
    parser = argparse.ArgumentParser()
    parser.add_argument("config")
    parser.add_argument("--reload", action="store_true")
    args = parser.parse_args()
    if args.reload:
        reloader = hupper.start_reloader("wsgiserve.main")
        reloader.watch_files([args.config])

    loader = plaster.get_loader(args.config, protocols=["wsgi"])
    app = loader.get_wsgi_app()
    server = loader.get_wsgi_server()
    server(app)
