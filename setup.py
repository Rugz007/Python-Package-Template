from setuptools import setup,find_packages

setup(name='package',
      version='0.0.1',
      description='Template for creating a python package',
      packages=find_packages(include=['package', 'package.*']),
      author_email='mail@mail.com',
      zip_safe=False)
