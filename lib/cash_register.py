class CashRegister:
    def __init__(self, discount=0):
        self.total = 0
        self.items = []
        self.discount = discount
        self.last_transaction_amount = 0.0

    def add_item(self, title, price, quantity=1):
      if quantity < 0 or price < 0:
          print("Invalid input: Quantity and price must be non-negative.")
      else:
          item_total = price * quantity
          self.items.append({'title': title, 'price': price, 'quantity': quantity, 'total': item_total})
          self.total += item_total
          self.last_transaction_amount = item_total

    def apply_discount(self):
      if self.discount > 0.0:
        discount_amount = self.total * self.discount / 100
        self.total -= discount_amount
        print(f"Discount applied. New total: ${self.total:.2f}")
        print(f"After the discount, the total comes to ${self.total:.2f}")
      else:
        print("There is no discount to apply.")



    def void_last_transaction(self):
        if self.items:
            removed_item = self.items.pop()
            self.total -= removed_item['total']
            self.last_transaction_amount = -removed_item['total']
        else:
            print("No transactions to void.")

    def get_all_items(self):
        return self.items
