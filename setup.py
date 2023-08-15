from os.path import join
from setuptools import setup, find_packages


long_description = open("README.md").read() + open("CHANGES.md").read()


def get_version():
    with open(join("fernet_fields", "__init__.py")) as f:
        for line in f:
            if line.startswith("__version__ ="):
                return line.split("=")[1].strip().strip("\"'")


setup(
    name="django-fernet-fields-v2",
    version=get_version(),
    description="Fernet-encrypted model fields for Django",
    long_description=long_description,
    author="MichelML, ORCAS, Inc",
    author_email="michmoreau.l@gmail.com",
    url="https://github.com/MichelML/django-fernet-fields/",
    packages=find_packages(),
    install_requires=["Django>=3.2", "cryptography"],
    zip_safe=False,
)
