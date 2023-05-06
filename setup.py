from setuptools import setup

setup(
    name='myproject',
    version='1.0',
    description='My project description',
    author='My Name',
    author_email='myname@example.com',
    packages=['myproject'],
    install_requires=[
        'numpy==1.19.5',
        'pandas==1.2.4',
        'matplotlib==3.4.2',
    ],
)
