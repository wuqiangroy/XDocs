from setuptools import setup

setup(
    name="xdocs",
    version="0.0.1",
    install_requires=["Click", "bottle"],
    entry_points="""
        [console_scripts]
        xdocs=Xdocs.server.xdocs:cli
    """
)
