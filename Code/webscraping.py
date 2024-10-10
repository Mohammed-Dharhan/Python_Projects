import yfinance as yf

class Stock:
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
    # Get user input for stock ticker, cost basis, and position size
    ticker = input("Enter the stock ticker (e.g., AAPL): ").upper()  # Convert to uppercase for consistency
    cost_basis = float(input("Enter the cost basis: "))
    position_size = int(input("Enter the position size: "))

    # Create an instance of the Stock class using user input
    user_stock = Stock(ticker=ticker, cost_basis=cost_basis, position_size=position_size)

    # Retrieve the closing price
    closing_price = user_stock.get_closing_price()
    print(f"The latest closing price for {user_stock.ticker} is: ${closing_price:.2f}")

    # Calculate total investment
    total_investment = user_stock.total_investment()
    print(f"Total investment in {user_stock.ticker}: ${total_investment:.2f}")
    
    profit = user_stock.profit_loss()
    print(f"Profit/Loss: ${profit:.2f}")
