from setuptools import setup, find_packages

setup(
    name='message-passing-nn',
    version='1.1.1',
    packages=find_packages(exclude=["tests"]),
    url='https://github.com/kovanostra/message-passing-nn',
    download_url='',
    keywords=[''],
    license='MIT',
    author='Michail Kovanis',
    description='A message passing neural network with GRU units',
    install_requires=[
        'click',
        'pandas==1.0.3',
        'torch==1.4.0'
    ],
    entry_points={
        'console_scripts': [
            'message-passing-nn = message_passing_nn.cli:main'
        ],
    },
    classifiers=[
        'Development Status :: 3 - Beta',
        'Intended Audience :: Data-scientists',
        'Topic :: Software Development :: Build Tools',
        'License :: OSI Approved :: MIT License',
        'Programming Language :: Python :: 3.7.6',
    ],
)
