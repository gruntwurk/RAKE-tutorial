from setuptools import setup, find_packages

setup(
    name="RAKE",
    version="0.1.0",
    packages=find_packages(exclude=["tests"]),
    include_package_data=True,
    zip_safe=False
)
