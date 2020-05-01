import click
from src.cep import Cep


@click.group('cep')
def cep():
    """Utilitarios de cep"""
    ...


@cep.command()
@click.argument('nr_cep', type=click.STRING)
def cep_by_number(nr_cep):
    """Type <number> to request by cep"""
    cep = Cep()
    response = cep.get_cep(nr_cep)
    click.echo(response.json())


@cep.command()
@click.argument('uf', type=click.STRING)
@click.argument('city', type=click.STRING)
@click.argument('street', type=click.STRING)
def cep_by_name(uf, city, street):
    """Type <uf> <city> <street> to request by name's street"""
    cep = Cep()
    response = cep.get_cep_by_name(uf, city, street)

    click.echo(response.text)
