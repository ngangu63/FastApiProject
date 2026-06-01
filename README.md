# FastAPI Customer Service

A simple REST API built with FastAPI for managing customers.

## Features

- Create customers
- Retrieve customer details
- Update customer information
- Delete customers
- Automatic API documentation
- Data validation using Pydantic

## Requirements

- Python 3.11+
- FastAPI
- Uvicorn



### Create Virtual Environment

Using uv:

```bash
uv venv
source .venv/bin/activate   # macOS/Linux

# Windows
.venv\Scripts\activate
```

### Install Dependencies

```bash
uv sync
```

or

```bash
uv pip install -r requirements.txt
```

## Running the Application

Start the FastAPI server:

```bash
uvicorn main:app --reload
```

The application will be available at:

```text
http://127.0.0.1:8000
```

## API Documentation

FastAPI automatically generates interactive API documentation.

### Swagger UI

Open:

```text
http://127.0.0.1:8000/docs
```

Features:

- View all available endpoints
- Execute API requests directly from the browser
- Inspect request and response schemas
- Test authentication (if configured)

### ReDoc

Open:

```text
http://127.0.0.1:8000/redoc
```

Features:

- Clean, readable API documentation
- Detailed schema descriptions
- API reference for developers

## Example Endpoints

### Create Customer

```http
POST /customers
```

Request Body:

```json
{
  "name": "John Doe",
  "email": "john.doe@example.com"
}
```

Response:

```json
{
  "id": 1,
  "name": "John Doe",
  "email": "john.doe@example.com"
}
```

### Get Customer

```http
GET /customers/{customer_id}
```

Example:

```http
GET /customers/1
```

## Project Structure

```text
.
├── main.py
├── models.py
├── schemas.py
├── routers/
│   └── customers.py
├── services/
│   └── customer_service.py
├── pyproject.toml
└── README.md
```

## Development

Run the application in development mode:

```bash
uvicorn main:app --reload
```

Run tests:

```bash
pytest
```

## License

MIT License