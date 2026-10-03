# AWS Serverless Student Management API

## Project Overview

This project implements a serverless Student Management API using AWS Lambda, Amazon API Gateway, and Amazon DynamoDB.

The API provides CRUD operations to:

* Add a student
* View all students
* View a student by ID
* Update student details
* Delete a student

All API operations are handled using AWS managed services without requiring an EC2 server.

---

## Architecture

```text
Client / Git Bash
       |
       v
Amazon API Gateway
       |
       v
AWS Lambda
       |
       v
Amazon DynamoDB
```

### Request Flow

```text
Git Bash (cURL)
      |
      v
API Gateway
      |
      v
StudentManagementFunction
      |
      v
StudentTable
```

---

## AWS Services Used

| AWS Service        | Purpose                                    |
| ------------------ | ------------------------------------------ |
| Amazon API Gateway | Provides HTTP API endpoints                |
| AWS Lambda         | Processes API requests and CRUD operations |
| Amazon DynamoDB    | Stores student records                     |
| AWS IAM            | Provides permissions to Lambda             |
| Amazon CloudWatch  | Provides Lambda monitoring and logs        |

---

## AWS Configuration

### Region

```text
US East (N. Virginia) - us-east-1
```

### Lambda Function

```text
StudentManagementFunction
```

### DynamoDB Table

```text
StudentTable
```

### DynamoDB Configuration

```text
Partition Key: id
Capacity Mode: On-demand
```

---

### Base URL
```text

### API Endpoints

| ------ | ---------------- | ------------------ |
| POST   | `/students`      | Add student        |
| GET    | `/students/{id}` | View student by ID |
| PUT    | `/students/{id}` | Update student     |
| DELETE | `/students/{id}` | Delete student     |
---

# CRUD API Testing Using Git Bash

The APIs were tested using cURL commands from Git Bash.

## 1. Create Student — POST

```bash
curl -X POST "https://78rg6h77qi.execute-api.us-east-1.amazonaws.com/students" \
-H "Content-Type: application/json" \
```

Expected result:

```text
Student added successfully
```

### Screenshot

![POST Student](screenshots/01-post.png)

---

## 2. View All Students — GET

```bash
curl -X GET "https://78rg6h77qi.execute-api.us-east-1.amazonaws.com/students"
```

### Screenshot

![Get All Students](screenshots/02-get-all.png)

---

## 3. View Student by ID — GET

```bash
curl -X GET "https://78rg6h77qi.execute-api.us-east-1.amazonaws.com/students/101"
```

### Screenshot

![Get Student by ID](screenshots/03-get-by-id.png)

---

## 4. Update Student — PUT

```bash
curl -X PUT "https://78rg6h77qi.execute-api.us-east-1.amazonaws.com/students/101" \
-H "Content-Type: application/json" \
-d '{"name":"Atharv Pawar","age":22,"course":"AWS DevOps","email":"atharvpawar1506@gmail.com"}'
```

### Screenshot

![Update Student](screenshots/04-put-update.png)

---

## 5. Delete Student — DELETE

```bash
curl -X DELETE "https://78rg6h77qi.execute-api.us-east-1.amazonaws.com/students/101"
```

### Screenshot

![Delete Student](screenshots/05-delete.png)

---

## 6. Verify Deletion — GET

```bash
curl -X GET "https://78rg6h77qi.execute-api.us-east-1.amazonaws.com/students"
```

Expected result after deleting student `101`:

```json
{
  "students": []
}
```

### Screenshot

![Final GET Verification](screenshots/06-final-get.png)

---

# AWS Console Screenshots

## DynamoDB

The `StudentTable` stores student information using `id` as the partition key.

![DynamoDB](screenshots/07-dynamodb.png)

---

## AWS Lambda

The `StudentManagementFunction` contains the backend logic for handling student CRUD operations.

![Lambda](screenshots/08-lambda.png)

---

## API Gateway

The API Gateway provides the HTTP routes used to access the Lambda backend.

![API Gateway](screenshots/09-api-gateway.png)

---

# Sample Student Data

```json
{
  "id": "101",
  "name": "Atharv Pawar",
  "age": 21,
  "course": "AWS Cloud",
  "email": "atharvpawar1506@gmail.com"
}
```

---

# Project Result

The serverless Student Management API successfully implements:

* Create student
* Read all students
* Read student by ID
* Update student
* Delete student
* Verify deleted records

The application uses AWS Lambda, API Gateway, and DynamoDB to provide a serverless CRUD-based student management system.

---

# Author

**Atharv Pawar**

## Technologies

* AWS Lambda
* Amazon API Gateway
* Amazon DynamoDB
* AWS IAM
* Amazon CloudWatch
* Python
* Git Bash
* cURL
-d '{"id":"101","name":"Atharv Pawar","age":21,"course":"AWS Cloud","email":"atharvpawar1506@gmail.com"}'

| GET    | `/students`      | View all students  |
| Method | Endpoint         | Operation          |
```
https://78rg6h77qi.execute-api.us-east-1.amazonaws.com


