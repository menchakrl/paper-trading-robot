import pandas as pd

# from td.client import TDClinet
# from td.util import milliseconds_since_epoch

from datetime import datetime
from datetime import time
from datetime import timezone

class PyRobot():

    ''' 6/16/2024
        access modifier convention
            public = nothing
            private = _ before method or class variable

        type hints
            docs: https://docs.python.org/3/library/typing.html
            cheat sheet: https://mypy.readthedocs.io/en/stable/cheat_sheet_py3.html         
    '''

    '''6/17/2024
        property decorator
            https://www.programiz.com/python-programming/property
        pass statement
            https://www.w3schools.com/python/ref_keyword_pass.asp

    '''

    # constructor
    def __init__(self, client_id: str, redirect_uri: str, 
                 credentials_path: str = None, trading_account: str = None) -> None:
        self.trading_account: str = trading_account
        self.client_id: str = client_id
        self.redirect_uri: str = redirect_uri
        self.credentials_path: str = credentials_path
        self.session: TDClient = self.__create_session()
        self.trades: dict[str, int] = {}
        self.historical_prices: dict[str, float] = {}
        self.stock_frame = None

    # private method
    def _create_session(self) -> TDClient:
        # create client
        td_client = TDClient(client_id = self.client_id,
                             redirect_url = self.redirect_uri,
                             credentials_path=self.credentials_path)
        # login
        td_client.login()

        return td_client
    
    @property
    def pre_market_open(self) -> bool:
        # pass
        per_market_start_time = datetime.now().replace(hour=12, minute=00, second=00, 
                                                       tzinfo=timezone.utc).timestamp()
        market_start_time = datetime.now().replace(hour=13, minute=30, second=00, 
                                                   tzinfo=timezone.utc).timestamp()
        right_now = datetime.now().replace(tzinfo=timezone.utc).timestamp()

        if per_market_start_time <= right_now <= market_start_time:
            return True
        else:
            return False

    @property
    def post_market_open(self) -> bool:
        # pass
        post_market_end_time = datetime.now().replace(hour=22, minute=30, second=00, 
                                                       tzinfo=timezone.utc).timestamp()
        market_end_time = datetime.now().replace(hour=20, minute=00, second=00, 
                                                   tzinfo=timezone.utc).timestamp()
        right_now = datetime.now().replace(tzinfo=timezone.utc).timestamp()

        if market_end_time <= right_now <= post_market_end_time:
            return True
        else:
            return False

    @property
    def regular_market_open(self) -> bool:
        market_start_time = datetime.now().replace(hour=13, minute=30, second=00, 
                                                   tzinfo=timezone.utc).timestamp()
        market_end_time = datetime.now().replace(hour=20, minute=00, second=00, 
                                                   tzinfo=timezone.utc).timestamp()
        right_now = datetime.now().replace(tzinfo=timezone.utc).timestamp()

        if market_start_time <= right_now <= market_end_time:
            return True
        else:
            return False

    def create_portfolio(self):
        pass

    def create_trade(self):
        pass

    def create_stock_frame(self):
        pass

    def get_current_quotes(self) -> dict:
        pass

    def get_historical_prices(self) -> list[dict]:
        pass



