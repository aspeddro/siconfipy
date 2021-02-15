import pandas as pd
from itertools import product
from time import sleep
from requests import get


def api(type):
    return f"http://apidatalake.tesouro.gov.br/ords/siconfi/tt/{type}?"


def as_list(items):
    """
    Convert to list

    Parameters
    ----------
    items : list or int or str

    Returns
    -------
    list
    """
    return [items] if type(items) is not list else items


def str_con(*kwargs, sep=""):
    """
    Concat string

    Parameters
    ----------
    *kwargs : str or list of str
        list of string

    sep : str, default ""
        seperator

    Examples
    --------
    >>> str_conc("hello", "world")

    >>> str_conc("Hello", ["Jesse", "John"])
    """
    a, b = kwargs

    results = []

    for i in as_list(a):
        for r in as_list(b):
            results.append(str(i) + str(sep) + str(r))

    return results


def fetch(**kwargs):
    """
    Fetch data and create dataframe
    """
    crossdf = [as_list(i) for i in kwargs.values()]
    par = [i for i in kwargs.keys()]
    reqs = [
        [(par[q], e[q]) for q in range(len(e))] for e in list(product(*crossdf))
    ]
    reqs_val = list(
        map(lambda i: list(filter(lambda x: x[1] is not None, i)), reqs)
    )
    # data = [get(api(i[0][1]), params=i[1:]) for i in reqs_val]
    data = []
    for i in reqs_val:
        sleep(1.0)
        r = get(api(i[0][1]), params=i[1:])
        data.append(r)

    results = pd.concat([pd.DataFrame(i.json()["items"]) for i in data])
    return results
