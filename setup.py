import re

from setuptools import setup

with open('game/__init__.py', 'r') as fh:
    version = re.search(r'^__version__\s*=\s*[\'"]([^\'"]*)[\'"]', fh.read(), re.MULTILINE).group(1)


setup(
    name='life',
    version=version,
    description='Conway\'s Game of Life',
    author='Alexandre Cunha',
    author_email='ale@rcunha.net',
    license='MIT',
    packages=[
        'game'
    ],
    install_requires=[],
    dependency_links=[
    ],
    entry_points={'console_scripts': [
    ]},
    classifiers=[
        'Intended Audience :: Developers',
        'Natural Language :: English',
        'Operating System :: OS Independent',
        'Programming Language :: Python',
    ],
)
