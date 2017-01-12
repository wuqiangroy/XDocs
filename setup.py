from setuptools import setup, find_packages

setup(
    name="xdocs",
    version="0.0.5",
    license='MIT',
    description='Documentation drives developing.',
    author='gaojiuli',
    author_email='gaojiuli@gmail.com',
    install_requires=["Click", "bottle"],
    url="https://github.com/gaojiuli/Xdocs",
    include_package_data=True,
    packages=find_packages(),
    entry_points="""
        [console_scripts]
        xdocs=Xdocs.server.xdocs:cli
    """
)
