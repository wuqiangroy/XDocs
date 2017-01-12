from setuptools import setup, find_packages

setup(
    name='xdocs',
    version='0.0.5',
    license='MIT',
    description='Documentation drives developing.',
    author='gaojiuli',
    author_email='gaojiuli@gmail.com',
    install_requires=["click", "bottle", 'PyYAML>=3.10'],
    url='https://github.com/gaojiuli/Xdocs',
    packages=find_packages(),
    package_data={
        'client': ['*'],
        'examples': ['*']
    },
    entry_points={
        'console_scripts': [
            'xdocs=xdocs.__main__:cli',
        ],
    },
)
