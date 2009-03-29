import os

from setuptools import setup
from setuptools import find_packages

def read(*rnames):
    return open(os.path.join(os.path.dirname(__file__), *rnames)).read()

setup(name = 'BasecampWrapper',
      version = '0.2',
      description = "A wrapper around the Basecamp API.",
      long_description=(
        read('README.txt')
        + '\n\n' +
        read('CHANGES.txt')
        ),
      keywords = 'Basecamp API XML ElementTree',
      author = 'stj',
      author_email = 'stefan (at) tjarks (dot) de',
      url = 'http://github.com/stj/basecampreporting/tree/master',
      license = 'MIT',
      classifiers = [
        'Development Status :: 4 - Beta',
        'Intended Audience :: Developers',
        'License :: OSI Approved :: MIT License',
        'Programming Language :: Python',
        'Natural Language :: English',
        'Operating System :: OS Independent',
	'Topic :: Internet :: WWW/HTTP',
	'Topic :: Office/Business :: Groupware',
	'Topic :: Office/Business :: Scheduling',
        'Topic :: Software Development :: Libraries :: Python Modules',
        ],
      packages = find_packages('src'),
      package_dir = {'':'src'},
      package_data = {
        '': ['*.txt'],
        },
      namespace_packages=['basecamp'],
      include_package_data = True,
      zip_safe = False,
      install_requires = [
          'setuptools',
          ],
      )
