# 🚀 Serverless Student Management API on AWS

> **A serverless Student Management REST API built using Amazon API Gateway, AWS Lambda, and Amazon DynamoDB to perform complete CRUD operations on student records.**

---

## 📌 Project Overview

This project implements a **serverless Student Management API** using AWS managed services.

The application provides REST API endpoints to **create, read, update, and delete student records** stored in Amazon DynamoDB.

The API is completely serverless and does not require an EC2 server to process requests.

### Core AWS Architecture

```text
Client / Git Bash
       │
       │ HTTP Request
       ▼
┌──────────────────────┐
│   Amazon API Gateway │
│     HTTP API         │
└──────────┬───────────┘
           │
           │ Invoke
           ▼
┌──────────────────────┐
│     AWS Lambda       │
│ StudentManagement    │
│     Function         │
└──────────┬───────────┘
           │
           │ Read / Write
           ▼
┌──────────────────────┐
│   Amazon DynamoDB    │
│    StudentTable      │
└──────────────────────┘
```

---

# 🎯 Project Objective

The objective of this project is to build a **serverless student management API** capable of performing the following operations:

* Create student records
* Retrieve all student records
* Retrieve a specific student by ID
* Update student information
* Delete student records
* Verify API operations using suitable sample data

---

# ☁️ AWS Services Used

| AWS Service            | Role in the Project                            |
| ---------------------- | ---------------------------------------------- |
| **Amazon API Gateway** | Exposes HTTP API endpoints to clients          |
| **AWS Lambda**         | Executes backend application logic             |
| **Amazon DynamoDB**    | Stores student records                         |
| **AWS IAM**            | Provides required permissions to AWS resources |
| **Amazon CloudWatch**  | Provides Lambda monitoring and execution logs  |

---

# 🏗️ Architecture & Request Flow

The request flow of the application is:

```text
1. Client sends an HTTP request
              │
              ▼
2. Amazon API Gateway receives the request
              │
              ▼
3. API Gateway invokes AWS Lambda
              │
              ▼
4. Lambda processes the CRUD operation
              │
              ▼
5. Lambda reads/writes data in DynamoDB
              │
              ▼
6. API response is returned to the client
```

### CRUD Flow

```text
POST   → Create Student
GET    → Read Students
PUT    → Update Student
DELETE → Delete Student
```

---

# ⚙️ AWS Configuration

## AWS Region

```text
US East (N. Virginia)
Region: us-east-1
```

## Lambda Function

```text
Function Name:
StudentManagementFunction
```

## DynamoDB

```text
Table Name:
StudentTable

Partition Key:
id

Capacity Mode:
On-Demand
```

## API Gateway

```text
API Name:
StudentManagementAPI

API Type:
HTTP API
```

---

# 🔗 API Reference

## Base URL

```text
https://78rg6h77qi.execute-api.us-east-1.amazonaws.com
```

## Available Endpoints

|  Method  | Endpoint         | Description                |
| :------: | ---------------- | -------------------------- |
|  `POST`  | `/students`      | Create a new student       |
|   `GET`  | `/students`      | Retrieve all students      |
|   `GET`  | `/students/{id}` | Retrieve a student by ID   |
|   `PUT`  | `/students/{id}` | Update student information |
| `DELETE` | `/students/{id}` | Delete a student           |

---

# 🧪 API Testing

All API operations were tested using **Git Bash and cURL** with suitable sample student data.

---

## 1. ➕ Create Student

### Endpoint

```text
POST /students
```

### Sample Request

```json
{
  "id": "101",
  "name": "Atharv Pawar",
  "age": 21,
  "course": "AWS Cloud",
  "email": "atharvpawar1506@gmail.com"
}
```

### cURL Command

```bash
curl -X POST "https://78rg6h77qi.execute-api.us-east-1.amazonaws.com/students" \
-H "Content-Type: application/json" \
-d '{"id":"101","name":"Atharv Pawar","age":21,"course":"AWS Cloud","email":"atharvpawar1506@gmail.com"}'
```

### Result

The student record was successfully created and stored in DynamoDB.

### 📸 Evidence

![POST Create Student](Screenshots/01-post.jpg)

---

# 2. 📋 Retrieve All Students

### Endpoint

```text
GET /students
```

### cURL Command

```bash
curl -X GET "https://78rg6h77qi.execute-api.us-east-1.amazonaws.com/students"
```

### Result

The API successfully retrieved student records stored in DynamoDB.

### 📸 Evidence

![GET All Students](Screenshots/02-get-all.jpg)

---

# 3. 🔍 Retrieve Student by ID

### Endpoint

```text
GET /students/101
```

### cURL Command

```bash
curl -X GET "https://78rg6h77qi.execute-api.us-east-1.amazonaws.com/students/101"
```

### Result

The API successfully retrieved the student record with ID `101`.

### 📸 Evidence

![GET Student by ID](Screenshots/03-get-by-id.jpg)

---

# 4. ✏️ Update Student

### Endpoint

```text
PUT /students/101
```

### Updated Data

```json
{
  "name": "Atharv Pawar",
  "age": 22,
  "course": "AWS DevOps",
  "email": "atharvpawar1506@gmail.com"
}
```

