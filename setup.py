import os
from setuptools import setup, find_packages


def read(filename):
    return open(os.path.join(os.path.dirname(__file__), filename)).read()


setup(
    name='temp-mail',
    version='0.2',
    license='MIT',
    description='Wrapper for online service which provides '
                'temporary email address: https://temp-mail.org/',
    long_description=read('README.rst') + read('CHANGES.rst'),
    keywords='temporary temp mail email address wrapper api anon '
             'anonymous secure free disposable',
    url='https://github.com/saippuakauppias/temp-mail',
    author='Denis Veselov',
    author_email='progr.mail@gmail.com',
    include_package_data=True,
    packages=find_packages(),
    install_requires=['requests'],
    py_modules=['tempmail'],
    classifiers=[
        'Development Status :: 5 - Production/Stable',
        'Intended Audience :: Developers',
        'Operating System :: OS Independent',
        'Programming Language :: Python',
        'Programming Language :: Python :: 2.6',
        'Programming Language :: Python :: 2.7',
        'Topic :: Internet :: WWW/HTTP'
    ],
)
