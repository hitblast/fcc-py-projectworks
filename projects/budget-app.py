class Category:
  def __init__(self, name: str):
    self.name = name
    self.ledger = list()

  def withdraw(self, amount: int, description: str=""):
    if self.check_funds(amount):
      self.ledger.append({"amount": -amount, "description": description})
      return True
    else:
      return False

  def deposit(self, amount: int, description: str=""):
    self.ledger.append({"amount": amount, "description": description})

  def get_balance(self):
    total = int()
    for item in self.ledger:
      total += item['amount']
    return total

  def transfer(self, amount: int, budget_category):
    if self.check_funds(amount):
      self.withdraw(amount, f"Transfer to {budget_category.name}")
      budget_category.deposit(amount, f"Transfer from {self.name}")
      return True
    else:
      return False

  def check_funds(self, amount: int):
    if amount <= self.get_balance():
      return True
    else:
      return False

  def __str__(self):
    output = self.name.center(30, "*") + "\n"
    for item in self.ledger:
      output += f"{item['description'][:23].ljust(23)}{format(item['amount'], '.2f').rjust(7)}\n"
    output += f"Total: {format(self.get_balance(), '.2f')}"
    return output

def create_spend_chart(categories):
  category_names = list()
  spent = list()
  spent_percentages = list()

  for category in categories:
    total = 0
    for item in category.ledger:
      if item['amount'] < 0:
        total -= item['amount']
    spent.append(round(total, 2))
    category_names.append(category.name)

  for amount in spent:
    spent_percentages.append(round(amount / sum(spent), 2)*100)

  graph = "Percentage spent by category\n"
  labels = range(100, -10, -10)

  for label in labels:
    graph += str(label).rjust(3) + "| "
    for percent in spent_percentages:
      if percent >= label:
        graph += "o  "
      else:
        graph += "   "
    graph += "\n"

  graph += "    ----" + ("---" * (len(category_names) - 1))
  graph += "\n     "
  longest_name_length = 0

  for name in category_names:
    if longest_name_length < len(name):
      longest_name_length = len(name)

  for i in range(longest_name_length):
    for name in category_names:
      if len(name) > i:
        graph += name[i] + "  "
      else:
        graph += "   "
    if i < longest_name_length-1:
      graph += "\n     "

  return(graph)
