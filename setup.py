from setuptools import setup, find_packages

setup(
    name='my_library',
    version='0.1',
    packages=find_packages(where='src'),
    package_dir={'': 'src'},
    install_requires=[
        'pandas>=1.0.0',
        'sklearn>=0.24.0',
    ],
)