import os
import functools
import platform
from setuptools import setup, find_packages

_IN_PACKAGE_DIR = functools.partial(os.path.join, "config")

with open(_IN_PACKAGE_DIR("__version__.py")) as version_file:
    exec(version_file.read())

install_requires = ['six']  # optional: ["blinker==1.2"]
if platform.python_version() < '2.7':
    install_requires.append('unittest2')

setup(name="configs",
      classifiers=[
          "Development Status :: 0.1 - Dev",
          "Intended Audience :: Developers",
          "Programming Language :: Python :: 3.4",
      ],
      description="Configurations for Virta Health",
      license="Apache 2.0",
      author="Tony Tam",
      author_email="tony@virtahealth.com",
      version=__version__,
      packages=find_packages(),
      data_files=[],
      install_requires=install_requires,
      scripts=[],
      )
