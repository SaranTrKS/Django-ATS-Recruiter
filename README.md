# Django-ATS-Recruiter
# Candidate Management API

A Django REST Framework application for managing candidate information. This application allows for creating, reading, updating, and deleting candidate records, as well as advanced name-based searching with relevancy ranking.

## Features

- **Candidate Management**: Full CRUD operations for candidate records
- **Advanced Search**: Name-based search with relevancy ranking
- **RESTful API**: Follows REST principles with proper HTTP methods and status codes
- **Data Validation**: Custom validation for email and phone number formats

## API Endpoints

### Candidate Management

- **GET /api/candidates/**: List all candidates
- **POST /api/candidates/**: Create a new candidate
- **GET /api/candidates/{id}/**: Retrieve a specific candidate
- **PUT /api/candidates/{id}/**: Update a candidate (full update)
- **PATCH /api/candidates/{id}/**: Update a candidate (partial update)
- **DELETE /api/candidates/{id}/**: Delete a candidate

### Search Functionality

- **GET /api/candidates/search/?q={query}**: Search candidates by name with relevancy ranking
  - Results are sorted by the number of matching words in the search query
  - Example: `/api/candidates/search/?q=Ajay Kumar Yadav` would return candidates with names containing any of these words, with candidates matching more words ranked higher

## Candidate Model

The Candidate model includes the following fields:

- **name**: Candidate's full name (max 100 characters)
- **age**: Positive integer representing candidate's age
- **gender**: One of 'M' (Male), 'F' (Female), or 'O' (Other)
- **email**: Unique email address
- **phone_number**: Phone number (validated to contain only digits or start with +)
- **created_at**: Auto-populated timestamp when record is created
- **updated_at**: Auto-updated timestamp when record is modified

## Search Implementation

The search functionality uses Django ORM features to:
1. Find candidates with names matching any words in the search query
2. Calculate a relevancy score based on how many search words match each name
3. Sort results by relevancy (highest first)

All filtering and sorting is done at the database level using Django's ORM (Q objects, Case expressions, and annotations) for maximum efficiency.

## Setup and Installation

1. Clone the repository:
   ```bash
   git clone https://github.com/yourusername/candidate-management-api.git
   cd candidate-management-api
   ```

2. Create and activate a virtual environment:
   ```bash
   python -m venv venv
   source venv/bin/activate  # On Windows: venv\Scripts\activate
   ```

3. Install dependencies:
   ```bash
   pip install -r requirements.txt
   ```

4. Run migrations:
   ```bash
   python manage.py migrate
   ```

5. Start the development server:
   ```bash
   python manage.py runserver
   ```

## Testing the API

You can test the API using curl, or any other HTTP client:

### Creating a Candidate
```bash
curl -X POST http://localhost:8000/api/candidates/ \
  -H "Content-Type: application/json" \
  -d '{"name": "Ajay Kumar Yadav", "age": 30, "gender": "M", "email": "ajay@example.com", "phone_number": "1234567890"}'
```

### Searching for Candidates
```bash
curl "http://localhost:8000/api/candidates/search/?q=Ajay Kumar"
```

