from setuptools import setup, find_packages


setup(
    name="dcc-utils",
    version="0.0.2",
    url="https://github.com/astagi/dcc-utils",
    install_requires=[],
    description="DCC Utils for Python",
    long_description=open("README.rst").read(),
    license="MIT",
    author="Andrea Stagi",
    author_email="stagi.andrea@gmail.com",
    packages=find_packages(),
    classifiers=[
        "Environment :: Web Environment",
        "Framework :: Django",
        "Intended Audience :: Developers",
        "Programming Language :: Python",
        "Programming Language :: Python :: 3",
    ],
)
