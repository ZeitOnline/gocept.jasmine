# This should be only one line. If it must be multi-line, indent the second
# line onwards to keep the PKG-INFO file format intact.
"""Jasmine integration for selenium.
"""

from setuptools import setup, find_packages


setup(
    name='gocept.jasmine',
    version='0.7.dev0',

    install_requires=[
        'fanstatic >= 1.0',
        'gocept.selenium>=2.0.0b4',
        'jasmine-core',
        'plone.testing',
        'setuptools',
    ],

    extras_require={
        'test': [
        ],
    },

    entry_points={
        'console_scripts': [
            # 'binary-name = gocept.jasmine.module:function'
        ],
        'fanstatic.libraries': [
            'gocept.jasmine = gocept.jasmine.resource:library',
        ],
    },

    author='Sebastian Wehrmann <sw@gocept.com>',
    author_email='sw@gocept.com',
    license='ZPL 2.1',
    url='https://github.com/gocept/gocept.jasmine',

    keywords='jasmine selenium test browser',
    classifiers="""\
License :: OSI Approved :: Zope Public License
Programming Language :: Python
Programming Language :: Python :: 2
Programming Language :: Python :: 2.6
Programming Language :: Python :: 2.7
Programming Language :: Python :: 2 :: Only
"""[:-1].split('\n'),
    description=__doc__.strip(),
    long_description='\n\n'.join(open(name).read() for name in (
        'README.rst',
        'HACKING.rst',
        'CHANGES.rst',
    )),

    namespace_packages=['gocept'],
    packages=find_packages('src'),
    package_dir={'': 'src'},
    include_package_data=True,
    zip_safe=False,
)
