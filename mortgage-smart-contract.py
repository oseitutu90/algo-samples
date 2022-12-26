from typing import Dict

class Mortgage:
    def __init__(self, borrower: str, principal: int, term: int,
                 start_date: int, monthly_payment: int, interest_rate: float) -> None:
        self.borrower = borrower
        self.principal = principal
        self.term = term
        self.start_date = start_date
        self.monthly_payment = monthly_payment
        self.interest_rate = interest_rate
        self.unpaid_balance = principal

    def make_payment(self) -> None:
        interest_due = self.unpaid_balance * (self.interest_rate / 100) / 12
        self.unpaid_balance -= self.monthly_payment + interest_due

    def check_balance(self) -> int:
        return self.unpaid_balance

def main() -> None:
    mortgage = Mortgage("John Doe", 500000, 60, 2021, 2500, 4.5)
    mortgage.make_payment()
    print(mortgage.check_balance())

if __name__ == "__main__":
    main()
