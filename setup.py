import setuptools

with open("README.md", "r") as fh:
    long_description = fh.read()

NAME = "anacondo"
AUTHOR_NAME, AUTHOR_EMAIL = "fongmanfong", "fongmanfong@gmail.com"
VERSION = "0.0.1"
DESCRIPTION = "Real estate investment analysis including financial analysis, risk and marginal simulations."

setuptools.setup(
    name=NAME,
    version="0.0.1",
    author=AUTHOR_NAME,
    author_email=AUTHOR_EMAIL,
    description=DESCRIPTION,
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/fongmanfong/anacondo",
    packages=setuptools.find_packages(),
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    python_requires='>=3.6',
)