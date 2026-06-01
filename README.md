# Customer API

A secure RESTful Customer Management API built with FastAPI. This application provides CRUD (Create, Read, Update, Delete) operations for customer records and protects endpoints using API Key authentication.

## Features

* FastAPI-based REST API
* API Key Security
* Customer CRUD Operations
* Request Validation using Pydantic
* Email Validation
* Interactive Swagger Documentation
* OpenAPI Specification Support
* Proper HTTP Status Codes and Error Handling

---

## Technology Stack

* Python 3.10+
* FastAPI
* Uvicorn
* Pydantic

---

## Project Structure

```text
project/
│
├── main.py
├── README.md
└── requirements.txt
```

---

## Installation

### Clone the Repository

```bash
git clone https://github.com/yourusername/customer-api.git
cd customer-api
```

### Create a Virtual Environment

```bash
python -m venv .venv
```

### Activate the Virtual Environment

#### Linux / macOS

```bash
source .venv/bin/activate
```

#### Windows

```cmd
.venv\Scripts\activate
```

### Install Dependencies

```bash
pip install fastapi uvicorn email-validator
```

---

## Running the Application

Start the FastAPI server:

```bash
uvicorn main:app --reload
```

Server starts on:

```text
http://127.0.0.1:8000
```

---

## API Documentation

FastAPI automatically generates interactive API documentation.

### Swagger UI

```text
http://127.0.0.1:8000/docs
```

### ReDoc

```text
http://127.0.0.1:8000/redoc
```

---

## Security

The API uses API Key authentication.

### API Key Header

```http
X-API-Key: my-secret-api-key
```

All customer endpoints require this header.

Example:

```bash
curl -H "X-API-Key: my-secret-api-key" \
http://127.0.0.1:8000/customers/
```

---

## API Endpoints

### Health Check

#### GET /

Returns application status.

Response:

```json
{
  "message": "Customer API is running"
}
```

---

### Get All Customers

#### GET /customers/

Headers:

```http
X-API-Key: my-secret-api-key
```

Response:

```json
[
  {
    "id": 1,
    "name": "John Doe",
    "email": "john@example.com"
  }
]
```

---

### Get Customer By ID

#### GET /customers/{customer_id}

Example:

```bash
GET /customers/1
```

Response:

```json
{
  "id": 1,
  "name": "John Doe",
  "email": "john@example.com"
}
```

---

### Create Customer

#### POST /customers/

Request Body:

```json
{
  "id": 1,
  "name": "John Doe",
  "email": "john@example.com"
}
```

Response:

```json
{
  "message": "Customer created successfully"
}
```

---

### Update Customer

#### PUT /customers/{customer_id}

Request Body:

```json
{
  "id": 1,
  "name": "John Smith",
  "email": "johnsmith@example.com"
}
```

Response:

```json
{
  "message": "Customer updated successfully"
}
```

---

### Delete Customer

#### DELETE /customers/{customer_id}

Response:

```json
{
  "message": "Customer deleted successfully"
}
```

---

## Customer Model

```json
{
  "id": 1,
  "name": "John Doe",
  "email": "john@example.com"
}
```

Field Description:

| Field | Type    | Description                |
| ----- | ------- | -------------------------- |
| id    | Integer | Unique customer identifier |
| name  | String  | Customer name              |
| email | String  | Valid email address        |

---

## Error Responses

### Invalid API Key

```json
{
  "detail": "Invalid or missing API Key"
}
```

Status Code:

```text
401 Unauthorized
```

### Customer Not Found

```json
{
  "detail": "Customer not found"
}
```

Status Code:

```text
404 Not Found
```

### Duplicate Customer ID

```json
{
  "detail": "Customer ID already exists"
}
```

Status Code:

```text
409 Conflict
```

---

## Example cURL Commands

### Create Customer

```bash
curl -X POST "http://127.0.0.1:8000/customers/" \
-H "Content-Type: application/json" \
-H "X-API-Key: my-secret-api-key" \
-d '{
  "id": 1,
  "name": "John Doe",
  "email": "john@example.com"
}'
```

### Get All Customers

```bash
curl -X GET "http://127.0.0.1:8000/customers/" \
-H "X-API-Key: my-secret-api-key"
```

### Delete Customer

```bash
curl -X DELETE "http://127.0.0.1:8000/customers/1" \
-H "X-API-Key: my-secret-api-key"
```

---

## Notes

* Data is stored in an in-memory list.
* All data will be lost when the application restarts.
* For production use, replace the in-memory storage with a database such as PostgreSQL, MySQL, or MongoDB.
* Store API keys in environment variables instead of hardcoding them.

---

## License

This project is provided for educational and demonstration purposes.
