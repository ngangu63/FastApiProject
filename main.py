from fastapi import FastAPI
from pydantic import BaseModel

# Create FastAPI application instance
app = FastAPI()


# Customer model used for request validation and serialization
class Customer(BaseModel):
    id: int
    name: str
    email: str


# In-memory database (data is lost when the application restarts)
customers = []


# Root endpoint to verify the API is running
@app.get("/")
def home():
    return {"message": "Welcome to the FastAPI project!"}


# Retrieve all customers
@app.get("/customers/")
def get_customers():
    return customers


# Retrieve a single customer by ID
@app.get("/customers/{customer_id}")
def get_customer(customer_id: int):
    # Search for the customer in the in-memory database
    for customer in customers:
        if customer["id"] == customer_id:
            return customer

    # Return an error if customer does not exist
    return {"error": "Customer not found"}


# Create a new customer
@app.post("/customers/")
def create_customer(customer: Customer):
    # Convert Pydantic model to dictionary and store it
    customers.append(customer.model_dump())

    return {"message": "Customer created"}


# Update an existing customer by ID
@app.put("/customers/{customer_id}")
def update_customer(customer_id: int, customer: Customer):
    # Find the customer and replace existing data
    for index, existing in enumerate(customers):
        if existing["id"] == customer_id:
            customers[index] = customer.model_dump()

            return {"message": "Customer updated"}

    # Return an error if customer does not exist
    return {"error": "Customer not found"}


# Delete a customer by ID
@app.delete("/customers/{customer_id}")
def delete_customer(customer_id: int):
    # Find and remove the customer from the list
    for customer in customers:
        if customer["id"] == customer_id:
            customers.remove(customer)

            return {"message": "Customer deleted"}

    # Return an error if customer does not exist
    return {"error": "Customer not found"}