from setuptools import setup
import os


def open_file(fname):
    return open(os.path.join(os.path.dirname(__file__), fname)).read()


setup(
    name="conv_curry_recommender",  # name of your package
    version="0.0.1",
    description="demo",
    author="Spiced Academy",
    author_email="foo@bar.com",
    packages=["conv_curry_recommender"],  # same as name
)