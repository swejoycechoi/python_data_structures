'''The CreditCard class of Section 2.3 initializes the balance of a new account
to zero. Modify that class so that a new account can be given a
nonzero balance using an optional fifth parameter to the constructor. The
four-parameter constructor syntax should continue to produce an account
with zero balance'''

# Read about default parameter values in Chapter 1
class CreditCard:
    """A customer credit card."""
    
    def __init__(self, customer, bank, acnt, limit, balance=0):
        """Create a new credit card instance.
        
        The initial balance can be zero or a specified amount.
        
        customer    the name of the customer (e.g., 'John Bowman')
        bank        the name of the bank (e.g., 'California Savings')
        acnt        the account identifier (e.g., '5391 0375 9387 5309')
        limit       credit limit (measured in dollars)
        balance     initial balance (default is 0)
        """
        self._customer = customer
        self._bank = bank
        self._account = acnt
        self._limit = limit
        self._balance = balance
    
    def get_customer(self):
        """Return name of customer."""
        return self._customer
    
    def get_bank(self):
        """Return bank name."""
        return self._bank
    
    def get_account(self):
        """Return card ID number (stored as string)."""
        return self._account
    
    def get_limit(self):
        """Return current credit limit."""
        return self._limit
    
    def get_balance(self):
        """Return current balance."""
        return self._balance
    
    def charge(self, price):
        """Charge given price to card, assuming sufficient credit limit.
        
        Return true if charge processed, false if denied.
        """
        try:
            # Ensure price is a valid number
            price = float(price)
            
            if price <= 0:
                raise ValueError("Price must be a positive number.")
            
            if price + self._balance > self._limit:
                return False
            else:
                self._balance += price
                return True
        
        except ValueError:
            print("Error: Invalid price. Please provide a valid number.")
            return False
    
    def make_payment(self, amount):
        """Process customer payment that reduces balance."""
        try:
            # Ensure amount is a valid number
            amount = float(amount)
            
            if amount <= 0:
                raise ValueError("Payment amount must be a positive number.")
            
            self._balance -= amount
        
        except ValueError:
            print("Error: Invalid amount. Please provide a valid number.")