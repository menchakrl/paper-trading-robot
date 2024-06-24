from typing import Optional

class Portfolio():

    '''6/17/2024
        Optional typing
            var_name: Optional[str] equivalent to var_name: str = None
    '''
    '''6/23/2024
        order of parameters in method signature - parameters w/o default type
            must come before parameters w/ default type
        isinstance(object, type) function - True if the specified object is of 
            the specified type, otherwise False.
    '''
    def __init__(self, account_number: Optional[str]):
        self.positions = {} # dictionary
        self.positions_count = 0
        self.market_value = 0.0
        self.profit_loss = 0.0
        self.risk_tolerance = 0.0
        self.account_number = account_number


    def add_position(self, symbol: str, asset_type: str, purchase_date: Optional[str],
                     quantity: int = 0, purchase_price: float = 0.0, ) -> dict:
        self.positions[symbol] = {}
        self.positions[symbol]["symbol"] = symbol
        self.positions[symbol]["quantity"] = quantity
        self.positions[symbol]["purchase_price"] = purchase_price
        self.positions[symbol]["purchase_date"] = purchase_date
        self.positions[symbol]["asset_type"] = asset_type

        return self.positions

    def add_positions(self, positions: list[dict]) -> dict:
        if isinstance(positions, list):
            for position in positions:
                self.add_position(
                    symbol=position["symbol"],
                    asset_type=position["asset_type"],
                    purchase_date=position.get("purchase_date", None),
                    purchase_price=position.get("purchase_price", 0.0),
                    quantity = position.get("quantity", 0)
                )

            return self.positions

        else:
            raise TypeError("Positions must be a list of dictionaries.")
        
    def remove_position(self, symbol: str) -> tuple[bool, str]:
        if symbol in self.positions:
            del self.positions[symbol]
            return (True, "{symbol} was successfully removed.".format(symbol=symbol))
        
        else:
            return (False, "{symbol} did not exist in the portfolio.".format(symbol=symbol))

    def in_portfolio(self, symbol: str) -> bool:
        return symbol in self.positions
        
    def is_profitable(self, symbol: str, current_price: float) -> bool:
        purchase_price = self.positions[symbol]["purchase_price"]

        return purchase_price <= current_price

    def total_allocation(self):
        # will show distribution across asset classes
        pass

    def risk_exposure(self):
        # a risk metric of some sort 
        pass

    def total_market_value(self):
        pass

