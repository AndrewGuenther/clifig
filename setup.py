from setuptools import setup

setup(name='clifig',
      version='0.1',
      description='A simple prompt to modify config files.',
      long_description='A command line utility that wraps a ConfigParser. Pretty simple, but can be useful if you want to "hide" a config file from a user.',
      keywords='ConfigParser command-line cli config configuration conf',
      classifiers=['License :: OSI Approved :: MIT License',
                   'Development Status :: 3 - Alpha',
                   'Operating System :: OS Independent',
                   'Topic :: Utilities'],
      url='https://github.com/andrewguenther/clifig',
      author='Andrew Guenther',
      author_email='guenther.andrew.j@gmail.com',
      license='MIT',
      packages=['clifig'],
      scripts=['bin/clifig']
     )
