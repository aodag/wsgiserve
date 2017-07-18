from setuptools import setup, find_packages


def read(filename):
    try:
        with open(filename) as f:
            return f.read()
    except Exception:
        return ""


__author__ = 'Atsushi Odagiri'
__author_email__ = 'aodagx@gmail.com'
__version__ = '0.1'

requires = [
    "plaster",
    "plaster_pastedeploy",
    "hupper",
]

tests_require = [
    "pytest",
    "pytest-cov",
    "flake8",
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
    author_email=__author_email__,
    url="https://github.com/aodag/wsgiserve",
    description="a command to run wsgi application defined paste deploy configuration.",
    long_description=read("README.rst"),
    packages=find_packages(exclude=["tests", "example"]),
    install_requires=requires,
    tests_require=tests_require,
    extras_require={
        "testing": tests_require,
    },
    entry_points=points,
)
