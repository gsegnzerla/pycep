from pprint import pprint

import click

from src.models.cep import Cep


@click.group('cep_cli')
def cep_cli():
    """pycep utilitaries"""
    pass


@cep_cli.command()
@click.argument('nr_cep', type=click.STRING)
def cep(nr_cep):
    """Type <number> to request info by cep."""

    cep = Cep()
    data = cep.get_cep(nr_cep)

    click.echo(data)


@cep_cli.command()
@click.argument('uf', type=click.STRING)
@click.argument('city', type=click.STRING)
@click.argument('street', type=click.STRING)
def name(uf, city, street):
    """Type <uf> <city> <street> to request by name's street."""
    cep = Cep()
    data = cep.get_cep_by_name(uf, city, street)

    pprint(data)
