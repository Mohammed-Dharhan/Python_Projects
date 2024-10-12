import yfinance as yf

class Stock:
    """ 
    Stock class that takes in user input for stock ticker,cost basis, and position size.
    """
    def __init__(self, ticker, cost_basis, position_size):        
        self.ticker = ticker
        self.cost_basis = cost_basis
        self.position_size = position_size

    def total_investment(self):
        """Calculates total investment based on cost basis and position size."""
        return self.cost_basis * self.position_size

    def get_closing_price(self):
        """Fetches the latest closing price of the stock."""
        stock_data = yf.Ticker(self.ticker)
        closing_price = stock_data.history(period="1d")['Close'].iloc[-1]  # Get the last closing price
        return closing_price
    
    
    def profit_loss(self):
        """Calculates profit/loss based on current price and cost basis."""
        current_price = self.get_closing_price()
        profit_loss = current_price - self.cost_basis
        return profit_loss * self.position_size

if __name__ == "__main__":
    portfolio = {
        "COIN": {"cost_basis":173.04, "position_size":2140},
        "HOOD": {"cost_basis":15.20, "position_size":8040},
        "MARA": {"cost_basis":21.86, "position_size":8500},  
        "CLSK": {"cost_basis":17.40, "position_size":6500},
        "SQ": {"cost_basis":68.68, "position_size":1155},
        "TSLA": {"cost_basis":197.65, "position_size":865},
    }
    
    cumulative_profit = 0
    for stock in portfolio:
        print("...................")
        stock = Stock(ticker=stock, cost_basis=portfolio[stock]["cost_basis"], position_size=portfolio[stock]["position_size"])
        closing_price = stock.get_closing_price()
        print(f"The latest closing price for {stock.ticker} is: ${closing_price:.2f}")
        total_investment = stock.total_investment()
        print(f"Total investment in {stock.ticker}: ${total_investment:.2f}")
        profit = stock.profit_loss()
        print(f"Profit/Loss: ${profit:.2f}")
        cumulative_profit = cumulative_profit + stock.total_investment()
    print("...................")    
    print(f"Cumulative Profit/Loss: ${cumulative_profit - 700000}")
    print("...................")
    print(f"Total: ${cumulative_profit:.2f}")
