from setuptools import setup, find_packages

__author__ = 'Atsushi Odagiri'
__version__ = '0.1'

requires = [
    "plaster",
    "plaster_pastedeploy",
    "hupper",
]

points = {
    "console_scripts": [
        "wsgiserve=wsgiserve:main",
    ],
}

setup(
    name="wsgiserve",
    version=__version__,
    author=__author__,
    packages=find_packages(),
    install_requires=requires,
    entry_points=points,
)
