"""A setuptools based setup module.

See:
https://packaging.python.org/guides/distributing-packages-using-setuptools/
https://github.com/pypa/sampleproject
"""

from setuptools import setup, find_packages
import pathlib

here = pathlib.Path(__file__).parent.resolve()

long_description = (here / 'README.md').read_text(encoding='utf-8')

setup(
    name='ttconv', 
    version='1.0.0.dev1',
    description='Library for conversion of common timed text formats',
    long_description=long_description,
    long_description_content_type='text/markdown',
    url='https://github.com/sandlow/ttconv',
    author='Sandflow Consulting LLC',
    author_email='pal@sandflow.com',
    classifiers=[
        'Development Status :: 1 - Planning',
        'Intended Audience :: Developers',
        'Topic :: Software Development :: Build Tools',
        'Environment :: Console',
        'License :: OSI Approved :: BSD License',
        'Programming Language :: Python :: 3.7',
        'Programming Language :: Python :: 3.8',
        'Programming Language :: Python :: 3 :: Only',
        'Topic :: Multimedia'
    ],
    keywords='ttml, timed text, captions, subtitles, imsc, scc, srt, webvtt, smpte-tt, conversion',

    package_dir={'ttconv': 'src/main/python'}, 

    packages=find_packages(where='src/main/python'),

    python_requires='>=3.7, <4',

    project_urls={
        'Bug Reports': 'https://github.com/sandflow/ttconv/issues',
        'Source': 'https://github.com/sandflow/ttconv',
    },
)