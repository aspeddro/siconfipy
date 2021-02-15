import pandas as pd
from .data import br_cods


def find_cod(query=None):
    """
    Find city or state information.

    Parameters
    ----------
    query : str or int
        if str search by name, int find by cod

    Returns
    -------
    DataFrame

    Examples
    --------
    >>> find_cod("Rio de Janeiro")
              cod_ibge            ente  capital regiao  uf esfera  exercicio  populacao          cnpj
        124         33  Rio de Janeiro        0     SE  BR      E       2021   17366189  4.249860e+13
        3156   3304557  Rio de Janeiro        1     SE  RJ      M       2021    6747815  4.249873e+13
    >>> find_cod(33)
             cod_ibge            ente  capital regiao  uf esfera  exercicio  populacao          cnpj
        124        33  Rio de Janeiro        0     SE  BR      E       2021   17366189  4.249860e+13
    """
    if not type(query) in [str, int] and query is not None:
        raise TypeError("query must be str or int")

    df = br_cods

    if query is None:
        return df
    if type(query) is str:
        return df[df["ente"].str.contains(query, case=False)]
    if type(query) is int:
        return df[df["cod_ibge"] == query]
