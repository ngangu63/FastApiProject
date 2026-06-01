from typing import List
from fastapi import (
    FastAPI,
    HTTPException,
    Depends,
    Security,
    status
)
from fastapi.security import APIKeyHeader
from pydantic import BaseModel, EmailStr

# =====================================================
# FastAPI Application
# =====================================================

app = FastAPI(
    title="Customer API",
    version="1.0.0",
    description="Secure Customer CRUD API"
)

# =====================================================
# API Key Security
# =====================================================

API_KEY = "my-secret-api-key"

api_key_header = APIKeyHeader(
    name="X-API-Key",
    auto_error=False
)


def verify_api_key(api_key: str = Security(api_key_header)):
    """
    Validate API Key sent in request header.
    """
    if api_key != API_KEY:
        raise HTTPException(
            status_code=status.HTTP_401_UNAUTHORIZED,
            detail="Invalid or missing API Key"
        )
    return api_key


# =====================================================
# Models
# =====================================================

class Customer(BaseModel):
    id: int
    name: str
    email: EmailStr


class CustomerResponse(BaseModel):
    id: int
    name: str
    email: EmailStr


# =====================================================
# In-Memory Database
# =====================================================

customers: List[dict] = []


# =====================================================
# Root Endpoint
# =====================================================

@app.get("/")
def home():
    return {"message": "Customer API is running"}


# =====================================================
# Get All Customers
# =====================================================

@app.get(
    "/customers/",
    response_model=List[CustomerResponse]
)
def get_customers(
    api_key: str = Depends(verify_api_key)
):
    return customers


# =====================================================
# Get Customer By ID
# =====================================================

@app.get(
    "/customers/{customer_id}",
    response_model=CustomerResponse
)
def get_customer(
    customer_id: int,
    api_key: str = Depends(verify_api_key)
):
    for customer in customers:
        if customer["id"] == customer_id:
            return customer

    raise HTTPException(
        status_code=status.HTTP_404_NOT_FOUND,
        detail="Customer not found"
    )


# =====================================================
# Create Customer
# =====================================================

@app.post(
    "/customers/",
    status_code=status.HTTP_201_CREATED
)
def create_customer(
    customer: Customer,
    api_key: str = Depends(verify_api_key)
):
    # Check duplicate ID
    if any(c["id"] == customer.id for c in customers):
        raise HTTPException(
            status_code=status.HTTP_409_CONFLICT,
            detail="Customer ID already exists"
        )

    customers.append(customer.model_dump())

    return {
        "message": "Customer created successfully"
    }


# =====================================================
# Update Customer
# =====================================================

@app.put("/customers/{customer_id}")
def update_customer(
    customer_id: int,
    customer: Customer,
    api_key: str = Depends(verify_api_key)
):
    for index, existing in enumerate(customers):
        if existing["id"] == customer_id:

            customers[index] = customer.model_dump()

            return {
                "message": "Customer updated successfully"
            }

    raise HTTPException(
        status_code=status.HTTP_404_NOT_FOUND,
        detail="Customer not found"
    )


# =====================================================
# Delete Customer
# =====================================================

@app.delete("/customers/{customer_id}")
def delete_customer(
    customer_id: int,
    api_key: str = Depends(verify_api_key)
):
    for customer in customers:
        if customer["id"] == customer_id:
            customers.remove(customer)

            return {
                "message": "Customer deleted successfully"
            }

    raise HTTPException(
        status_code=status.HTTP_404_NOT_FOUND,
        detail="Customer not found"
    )