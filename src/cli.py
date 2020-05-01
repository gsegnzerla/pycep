import click
from src.cep import Cep


@click.group('cep_cli')
def cep_cli():
    """Pycep utilitaries"""
    ...


@cep_cli.command()
@click.argument('nr_cep', type=click.STRING)
def cep(nr_cep):
    """Type <number> to request by cep."""
    cep = Cep()
    response = cep.get_cep(nr_cep)
    click.echo(response.text)

@cep_cli.command()
@click.argument('uf', type=click.STRING)
@click.argument('city', type=click.STRING)
@click.argument('street', type=click.STRING)
def name(uf, city, street):
    """Type <uf> <city> <street> to request by name's street."""
    cep = Cep()
    response = cep.get_cep_by_name(uf, city, street)

    click.echo(response.text)
