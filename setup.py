from setuptools import setup, find_packages


setup(
    name='viacep',
    packages=['src'],
    version='1.0',
    py_modules=['main'],
    entry_points={
        'console_scripts':
        ['pycep = main:main']
    },
    install_requires=['requests', 'click']
)

print(find_packages())
