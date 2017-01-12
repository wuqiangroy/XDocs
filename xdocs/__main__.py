import logging
import os
import shutil

import click
from flask_script import Manager
from livereload import Server

from .server import app

logging.basicConfig(format='[%(levelname)s]:%(message)s', level=logging.INFO)

config_text = 'site_name: My Docs\n'
todo_text = """# Welcome to MkDocs
For full documentation visit [mkdocs.org](http://mkdocs.org).
## Commands
* `mkdocs new [dir-name]` - Create a new project.
* `mkdocs serve` - Start the live-reloading docs server.
* `mkdocs build` - Build the documentation site.
* `mkdocs help` - Print this help message.
## Project layout
    mkdocs.yml    # The configuration file.
    docs/
        index.md  # The documentation homepage.
        ...       # Other markdown pages, images and other files.
"""


@click.group(context_settings={'help_option_names': ['-h', '--help']})
def cli():
    """
    XDocs - 文档驱动开发
    """


@cli.command(name="new")
@click.argument('output_dir')
def new(output_dir):
    """Create a new XDocs project"""
    docs_dir = os.path.join(output_dir, 'docs')
    config_path = os.path.join(output_dir, 'xdocs.yml')
    todo_path = os.path.join(docs_dir, 'Todo.yml')
    if os.path.exists(output_dir):
        logging.warning('Directory already exists.')
        return

    logging.info('Creating project directory: %s', output_dir)
    os.mkdir(output_dir)

    logging.info('Writing config file: %s', config_path)
    open(config_path, 'w').write(config_text)

    logging.info('Writing initial docs: %s', todo_path)
    os.mkdir(docs_dir)
    open(todo_path, 'w').write(todo_text)
    logging.info('Project %s created!', output_dir)


@cli.command(name="run")
@click.option('-a', '--address',
              help='IP address and port to serve documentation locally (default:"localhost:8000")',
              metavar='<IP:PORT>')
def run(address):
    """Run the builtin development server"""
    script_path = os.path.dirname(os.path.realpath(__file__))
    base_path = os.getcwd()
    source_path = os.path.join(base_path, 'docs')
    config_path = os.path.join(base_path, 'xdocs.yml')
    if not os.path.exists(config_path):
        logging.warning('The Directory is not a XDocs project.')
        return
    if os.path.exists("client"):
        shutil.rmtree("client")
    logging.info('Coping web pages')
    shutil.copytree(script_path + "/client", "client")
    if not address:
        address = "localhost:8000"
    host, port = address.split(':', 1)

    manager = Manager(app)
    live_server = Server(app.wsgi_app)
    live_server.watch(source_path)
    live_server.serve(restart_delay=0, open_url_delay=True, host=host, port=port)
    manager.run()


if __name__ == '__main__':
    cli()
