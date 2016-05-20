from setuptools import setup
# import codecs
# import os

# import falcor

# here = os.path.abspath(os.path.dirname(__file__))

# # Get the long description from the relevant file
# with codecs.open('README.rst', encoding='utf-8') as f:
#     long_description = f.read()

tests_require = [
    'pytest>=2.6.0',
    'pytest-cov>=1.7.0',
]

setup(
    name="falcor",
    version='0.0.1',

    description="",
    # long_description=long_description,

    # The project URL.
    url='https://github.com/canassa/falcor',

    # Author details
    author='Cesar Canassa',
    author_email='cesar@canassa.com',

    # Choose your license
    license='MIT',

    classifiers=[
        'Development Status :: 1 - Planning',

        # Who the project is intended for.
        'Intended Audience :: Developers',
        'Intended Audience :: System Administrators',
        'Topic :: Software Development :: Libraries',

        'License :: OSI Approved :: Apache Software License',

        # Supported Python versions.
        'Programming Language :: Python :: 3.5',
    ],
    tests_require=tests_require,
    extras_require={'test': tests_require},
    keywords='falcor',
    packages=['falcor'],
)
