import io
import logging
import os
import shutil

import click

log = logging.getLogger('XDocs')
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
        click.echo('Directory already exists.')
        return

    click.echo('Creating project directory: %s', output_dir)
    os.mkdir(output_dir)

    click.echo('Writing config file: %s', config_path)
    io.open(config_path, 'w', encoding='utf-8').write(config_text)

    click.echo('Writing initial docs: %s', todo_path)
    os.mkdir(docs_dir)
    io.open(todo_path, 'w', encoding='utf-8').write(todo_text)
    click.echo('Project %s created!', output_dir)


@cli.command(name="run")
def run():
    """Run the builtin development server"""
    script_path = os.path.dirname(os.path.realpath(__file__))
    base_path = os.getcwd()
    config_path = os.path.join(base_path, 'xdocs.yml')
    if not os.path.exists(config_path):
        click.echo('The Directory is not a XDocs project.')
        return
    if os.path.exists("build"):
        shutil.rmtree("build")
    click.echo('Coping web pages')
    shutil.copytree(script_path + "/client", "build")

    click.echo('Coping documentation')
    shutil.copytree("docs", os.path.join("build", 'sources'))


if __name__ == '__main__':
    cli()
