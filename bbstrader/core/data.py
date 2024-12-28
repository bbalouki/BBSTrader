import pandas as pd
import numpy as np
from financetoolkit import Discovery
from financetoolkit import Toolkit


__all__ = [
    'FMP',
    'Discovery',
]

class FMP(Toolkit):
    """
    FMPData class for fetching data from Financial Modeling Prep API
    using the Toolkit class from financetoolkit package.

    See `financetoolkit.toolkit_controller.Toolkit` for more details.
    """
    def __init__(self, api_key: str ='', symbols: str | list = 'AAPL'):
        super().__init__(tickers=symbols, api_key=api_key)


class DataBendo:
    ...