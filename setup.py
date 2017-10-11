from distutils.core import setup

with open('README.md') as file:
    readme = file.read()

with open('requirements.txt') as file:
    install_requires = file.readlines()

setup(
    name='reloadcat',
    version='0.1',
    packages=['reloadcat'],
    install_requires=install_requires,
    url='',
    license='LICENSE.txt',
    description='',
    long_description=readme,
    author='Perry',
    author_email='perryism@gmail.com'
)

