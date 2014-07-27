import re
from setuptools import setup, find_packages

def find_version(fname):
    """Attempts to find the version number in the file names fname.
    Raises RuntimeError if not found.
    """
    version = ''
    with open(fname, 'r') as fp:
        reg = re.compile(r'__version__ = [\'"]([^\'"]*)[\'"]')
        for line in fp:
            m = reg.match(line)
            if m:
                version = m.group(1)
                break
    if not version:
        raise RuntimeError('Cannot find version information')
    return version

def read(fname):
    with open(fname) as fp:
        content = fp.read()
    return content

__version__ = find_version("shelf_reader/__init__.py")

setup(
    name='shelf-reader',
    version=__version__,
    description='Make sure your collections are in call number order.',
    long_description=(read("README.md")),
    author='Austin Macdonald',
    author_email='asmacdo@gmail.com',
    url='https://github.com/asmacdo/shelf-reader',
    license=read("LICENSE.txt"),
    zip_safe=False,
    keywords='library barcode call number shelf collection',
    classifiers=[
        'Development Status :: 4 - Beta',
        'Intended Audience :: Developers',
        'License :: OSI Approved :: GNU General Public License v2 (GPLv2)',
        'Natural Language :: English',
        "Programming Language :: Python :: 2",
        'Programming Language :: Python :: 2.7',
        'Environment :: Console',
    ],

    entry_points={
        'console_scripts': ['shelf-reader = shelf_reader.shelf_reader:main']
    },
    packages=find_packages(),
    include_package_data=True,
    tests_require=['nose'],
)
