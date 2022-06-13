from pathlib import Path
from setuptools import setup, find_packages
from hopenapi import VERSION


here = Path(__file__).parent.resolve()

long = (here / 'README.md').read_text(encoding='uf8')
short = long.split('\n')[1]


setup(
    name='hopenapi',
    version=str(VERSION),
    packages=find_packages(),
    description=short,
    long_description=long,
    long_description_content_type='text/markdown',
    url='https://github.com/HazelTheWitch/HOpenAPI',
    author='Hazel Rella',
    author_email='hazelrella11@gmail.com',
    classifiers=[
        'Development Status :: 3 - Alpha',
        'Framework :: AsyncIO',
        'Framework :: aiohttp',
        'License :: OSI Approved :: MIT License',
        'Intended Audience :: Developers',
        'Programming Language :: Python :: 3.10',
        'Programming Language :: Python :: 3 :: Only'
    ],
    keywords='openapi, aiohttp',
    python_requires='>=3.10, <4',
    install_requires=[
        'aiohttp'
    ]
)
