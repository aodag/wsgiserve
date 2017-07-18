from setuptools import setup, find_packages

__author__ = 'Atsushi Odagiri'
__version__ = '0.1'

requires = [
    "plaster",
    "plaster_pastedeploy",
    "hupper",
]

tests_require = [
    "waitress",
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
    tests_require=tests_require,
    extras_require={
        "testing": tests_require,
    },
    entry_points=points,
)
