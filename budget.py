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
    result = ""
    result += "Percentage spent by category\n"

    # Calculate total amount of withdrawals fo each category
    withdrawals = [
        sum(-1 * entry["amount"] for entry in c.ledger if entry["amount"] < 0)
        for c in categories
    ]
    total = sum(withdrawals)
    percentages = [(w / total) * 100 for w in withdrawals]
    # Index of highest bar chart block for each category
    bar_block_indices = [p // 10 for p in percentages]

    for i in range(11)[::-1]:
        line = ""
        line += f"{i * 10:>3}| "
        for j in bar_block_indices:
            if i <= j:
                line += "o"
            else:
                line += " "

            line += "  "
        result += line + "\n"

    result += " " * 4 + "-" * (1 + 3 * len(categories)) + "\n"

    for i in range(max(len(c.name) for c in categories)):
        line = " " * 5
        for c in categories:
            if i < len(c.name):
                line += c.name[i]
            else:
                line += " "
            line += "  "
        result += line + "\n"
    
    # Slice using [:-1] to remove the last newline character
    return result[:-1]
