import os

from setuptools import setup

here = os.path.abspath(os.path.dirname(__file__))
README = open(os.path.join(here, 'README.md'), "r").read()

setup(name='edo_fabric',
      version='0.1',
      description='Remote script engine',
      long_description=README,
      license = "MIT",
      author='edo',
      author_email="service@everydo.com",
      url="http://everydo.com/",
      keywords='Everydo rse remote script engine',
      packages=['edo_fabric'],
      package_dir={'edo_fabric': 'edo_fabric'},
      include_package_data=True,
      zip_safe=False,
      install_requires=['edo_client', 'fabric2'],
      classifiers = [
          'Development Status :: 4 - Beta',
          'Environment :: Web Environment',
          'Intended Audience :: Developers',
          'Programming Language :: Python',
          'Operating System :: OS Independent'
          ]
    )
