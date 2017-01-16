# -*- coding: utf-8 -*-

import click
from math import pow

def _calculate(temp: float) -> float:
    return 62.56 + 3.413 * pow(10, -4) * temp - 6.255 * pow(10, -5) * pow(temp, 2)


@click.command()
@click.argument('temp', type=click.FLOAT)
def main(temp):
    """Console script for water-density, based on TEMP"""
    click.echo()
    if temp < 50 or temp > 250:
        click.echo('Temperature must be greater than 49 and less than 251')
    else:
        click.echo('Density @ {}°: {}'.format(temp, _calculate(temp)))


if __name__ == "__main__":
    main()
