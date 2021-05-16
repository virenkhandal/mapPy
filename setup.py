from setuptools import setup, find_packages

classifiers = [
  'Development Status :: 5 - Production/Stable',
  'Intended Audience :: Education',
  'Operating System :: Microsoft :: Windows :: Windows 10',
  'License :: OSI Approved :: MIT License',
  'Programming Language :: Python :: 3'
]

setup(
  name='mapPy',
  version='0.0.1',
  description='Map creator',
  long_description=open('README.txt').read() + '\n\n' + open('CHANGELOG.txt').read(),
  url='',  
  author='Viren Khandal',
  author_email='virenkhanda@berkeley.edu',
  license='MIT', 
  classifiers=classifiers,
  keywords='calculator', 
  packages=find_packages(),
  install_requires=[''] 
)