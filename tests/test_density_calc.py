#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""
test_density_calc
----------------------------------

Tests for `density_calc` module.
"""

import pytest

from contextlib import contextmanager
from click.testing import CliRunner

from density_calc import cli

INVALID_TEMP_TEXT = 'Temperature must be greater than 49 and less than 251'


@pytest.fixture
def response():
    """Sample pytest fixture.
    See more at: http://doc.pytest.org/en/latest/fixture.html
    """
    # import requests
    # return requests.get('https://github.com/audreyr/cookiecutter-pypackage')


def test_content(response):
    """Sample pytest test function with the pytest fixture as an argument.
    """
    # from bs4 import BeautifulSoup
    # assert 'GitHub' in BeautifulSoup(response.content).title.string
def test_command_line_interface():
    runner = CliRunner()
    result = runner.invoke(cli.main, ['60.0'])
    print(result)
    assert result.exit_code == 0
    assert '62.355298' in result.output

    result = runner.invoke(cli.main, ['49'])
    assert INVALID_TEMP_TEXT in result.output

    result = runner.invoke(cli.main, ['251'])
    assert INVALID_TEMP_TEXT in result.output

    help_result = runner.invoke(cli.main, ['--help'])
    assert help_result.exit_code == 0
    assert '--help  Show this message and exit.' in help_result.output
