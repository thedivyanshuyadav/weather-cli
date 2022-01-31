import pathlib
from setuptools import setup

# The directory containing this file
HERE = pathlib.Path(__file__).parent

# The text of the README file
README = (HERE / "README.md").read_text()

# This call to setup() does all the work
setup(
    name="weather-cli",
    version="1.0.0",
    description="It gives the weather information of given city.",
    long_description=README,
    long_description_content_type="text/markdown",
    url="https://github.com/thedivyanshuyadav/weather-cli",
    author="Divyanshu Yadav",
    author_email="thedivyanshuyadav@gmail.com",
    classifiers=[
        "Programming Language :: Python :: 3.6",
        "Programming Language :: Python :: 3.7",
        "Programming Language :: Python :: 3.8",
    ],
    packages=["weather"],
    include_package_data=True,
    install_requires=["requests"],
    entry_points={
        "console_scripts": [
            "weather=weather.__main__:main",
        ]
    },
)