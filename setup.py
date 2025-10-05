from setuptools import setup, find_packages

setup(
    name="QtMusic",
    packages=find_packages(),
    install_requires=[
        "PyQt5>=5.14.0",
    ],
    python_requires=">=3.5"
)
