from setuptools import setup, find_packages


def read(filename):
    try:
        with open(filename) as f:
            return f.read()
    except Exception:
        return ""


__author__ = 'Atsushi Odagiri'
__author_email__ = 'aodagx@gmail.com'

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
    author=__author__,
    author_email=__author_email__,
    license="MIT",
    url="https://github.com/aodag/wsgiserve",
    description="a command to run wsgi application defined paste deploy configuration.",
    long_description=read("README.rst") + "\n" + read("Changes.rst"),
    packages=find_packages(exclude=["tests", "example"]),
    install_requires=requires,
    tests_require=tests_require,
    extras_require={
        "testing": tests_require,
    },
    setup_requires=[
        "setuptools-scm",
    ],
    use_scm_version=True,
    entry_points=points,
)
