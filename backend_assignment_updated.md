## Django Assignment for Interview Round

### Objective
The goal of this assignment is to assess your ability to design and implement a RESTful API using Django and PostgreSQL. You will create a comprehensive API for an employee management system that allows users to manage employees, departments, projects, and timesheets.

### Duration
The assignment is designed to be completed in 3 days.

### Requirements

1. **Database**: Use PostgreSQL for the database.
2. **API**: Implement the API using Django REST framework.
3. **Documentation**: Provide a comprehensive README file.
4. **Coding Standards**: Follow PEP 8 coding standards.
5. **Testing**: Write test cases using Django's testing framework.
6. **Dockerization**: Provide a Dockerfile and docker-compose.yml to set up the project easily.

### Functional Requirements

1. **Employee Management**
   - Create, Read, Update, and Delete (CRUD) operations for employees.
   - Each employee should have the following fields:
     - First Name (string)
     - Last Name (string)
     - Email (string, unique)
     - Phone Number (string)
     - Department (foreign key to Department)
     - Date of Joining (date)
     - Position (string)
     - Salary (decimal)

2. **Department Management**
   - CRUD operations for departments.
   - Each department should have the following fields:
     - Name (string)
     - Description (text)
     - Location (string)

3. **Project Management**
   - CRUD operations for projects.
   - Each project should have the following fields:
     - Name (string)
     - Description (text)
     - Start Date (date)
     - End Date (date, nullable)
     - Department (foreign key to Department)
     - Employees (many-to-many relationship with Employee)

4. **Timesheet Management**
   - CRUD operations for timesheets.
   - Each timesheet should have the following fields:
     - Employee (foreign key to Employee)
     - Project (foreign key to Project)
     - Date (date)
     - Hours Worked (decimal)
     - Description (text, nullable)

### Non-Functional Requirements

1. **Authentication**: Implement token-based authentication using Django REST framework's TokenAuthentication.
2. **Pagination**: Implement pagination for the list endpoints.
3. **Filtering and Sorting**: Allow filtering and sorting of employees, departments, and projects.
4. **Documentation**: Use Swagger or DRF-YASG for API documentation.

### Project Structure

```plaintext
employee_management/
├── employee_management/
│   ├── __init__.py
│   ├── settings.py
│   ├── urls.py
│   ├── wsgi.py
│   └── asgi.py
├── employees/
│   ├── __init__.py
│   ├── admin.py
│   ├── apps.py
│   ├── models.py
│   ├── serializers.py
│   ├── views.py
│   ├── urls.py
│   └── tests.py
├── departments/
│   ├── __init__.py
│   ├── admin.py
│   ├── apps.py
│   ├── models.py
│   ├── serializers.py
│   ├── views.py
│   ├── urls.py
│   └── tests.py
├── projects/
│   ├── __init__.py
│   ├── admin.py
│   ├── apps.py
│   ├── models.py
│   ├── serializers.py
│   ├── views.py
│   ├── urls.py
│   └── tests.py
├── timesheets/
│   ├── __init__.py
│   ├── admin.py
│   ├── apps.py
│   ├── models.py
│   ├── serializers.py
│   ├── views.py
│   ├── urls.py
│   └── tests.py
├── manage.py
├── Dockerfile
├── docker-compose.yml
└── README.md
```

### README.md

Provide a README.md file with the following sections:

1. **Introduction**: Brief description of the project.
2. **Requirements**: List of required software and dependencies.
3. **Installation**:
   - How to set up the project locally.
   - How to run the project using Docker.
4. **API Documentation**: How to access the API documentation.
5. **Usage**: Example requests for each endpoint.
6. **Testing**: How to run the test cases.

### Coding Standards

- Follow PEP 8 guidelines.
- Use meaningful variable and function names.
- Write docstrings for classes and methods.
- Avoid code duplication.

### Test Cases

Write unit tests and integration tests for:

1. Employees API
   - Test CRUD operations.
   - Test filtering and sorting.
   - Test pagination.

2. Departments API
   - Test CRUD operations.
   - Test filtering and sorting.
   - Test pagination.

3. Projects API
   - Test CRUD operations.
   - Test filtering and sorting.
   - Test pagination.

4. Timesheets API
   - Test CRUD operations.
   - Test timesheet logic.
   - Test filtering and sorting.
   - Test pagination.

### Dockerization

**Dockerfile**:

```dockerfile
# Use the official Python image.
# https://hub.docker.com/_/python
FROM python:3.9-slim

# Set environment variables
ENV PYTHONDONTWRITEBYTECODE 1
ENV PYTHONUNBUFFERED 1

# Set work directory
WORKDIR /code

# Install dependencies
COPY requirements.txt /code/
RUN pip install -r requirements.txt

# Copy project
COPY . /code/
```

**docker-compose.yml**:

```yaml
version: '3.7'

services:
  db:
    image: postgres
    volumes:
      - postgres_data:/var/lib/postgresql/data/
    environment:
      - POSTGRES_DB=employee_management
      - POSTGRES_USER=postgres
      - POSTGRES_PASSWORD=postgres

  web:
    build: .
    command: python manage.py runserver 0.0.0.0:8000
    volumes:
      - .:/code
    ports:
      - "8000:8000"
    depends_on:
      - db

volumes:
  postgres_data:
```

### Submission

1. Push your code to a public GitHub repository.
2. Ensure your repository contains the following:
   - Complete project code
   - README.md
   - Dockerfile
   - docker-compose.yml
3. Share the repository link.

### Evaluation Criteria

- Code quality and adherence to coding standards.
- Correctness and completeness of the implemented features.
- Quality and coverage of test cases.
- Proper use of Docker.
- Clarity and comprehensiveness of the documentation.

#### Note : Above Docker related files are sample. 

Good luck!
