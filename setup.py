from setuptools import setup

setup(
    name="xdocs",
    version="0.0.1",
    license='MIT',
    description='Documentation drives developing.',
    author='gaojiuli',
    author_email='gaojiuli@gmail.com',
    install_requires=["Click", "bottle"],
    entry_points="""
        [console_scripts]
        xdocs=Xdocs.server.xdocs:cli
    """
)
