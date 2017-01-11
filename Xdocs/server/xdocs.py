import click


@click.group(context_settings={'help_option_names': ['-h', '--help']})
def cli():
    """
    XDocs - 文档驱动开发
    """


@cli.command(name="new")
@click.argument('project')
def new(name):
    """Create a new XDocs project"""
    click.echo('Project %s!' % name)


@cli.command(name="run")
def run():
    """Run the builtin development server"""
    click.echo('the serve is running')


if __name__ == '__main__':
    cli()