### cURL Command

```bash
curl -X PUT "https://78rg6h77qi.execute-api.us-east-1.amazonaws.com/students/101" \
-H "Content-Type: application/json" \
-d '{"name":"Atharv Pawar","age":22,"course":"AWS DevOps","email":"atharvpawar1506@gmail.com"}'
```

### Result

The existing student record was successfully updated in DynamoDB.

### 📸 Evidence

![PUT Update Student](Screenshots/04-put-update.jpg)

---

# 5. 🗑️ Delete Student

### Endpoint

```text
DELETE /students/101
```

### cURL Command

```bash
curl -X DELETE "https://78rg6h77qi.execute-api.us-east-1.amazonaws.com/students/101"
```

### Result

Student `101` was successfully deleted from DynamoDB.

### 📸 Evidence

![DELETE Student](Screenshots/05-delete.jpg)

---

# 6. ✅ Verify Deletion

After deleting student `101`, the GET API was executed again to verify that the record was successfully removed.

### Endpoint

```text
GET /students
```

### cURL Command

```bash
curl -X GET "https://78rg6h77qi.execute-api.us-east-1.amazonaws.com/students"
```

### Result

The API was used to verify that student `101` was removed successfully.

### 📸 Evidence

![Final GET](Screenshots/06-final-get.jpg)

---

# 📊 CRUD Testing Summary

| Operation          | HTTP Method | Endpoint        |    Status    |
| ------------------ | :---------: | --------------- | :----------: |
| Create Student     |    `POST`   | `/students`     | ✅ Successful |
| Read All Students  |    `GET`    | `/students`     | ✅ Successful |
| Read Student by ID |    `GET`    | `/students/101` | ✅ Successful |
| Update Student     |    `PUT`    | `/students/101` | ✅ Successful |
| Delete Student     |   `DELETE`  | `/students/101` | ✅ Successful |
| Verify Deletion    |    `GET`    | `/students`     | ✅ Successful |

---

# 📸 AWS Implementation Evidence

## Amazon DynamoDB

The DynamoDB table is responsible for persistent storage of student records.

### Configuration

```text
Table Name    : StudentTable
Partition Key : id
Capacity Mode : On-Demand
```

![DynamoDB Student Table](Screenshots/07-dynamodb.jpg)

---

## AWS Lambda

AWS Lambda contains the backend logic that processes API Gateway requests and performs CRUD operations on DynamoDB.

### Function

```text
StudentManagementFunction
```

![AWS Lambda Function](Screenshots/08-lambda.jpg)

---

## Amazon API Gateway

API Gateway provides the HTTP endpoints that expose the student management functionality.

### Configured Routes

```text
POST   /students
GET    /students
GET    /students/{id}
PUT    /students/{id}
DELETE /students/{id}
```

![API Gateway](Screenshots/09-api-gateway.jpg)

---

# 📁 Project Structure

```text
student-management-api/
│
├── lambda_function.py
├── README.md
├── .gitignore
│
└── Screenshots/
    ├── 01-post.jpg
    ├── 02-get-all.jpg
    ├── 03-get-by-id.jpg
    ├── 04-put-update.jpg
    ├── 05-delete.jpg
    ├── 06-final-get.jpg
    ├── 07-dynamodb.jpg
    ├── 08-lambda.jpg
    └── 09-api-gateway.jpg
```

---

# 🔐 Security Considerations

* AWS IAM permissions are used to control access between AWS services.
* Sensitive credentials must not be stored in the GitHub repository.
* Environment files such as `.env` should be excluded using `.gitignore`.
* AWS access keys and secret keys should never be hard-coded in application code.

---

# 💡 Key Learning Outcomes

Through this project, the following AWS concepts were implemented:

* Serverless application architecture
* AWS Lambda function development
* API Gateway HTTP APIs
* DynamoDB data storage
* CRUD API implementation
* IAM permissions
* API testing using cURL
* Git and GitHub project management
* AWS service integration

---

# 🏁 Final Result

The **Serverless Student Management API** was successfully implemented using:

```text
Amazon API Gateway
        +
AWS Lambda
        +
Amazon DynamoDB
```

The application successfully performs all required student management operations:

**Create → Read → Update → Delete**

All APIs were tested using suitable sample data through Git Bash, and the implementation was verified using AWS Console evidence.

---

# 🛠️ Technology Stack

```text
Language       : Python
API            : Amazon API Gateway
Compute        : AWS Lambda
Database       : Amazon DynamoDB
Monitoring     : Amazon CloudWatch
Security       : AWS IAM
Testing        : Git Bash / cURL
Version Control: Git / GitHub
Region         : us-east-1
```

---

# 👨‍💻 Author

## Atharv Pawar

**Project:** Serverless Student Management API
**Platform:** Amazon Web Services (AWS)

---

## ⭐ Project Highlights

```text
✓ Fully Serverless Architecture
✓ RESTful CRUD APIs
✓ AWS Lambda Backend
✓ DynamoDB Persistent Storage
✓ API Gateway Integration
✓ Git Bash API Testing
✓ Complete CRUD Verification
✓ AWS Console Implementation Evidence
```
