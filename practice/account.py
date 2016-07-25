# def _cents_to_dollars(self, cents):


class Account:
    def __init__(self):
        """Initialize Class balance in cents, rate in real numbers"""
        self._balance_cents = 0
        self._rate = 0.001

    def __repr__(self):
        """Return repr

        >>> repr(Account())
        'Account()'
        """
        return 'Account({})'.format(self._balance_cents)

    def __eq__(self, other):
        """Defines equality

        >>> Account(1) == Account(1)
        True
        >>> Account(1) == Account(2)
        False
        """
        return (
            self._balance_cents == other._balance_cents and
            self._rate == other._rate
        )

    def get_funds(self):
        """Returns account balance.

        >>> a = Account()
        >>> a.get_funds()
        0.0
        """
        return self._balance_cents / 100

    def deposit(self, amount):
        """Deposit to the account.

        >>> a = Account()
        >>> a.deposit(30)
        >>> a._balance_cents
        3000
        """
        self._balance_cents += amount * 100

    def check_withdrawal(self, amount):
        """Returns True if large enough balance for withdrawal.

        >>> a = Account()
        >>> a.check_withdrawal(10)
        False
        >>> a = Account()
        >>> a._balance_cents = 1000
        >>> a.check_withdrawal(10)
        True
        """
        return amount * 100 <= self._balance_cents

    def withdraw(self, amount):
        """Withdraw an allowed amount, raises ValueError if insufficient balance.

        >>> a = Account()
        >>> a._balance_cents = 1000
        >>> a.withdraw(10)
        >>> a._balance_cents
        0
        >>> a = Account()
        >>> a.withdraw(10)
        Traceback (most recent call last):
            ...
        ValueError
        """
        if not self.check_withdrawal(amount):
            raise ValueError()
        else:
            self._balance_cents -= amount * 100

    def calc_interest(self):
        """Calculate and return interest on the current account balance.

        >>> a = Account()
        >>> a._balance_cents = 1000
        >>> a.calc_interest()
        0.01
        """
        return self._balance_cents * self._rate / 100
