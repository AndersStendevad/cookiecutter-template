"""{{cookiecutter.package_name}} CLI"""


import click
from {{cookiecutter.package_name}} import __version__ as VERSION


@click.command()
@click.option("--version", is_flag=True, help="Shows the version of {{cookiecutter.package_name}}")
def {{cookiecutter.package_name}}(version):
    """The main way to engange with {{cookiecutter.package_name}} is with this cli"""
    if version:
        click.echo(f"{VERSION}")
