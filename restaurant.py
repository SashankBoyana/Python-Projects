from .table import Table
from .menu_item import MenuItem
from .customer import Customer

class Restaurant:
    def __init__(self):
        self.tables = []
        self.menu = []
        self.reviews = []
        self.customers = {}

    def add_table(self, table: Table):
        self.tables.append(table)

    def add_menu_item(self, item: MenuItem):
        self.menu.append(item)

    def register_customer(self, name: str) -> Customer:
        customer = Customer(name)
        self.customers[name] = customer
        return customer

    def book_table(self, customer_name: str, group_size: int) -> str:
        for table in self.tables:
            if not table.is_reserved and table.seats >= group_size:
                table.is_reserved = True
                return f"Table {table.number} booked for {customer_name}"
        return "No table available for that group size."

    def place_order(self, customer_name: str, item_indices: list[int]) -> list[str]:
        customer = self.customers.get(customer_name)
        added = []
        for idx in item_indices:
            if 0 <= idx < len(self.menu):
                item = self.menu[idx]
                customer.order.append(item)
                added.append(item.name)
        return added

    def get_bill(self, customer_name: str) -> dict:
        customer = self.customers.get(customer_name)
        total = sum(item.price for item in customer.order)
        return {
            "items": [(item.name, item.price) for item in customer.order],
            "total": total
        }

    def leave_review(self, customer_name: str, text: str):
        self.reviews.append(f"{customer_name}: {text}")

    def show_reviews(self) -> list[str]:
        return self.reviews

    def show_menu(self) -> list[dict]:
        return [{"name": item.name, "price": item.price} for item in self.menu]