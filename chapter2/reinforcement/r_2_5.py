'''Use the techniques of Section 1.7 to revise the charge and make payment
methods of the CreditCard class to ensure that the caller sends a number
as a parameter'''

# Hint: Read about exception handling in Chapter 1

class CreditCard:
    """A customer credit card."""
    
    def __init__(self, customer, bank, acnt, limit):
        """ Create a new credit card instance.
        
        The initial balance is zero.
        
        customer    the name of the customer (e.g., 'john bowman')
        bank        the name of the bank (e.g., 'California Savings')
        acnt        the amount identifier (e.g., '5391 0375 9387 5309')
        limit       credit limit (measured in dollars)
        """
        self._customer = customer
        self._bank = bank
        self._account = acnt
        self._limit = limit
        self._balance = 0
    
    def get_customer(self):
        """return name of customer"""
        return self._customer
    
    def get_bank(self):
        """return bank name"""
        return self._bank
    
    def get_account(self):
        """return card id num (stored as string)"""
        return self._account
    
    def get_limit(self):
        """return current credit limit"""
        return self._limit
    
    def get_balance(self):
        """return current balance"""
        return self._balance
    
    def charge(self, price):
        """charge given price to card, assuming sufficient credit limit
        
        return true if charge processed, false if denied
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
        """process customer payment that reduces balance"""
        try:
            # Ensure amount is a valid number
            amount = float(amount)
            
            if amount <= 0:
                raise ValueError("Payment amount must be a positive number.")
            
            self._balance -= amount
        
        except ValueError:
            print("Error: Invalid amount. Please provide a valid number.")
