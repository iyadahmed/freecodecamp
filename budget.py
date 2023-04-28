class Category:
    def __init__(self, name: str):
        self.name = name
        self.ledger = []

    def deposit(self, amount: float, description=""):
        self.ledger.append({"amount": amount, "description": description})

    def withdraw(self, amount: float, description=""):
        if self.check_funds(amount):
            self.deposit(-1 * amount, description)
            return True
        return False

    def get_balance(self):
        return sum(entry["amount"] for entry in self.ledger)

    def transfer(self, amount: float, other: "Category"):
        if self.withdraw(amount, f"Transfer to {other.name}"):
            other.deposit(amount, f"Transfer from {self.name}")
            return True

        return False

    def check_funds(self, amount: float):
        return amount <= self.get_balance()

    def __str__(self) -> str:
        title_line = bytearray(b"*" * 30)
        i = 30 // 2 - len(self.name) // 2
        title_line[i : i + len(self.name)] = self.name.encode("ascii")

        result = title_line.decode("ascii") + "\n"

        for entry in self.ledger:
            amount_str = f"{entry['amount']:.2f}"[:7]
            result += f"{entry['description'][:23]:<23}{amount_str:>7}\n"

        result += f"Total: {self.get_balance()}"

        return result


def create_spend_chart(categories: list[Category]):
    pass
