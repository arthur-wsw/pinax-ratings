import codecs

from os import path
from setuptools import find_packages, setup


def read(*parts):
    filename = path.join(path.dirname(__file__), *parts)
    with codecs.open(filename, encoding="utf-8") as fp:
        return fp.read()

setup(
    author="Pinax Team",
    author_email="team@pinaxproject.com",
    description="a ratings app for Django",
    name="pinax-ratings",
    long_description=read("README.rst"),
    version="0.3.3",
    url="http://github.com/pinax/pinax-ratings/",
    license="MIT",
    packages=find_packages(),
    package_data={
        "pinax.ratings": [
            "static/pinax/ratings/img/*",
            "static/pinax/ratings/js/*",
            "templates/pinax/ratings/*"
        ]
    },
    test_suite="runtests.runtests",
    tests_require=[
    ],
    install_requires=[
        "django-user-accounts>=1.1",
    ],
    classifiers=[
        "Development Status :: 4 - Beta",
        "Environment :: Web Environment",
        "Framework :: Django",
        "Intended Audience :: Developers",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
        "Programming Language :: Python",
        "Programming Language :: Python :: 2",
        "Programming Language :: Python :: 3",
        "Topic :: Software Development :: Libraries :: Python Modules",
    ],
    zip_safe=False
)
