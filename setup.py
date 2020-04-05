import io
import os
import re

from setuptools import find_packages, setup

# allow setup.py to be run from any path
os.chdir(os.path.normpath(os.path.join(os.path.abspath(__file__), os.pardir)))


def read(filename):
    filename = os.path.join(os.path.dirname(__file__), filename)
    text_type = type(u"")
    with io.open(filename, mode="r", encoding='utf-8') as fd:
        return re.sub(text_type(r':[a-z]+:`~?(.*?)`'), text_type(r'``\1``'), fd.read())


setup(
    name='fluentcheck',
    version='0.2.0',
    packages=find_packages(),
    include_package_data=True,
    install_requires=[
        'pyyaml>=4.2b1',
    ],
    license='MIT License',
    description='Fluent assertions framework for Python',
    long_description=read("README.md"),
    long_description_content_type='text/markdown',
    url='https://github.com/csparpa/fluentcheck',
    author='Claudio Sparpaglione',
    author_email='csparpa@gmail.com',
    python_requires='>3.5.0',
    classifiers=[
        "License :: OSI Approved :: MIT License",
        "Programming Language :: Python :: 3 :: Only",
        "Natural Language :: English",
        "Operating System :: OS Independent",
        "Development Status :: 3 - Alpha",
        "Intended Audience :: Developers",
        "Topic :: Software Development :: Libraries"],
    keywords='check python fluent fluent-interface assertion-library assertions testing fluent-assertions fluentcheck',
    test_suite='fluentcheck.tests'
)
