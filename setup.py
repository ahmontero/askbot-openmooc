# Copyright 2012 Rooter. All rights reserved.
import fnmatch
from setuptools import setup, find_packages
import sys, os



def read(*rnames):
    return open(os.path.join(os.path.dirname(__file__), *rnames)).read()


def recursive_include(directory, patterns):
    result = []
    for root, dirs, files in os.walk(directory):
        child_root = root.replace(directory, '').lstrip('/')
        for pattern in patterns:
            result.extend([os.path.join(child_root, name)
                           for name in fnmatch.filter(files, pattern)])
    return result


version = '0.0'

setup(name='askbot-openmooc/',
      version=version,
      description=("Askbot openmooc integration (theme, saml2, tags api)"),
      long_description = long_description=(read('README') + '\n\n' + read('CHANGES')),,
      classifiers=[
        'Development Status :: 6 - Development',
        'Environment :: Web Environment',
        'Framework :: Django',
        'License :: OSI Approved :: BSD License',
        'Operating System :: OS Independent',
        'Programming Language :: Python',
      ],
      keywords='askbot openmoc',
      author='Rooter',
      author_email='',
      url='https://github.com/OpenMOOC/askbot-openmooc',
      license='Undecided',
      packages=find_packages('.'),
      include_package_data=True,
      zip_safe=False,
      install_requires=[
          'askbot==0.7.43',
          'djangosaml2>=0.5.0',
          'python-memcached',
      ],
      entry_points="""
      # -*- Entry points: -*-
      """,
      )