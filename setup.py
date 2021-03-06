from setuptools import setup

with open("README.md", "r") as fh:
    long_description = fh.read()

setup(
    name='gormanian',
    packages=['gormanian'],
    version='0.0.7',
    license='MIT',
    description='A simple library to convert a datetime date to use the superior Gormanian Calendar.',
    long_description=long_description,
    long_description_content_type="text/markdown",
    author='Ian Havelock',
    author_email='ian@morrolan.com',
    url='https://github.com/Morrolan/gormanian',
    download_url='https://github.com/Morrolan/gormanian/archive/v0.0.1.tar.gz',
    keywords=['Gormanian', 'Gormanuary', 'Dave Gorman'],
    install_requires=[],
    classifiers=[
        'Development Status :: 3 - Alpha',
        'Intended Audience :: Developers',
        'Intended Audience :: Education',
        'Intended Audience :: Information Technology',
        'Topic :: Software Development :: Build Tools',
        'Topic :: Software Development :: Libraries :: Python Modules',
        'Topic :: Software Development :: Localization',
        'License :: OSI Approved :: MIT License',
        'Programming Language :: Python :: 3.6',
        'Programming Language :: Python :: 3.7',
        'Programming Language :: Python :: 3.8',
        'Programming Language :: Python :: 3.9',
    ],
)
