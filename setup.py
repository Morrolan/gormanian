from distutils.core import setup
setup(
    name = 'gormanian',
    packages = ['gormanian'],
    version = '0.1',
    license='MIT',
    description = 'A simple library to convert a datetime date to use the superior Gormanian Calendar',
    author = 'Ian Havelock',
    author_email = 'ian@morrolan.com',
    url = 'https://github.com/morrolan/gormanian',
    download_url = 'https://github.com/user/reponame/archive/v_01.tar.gz',    # I explain this later on
    keywords = ['Gormanian', 'Gormanuary', 'Dave Gorman'],
    install_requires=[            # I get to this in a second
        'validators',
        'beautifulsoup4',
    ],
    classifiers=[
        'Development Status :: 3 - Alpha',
        'Intended Audience :: Developers',
        'Topic :: Software Development :: Build Tools',
        'License :: OSI Approved :: MIT License',
        'Programming Language :: Python :: 3.6',
        'Programming Language :: Python :: 3.7',
        'Programming Language :: Python :: 3.8',
        'Programming Language :: Python :: 3.9',
    ],
)