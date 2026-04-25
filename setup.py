from setuptools import setup, find_packages


def readme():
  with open('README.md', 'r') as f:
    return f.read()


setup(
  name='ultimate-chesslib',
  version='0.0.2',
  author='IgorGrebenchikov',
  author_email='grebenchikov_igor@mail.ru',
  description='This is ultimate library to create your own chess simulator!',
  long_description=readme(),
  long_description_content_type='text/markdown',
  url='https://github.com/Salmon-bit/OOPChess',
  packages=find_packages(),
  install_requires=[],
  classifiers=[
    'Programming Language :: Python :: 3.14',
    'License :: OSI Approved :: MIT License',
    'Operating System :: OS Independent'
  ],
  keywords='games chess ',
  project_urls={
    'GitHub': 'https://github.com/Salmon-bit'
  },
  python_requires='>=3.10'
)