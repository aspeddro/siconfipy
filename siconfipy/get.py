from siconfipy.utils import fetch, as_list, str_con


def get_fiscal(
    year, period, cod, freq="Q", annex=None, power=["E", "L", "J", "M", "D"]
):
    """
    Access the Fiscal Management Report

    Parameters
    ----------
    year : int or list of int
        year
    period : int or list of int
        period of the year, if the parameter `freq` is "Q" (Default) then it will
        be an integer between 1 and 3. If `freq` is "S" then it will be an integer
        between 1 and 2.
    cod : int or list of int
        id of city or state. Brazilian Institute of Geography and Statistics
        (IBGE) code assigned to each municipality and state
    freq : str, optional, default 'Q'
        "Q" or "S", periodicity of the fiscal management report. "S" is
        semiannual (6 months). "Q" is four-month. The semiannual periodicity "S"
        applies only to municipalities with less than 50 thousand inhabitants
        that opted for simplified publication
    annex : int or list of int, optional, default None
        Attachment number. A value between 1 and 6. The default value is None,
        it will get all attachments
    power : str or list of str, optional, default ["E", "L", "J", "M", "D"]
        Acronym for each power, executive "E", legislative "L", judiciary "J",
        public ministry "M", Public defense "D".

    Returns
    -------
    DataFrame

    Examples
    --------
    >>> get_fiscal(year=2020, period=1, cod=35)

    >>> get_fiscal(year=2019, period=[1,2,3], cod=35)

    >>> get_fiscal(year=2020, period=1, cod=[17,35], power = "E")
    """
    return fetch(
        type="rgf",
        an_exercicio=year,
        in_periodicidade=freq,
        nr_periodo=period,
        co_tipo_demonstrativo="RGF" if freq == "Q" else "RGF Simplificado",
        no_anexo=str_con("RGF-Anexo 0", annex) if annex is not None else None,
        co_poder=power,
        id_ente=cod,
    )


def get_budget(year, period, cod, simple=False, annex=None):
    """
    Access the Budget Execution Summary Report

    Parameters
    ----------
    year : int or list of int
        year
    period : int or list of int
        Two months period, an integer between 1 and 6
    cod : int, list of int
        id of city or state. Brazilian Institute of Geography and Statistics
        (IBGE) code assigned to each municipality and state
    simple : bool, optional, default False
        Report type. True applies only to municipalities with less than 50
        thousand inhabitants that have opted for simplified publication
    annex : str or list of str, optional, default None
        Attachment name. Default is None it will get all attachments. Possible
        values: "01", "02", "03", "04", "04 - RGPS", "04 - RPPS", "04.0 - RGPS",
        "04.1", "04.2", "04.3 - RGPS", "05", "06", "07", "09", "10 - RGPS",
        "10 - RPPS", "11", "13", "14"

    Returns
    -------
    DataFrame

    Examples
    --------
    >>> get_budget(year=2020, period=2, cod=35)

    >>> get_budget(year=[2018,2019,2020], period=2, cod=35)
    """
    return fetch(
        type="rreo",
        an_exercicio=year,
        nr_periodo=period,
        co_tipo_demonstrativo="RREO Simplificado" if simple else "RREO",
        no_anexo=str_con("RREO-Anexo ", annex) if annex is not None else None,
        id_ente=cod,
    )


def get_annual_acc(year, cod, annex=None):
    """
    Access the Annual Statement of Accounts

    Parameters
    ----------
    year : int or list of int
        year
    cod : int or list of int
        id of city or state. Brazilian Institute of Geography and Statistics
        (IBGE) code assigned to each municipality and state
    annex : str or list of str, optional, default None
        Attachment name. Default is None it will get all attachments. Possible
        values: "Anexo I-AB", "Anexo I-C", "Anexo I-D", "Anexo I-E", "Anexo I-F",
        "Anexo I-G", "Anexo I-HI", "DCA-Anexo I-AB", "DCA-Anexo I-C",
        "DCA-Anexo I-D", "DCA-Anexo I-E", "DCA-Anexo I-F", "DCA-Anexo I-G",
        "DCA-Anexo I-HI"

    Returns
    -------
    DataFrame

    Examples
    --------
    >>> get_annual_acc(year=2019, cod = 52)

    >>> get_annual_acc(year=2019, cod = 42, annex=["Anexo I-E", "Anexo I-F"])
    """
    return fetch(
        type="dca", an_exercicio=year, no_annex=as_list(annex), id_ente=cod
    )


def get_info():
    """
    Basic information of the federation entities

    Returns
    -------
    DataFrame

    Examples
    --------
    >>> get_info()
    """
    return fetch(type="entes")
