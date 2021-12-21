from setuptools import setup


setup(
    name="dcc-utils",
    version="0.2.0",
    url="https://github.com/italia/dcc-utils",
    install_requires=[
        "base45==0.4.1",
        "cbor2==5.4.1",
        "cose==0.9.dev8",
        "panzi-json-logic==1.0.1",
        "Pillow==8.3.1",
        "pyzbar==0.1.8",
        "typing-extensions==3.10.0.0",
    ],
    description="DCC utils for Python",
    long_description=open("README.rst").read(),
    license="MIT",
    author="Andrea Stagi",
    author_email="stagi.andrea@gmail.com",
    packages=["dcc_utils"],
    classifiers=[
        "Intended Audience :: Developers",
        "Programming Language :: Python",
        "Programming Language :: Python :: 3",
    ],
)
