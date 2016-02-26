from setuptools import setup, find_packages
import mplutils

setup(name = 'mplutils', 
      version = mplutils.__version__,
      description = '',
      url = '',
      author = mplutils.__author__,
      author_email = mplutils.__author_email__,
      license = 'MIT',
      packages = find_packages(),
      requires = ['numpy', 'matplotlib'],
      classifiers = ['Programming Language :: Python',
                     'Topic :: Scientific/Engineering :: Visualization',
                     'Development Status :: 2 - Pre-Alpha',
                     'License :: OSI Approved :: '
                     'MIT License'],
      zip_safe=True)
