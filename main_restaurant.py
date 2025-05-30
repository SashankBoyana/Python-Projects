from fastapi import FastAPI
from pydantic import BaseModel
from typing import List

from models.restaurant import Restaurant
from models.table import Table
from models.menu_item import MenuItem

app = FastAPI()
restaurant = Restaurant()

# Add tables and menu items
restaurant.add_table(Table(1, 2))
restaurant.add_table(Table(2, 4))
restaurant.add_table(Table(3, 6))

restaurant.add_menu_item(MenuItem("Burger", 8))
restaurant.add_menu_item(MenuItem("Fries", 3))
restaurant.add_menu_item(MenuItem("Pizza", 10))
restaurant.add_menu_item(MenuItem("Coke", 2))
restaurant.add_menu_item(MenuItem("Pasta", 9))

# Request Models
class CustomerRequest(BaseModel):
    name: str

class OrderRequest(BaseModel):
    name: str
    item_indices: List[int]

class BookTableRequest(BaseModel):
    name: str
    group_size: int

class ReviewRequest(BaseModel):
    name: str
    text: str

# Routes
@app.post("/register")
def register_customer(req: CustomerRequest):
    customer = restaurant.register_customer(req.name)
    return {"message": f"Customer {customer.name} registered."}

@app.get("/menu")
def get_menu():
    return restaurant.show_menu()

@app.post("/book-table")
def book_table(req: BookTableRequest):
    return {"message": restaurant.book_table(req.name, req.group_size)}

@app.post("/order")
def place_order(req: OrderRequest):
    items = restaurant.place_order(req.name, req.item_indices)
    return {"ordered": items}

@app.get("/bill/{name}")
def get_bill(name: str):
    return restaurant.get_bill(name)

@app.post("/review")
def leave_review(req: ReviewRequest):
    restaurant.leave_review(req.name, req.text)
    return {"message": "Review added."}

@app.get("/reviews")
def show_reviews():
    return {"reviews": restaurant.show_reviews()}