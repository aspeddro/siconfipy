# siconfipy

[![pypi](https://img.shields.io/pypi/v/siconfipy.svg)](https://pypi.python.org/pypi/siconfipy/)
[![PyPI status](https://img.shields.io/pypi/status/siconfipy.svg)](https://pypi.python.org/pypi/siconfipy/)
[![PyPI license](https://img.shields.io/pypi/l/siconfipy.svg)](https://pypi.python.org/pypi/siconfipy/)
[![Code style: black](https://img.shields.io/badge/code%20style-black-000000.svg)](https://github.com/psf/black)

Python library to access data from the Brazilian Public Sector Accounting and Tax Information System (SICONFI/[National Treasure](https://www.gov.br/tesouronacional/en?set_language=en))

This package is available for [**R**](https://github.com/pedrocastroo/siconfir)

## Installation

Install from [pip](https://pypi.org/project/siconfipy)

```bash
pip install siconfipy
```

Install from github

```bash
pip install git+https://github.com/pedrocastroo/siconfipy.git
```

Dependencies:

* `pandas>=2.25.1`
* `requests>=1.2.1`

## Using

siconfipy provides four main functions:

* `get_fiscal()` - Fiscal Management Report

* `get_budget()` - Budget Execution Summary Report
  
* `get_annual_acc()` - Annual Statement of Accounts

* `get_info()` - Basic information of the federation entities

Utility functions:

`find_cod()` to get the id (`cod_ibge`) for each state or city

Datasets:

* `br_cods`

## Examples

Load `siconfipy`

```python
import siconfipy
```

or load functions

```python
from siconfipy import get_fiscal, get_budget, br_cods
```

Fiscal management report for the state of Sao Paulo (`35`) for the first four months of 2020:

```python
get_fiscal(year=2020, period=1, cod=35)
```

> You can pass a list of integers in `year`, `period` or `cod`. Example: `year=[2018,2019,2020]` or `cod=[35,33]`. More details `help(get_fiscal)`

Summary of the budget execution report for the state of Rio de Janeiro (`33`) of 2018 for the first two months:

```python
get_budget(year=2018, period=1, cod=33)
```

Annual accounts statement of the Federal District (`53`) for 2018:

```python
get_annual_acc(year=2018, cod=53)
```

Use `find_cod()` to get the `cod` (`cod_ibge` column) parameter:

```python
find_cod("Rio de Janeiro")
      cod_ibge            ente  capital regiao  uf esfera  exercicio  populacao          cnpj
124         33  Rio de Janeiro        0     SE  BR      E       2021   17366189  4.249860e+13
3156   3304557  Rio de Janeiro        1     SE  RJ      M       2021    6747815  4.249873e+13
```

Acess basic information of the federation entities:

```python
get_info()
```

`br_cods` provides results similar to `get_info()`, but with some corrections, see [`utils/build_datasets.py`](utils/build_datasets.py)

> All data, as column name is in pt-BR, the [API](http://apidatalake.tesouro.gov.br/docs/siconfi/) does not provide an endpoint in en.

## TODO

- [ ] `README.md` pt-br
- [ ] Add Accounting Balance Matrix - balance sheet accounts
- [ ] Add Accounting Balances Matrix - Budget Accounts 
- [ ] Add Accounting Balances Matrix - Control Accounts
- [ ] Add Extract of approved reports and matrices delivered
- [ ] Add Attachments of reports by sphere of government 

## Contributing

Bugs or suggestions: open an [issue](https://github.com/pedrocastroo/siconfipy/issues) detailing the problem/suggestion, be as reproducible as possible.

## License

This project is released under the MIT License.
