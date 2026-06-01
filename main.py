from fastapi import FastAPI
from pydantic import BaseModel
app = FastAPI()

class Customer(BaseModel):
    id: int
    name: str
    email: str
    
    
#In-memory database
customers = []  

@app.get("/")
def home():
    return {"message": "Welcome to the FastAPI project!"}

@app.get("/customers/")
def get_customers():
    return customers

@app.get("/customers/{customer_id}")
def get_customer(customer_id: int):
    for customer in customers:
        if customer["id"] == customer_id:
            return customer

    return {"error": "Customer not found"}

""" @app.post("/customers/")
def create_customer(customer: Customer):
    customers.append(customer.model_dump())
    return {
        
    } """

@app.post("/customers/")
def create_customer(customer: Customer):
    customers.append(customer.model_dump())
    return {"message": "Customer created"}  

@app.put("/customers/{customer_id}")
def update_customer(customer_id: int, customer: Customer):
    for index, existing in enumerate(customers):
        if existing["id"] == customer_id:
            customers[index] = customer.model_dump()
            return {"message": "Customer updated"}

    return {"error": "Customer not found"}


@app.delete("/customers/{customer_id}")
def delete_customer(customer_id: int):
    for customer in customers:
        if customer["id"] == customer_id:
            customers.remove(customer)
            return {"message": "Customer deleted"}

    return {"error": "Customer not found"}