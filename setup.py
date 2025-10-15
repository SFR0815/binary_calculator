"""Setup configuration for binary_calculator package."""

from setuptools import setup, find_packages
import pathlib

# Read the README file
here = pathlib.Path(__file__).parent.resolve()
long_description = (here / 'README.md').read_text(encoding='utf-8')

setup(
    name='binary_calculator',
    version='1.0.0',
    description='Pure binary arithmetic operations without decimal conversion',
    long_description=long_description,
    long_description_content_type='text/markdown',
    url='https://github.com/SFR0815/binary_calculator',
    author='SFR0815',
    author_email='',
    classifiers=[
        'Development Status :: 5 - Production/Stable',
        'Intended Audience :: Education',
        'Intended Audience :: Developers',
        'Topic :: Software Development :: Libraries :: Python Modules',
        'Topic :: Education',
        'Topic :: Scientific/Engineering :: Mathematics',
        'License :: OSI Approved :: MIT License',
        'Programming Language :: Python :: 3',
        'Programming Language :: Python :: 3.7',
        'Programming Language :: Python :: 3.8',
        'Programming Language :: Python :: 3.9',
        'Programming Language :: Python :: 3.10',
        'Programming Language :: Python :: 3.11',
        'Programming Language :: Python :: 3.12',
        'Programming Language :: Python :: 3.13',
        'Programming Language :: Python :: 3 :: Only',
    ],
    keywords='binary, arithmetic, calculator, education, algorithms',
    packages=find_packages(exclude=['tests', 'docs', 'examples']),
    python_requires='>=3.7',
    install_requires=[],
    extras_require={
        'docs': [
            'mkdocs>=1.5.0',
            'mkdocs-material>=9.0.0',
            'pymdown-extensions>=10.0.0',
        ],
        'dev': [
            'mkdocs>=1.5.0',
            'mkdocs-material>=9.0.0',
            'pymdown-extensions>=10.0.0',
        ],
    },
    entry_points={
        'console_scripts': [
            'binary-calc-examples=examples.example:main',
        ],
    },
    project_urls={
        'Bug Reports': 'https://github.com/SFR0815/binary_calculator/issues',
        'Source': 'https://github.com/SFR0815/binary_calculator',
        'Documentation': 'https://SFR0815.github.io/binary_calculator',
    },
)

