# Invoice Management REST API Guide

This guide will walk you through the REST API lifecycle of an invoice, demonstrating the creation and deletion of clients, invoices, services, and invoice services, and showcasing the cascade relationships. Additionally, it will demonstrate updating invoice service quantities and their reflection in the invoice.

## Prerequisites

- A virtual python enviroment with all requirements listed in the `requirements.txt` file installed.
- Ensure the FastAPI server is running on `localhost:8080`.
- Use the following `curl` commands to interact with the API.

## REST API Lifecycle of an Invoice

### Step 1: Create a Client

Create a client if it doesn't already exist.

**Request:**

```bash
curl -X POST "http://localhost:8080/api/v1/clients/" -H "Content-Type: application/json" -d '{
  "name": "John Doe",
  "email": "john.doe@example.com"
}'
```

**Response:**

```json
{
  "id": 1,
  "name": "John Doe",
  "email": "john.doe@example.com",
  "invoices": []
}
```

### Step 2: Create a Service

Create a service if it doesn't already exist.

**Request:**

```bash
curl -X POST "http://localhost:8080/api/v1/services/" -H "Content-Type: application/json" -d '{
  "name": "Consulting",
  "price": 150.0
}'
```

**Response:**

```json
{
  "id": 1,
  "name": "Consulting",
  "price": 150.0
}
```

### Step 3: Create an Invoice

Create an invoice for the client.

**Request:**

```bash
curl -X POST "http://localhost:8080/api/v1/invoices/" -H "Content-Type: application/json" -d '{
  "invoice_number": "INV-001",
  "date": "2024-05-26",
  "status": 4,
  "client_id": 1,
  "services": [],
  "payments": []
}'
```

**Response:**

```json
{
  "id": 1,
  "invoice_number": "INV-001",
  "date": "2024-05-26",
  "due_date": null,
  "status": 4,
  "client_id": 1,
  "services": [],
  "payments": [],
  "total": 0.0,
  "total_paid": 0.0,
  "total_due": 0.0
}
```

**_Invoice Status_**

Statuses are integer values 0-12, which are defined by the enum below:

```yaml
ESTIMATE = 0
DRAFT = 1
PENDING_APPROVAL = 2
APPROVED = 3
SENT = 4
VIEWED = 5
PARTIALLY_PAID = 6
PAID = 7
OVERDUE = 8
DISPUTED = 9
CANCELLED = 10
WRITTEN_OFF = 11
REFUNDED = 12
```

### Step 4: Create an Invoice Service

Create an invoice service to apply the service to the specific invoice.

**Request:**

```bash
curl -X POST "http://localhost:8080/api/v1/invoice_services/" -H "Content-Type: application/json" -d '{
  "service_id": 1,
  "quantity": 2
}'
```

**Response:**

```json
{
  "id": 1,
  "service_id": 1,
  "quantity": 2,
  "service": {
    "id": 1,
    "name": "Consulting",
    "price": 150.0
  }
}
```

### Step 5: Update Invoice Service Quantity

Update the quantity of the invoice service and check the reflection in the invoice.

**Request:**

```bash
curl -X PUT "http://localhost:8080/api/v1/invoice_services/1" -H "Content-Type: application/json" -d '{
  "id": 1,
  "service_id": 1,
  "quantity": 3
}'
```

**Response:**

```json
{
  "id": 1,
  "service_id": 1,
  "quantity": 3,
  "service": {
    "id": 1,
    "name": "Consulting",
    "price": 150.0
  }
}
```

### Step 6: Demonstrate Cascade Deletion

#### Delete an Invoice

Deleting an invoice will result in the deletion of all associated invoice services.

**Request:**

```bash
curl -X DELETE "http://localhost:8080/api/v1/invoices/1" -H "Content-Type: application/json"
```

**Response:**

```json
{
  "id": 1,
  "invoice_number": "INV-001",
  "date": "2024-05-26",
  "due_date": null,
  "status": 4,
  "client_id": 1,
  "services": [
    {
      "id": 1,
      "service_id": 1,
      "quantity": 3,
      "service": {
        "id": 1,
        "name": "Consulting",
        "price": 150.0
      }
    }
  ],
  "payments": [],
  "total": 450.0,
  "total_paid": 0.0,
  "total_due": 450.0
}
```

The above response shows the deleted invoice along with its associated invoice services.

#### Verify Deletion of Invoice Services

Attempt to get the deleted invoice service.

**Request:**

```bash
curl -X GET "http://localhost:8080/api/v1/invoice_services/1" -H "Content-Type: application/json"
```

**Response:**

```json
{
  "detail": "InvoiceService not found"
}
```

#### Delete a Client

Deleting a client will result in the deletion of all associated invoices and their invoice services.

**Request:**

```bash
curl -X DELETE "http://localhost:8080/api/v1/clients/1" -H "Content-Type: application/json"
```

**Response:**

```json
{
  "id": 1,
  "name": "John Doe",
  "email": "john.doe@example.com",
  "invoices": [
    {
      "id": 1,
      "invoice_number": "INV-001",
      "date": "2024-05-26",
      "due_date": null,
      "status": 4,
      "client_id": 1,
      "services": [],
      "payments": [],
      "total": 0.0,
      "total_paid": 0.0,
      "total_due": 0.0
    }
  ]
}
```

The above response shows the deleted client along with their associated invoices, which in turn would have had their invoice services deleted.

#### Verify Deletion of Invoices and Invoice Services

Attempt to get the deleted invoice.

**Request:**

```bash
curl -X GET "http://localhost:8080/api/v1/invoices/1" -H "Content-Type: application/json"
```

**Response:**

```json
{
  "detail": "Invoice not found"
}
```

Attempt to get the deleted invoice service.

**Request:**

```bash
curl -X GET "http://localhost:8080/api/v1/invoice_services/1" -H "Content-Type: application/json"
```

**Response:**

```json
{
  "detail": "InvoiceService not found"
}
```

### Summary

This guide demonstrated the lifecycle of creating and deleting entities in the Invoice Management System, including the creation of clients, services, invoices, and invoice services, as well as demonstrating the cascade delete functionality. Deleting an invoice resulted in the deletion of associated invoice services, and deleting a client resulted in the deletion of associated invoices and their invoice services.

