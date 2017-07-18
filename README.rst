====================
wsgiserve
====================

``wsgiserve`` is a command to run wsgi application defined paste deploy configuration.

::

    usage: wsgiserve [-h] [--reload] config [config_vars [config_vars ...]]

    positional arguments:
    config       A path to the configuration file
    config_vars  Variables required by the config file.

    optional arguments:
    -h, --help   show this help message and exit
    --reload     Use auto-restart file monitor
