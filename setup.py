import os
from setuptools import find_packages, setup

# allow setup.py to be run from any path
os.chdir(os.path.normpath(os.path.join(os.path.abspath(__file__), os.pardir)))

setup(
    name='fluentcheck',
    version='0.1.0',
    packages=find_packages(),
    include_package_data=True,
    install_requires=[
        'pyyaml>=4.2b1',
    ],
    license='MIT License',
    description='Fluent assertions framework for Python',
    url='https://github.com/csparpa/check',
    author='Claudio Sparpaglione',
    author_email='csparpa@gmail.com',
    python_requires='>3.5.0',
    classifiers=[
      "License :: OSI Approved :: MIT License",
      "Programming Language :: Python :: 2 :: Only",
      "Natural Language :: English",
      "Operating System :: OS Independent",
      "Development Status :: 3 - Alpha",
      "Intended Audience :: Developers",
      "Topic :: Software Development :: Libraries"],
    keywords='check python fluent fluent-interface assertion-library assertions testing fluent-assertions',
    test_suite='fluentcheck.tests'
)
