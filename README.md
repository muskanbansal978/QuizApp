# QuizApp
This repo contains backend of a QuizApp created with the help of FastAPI and Postgres and containerized via Docker

<h2>Project Description</h2>
This project is a template for building a FastAPI application with a PostgreSQL database, using Docker for containerization. It provides a basic setup that includes:
A FastAPI backend for handling API requests.
A PostgreSQL database for data storage.
Docker and Docker Compose for easy deployment.

<h2>Features</h2>
FastAPI: A modern, fast (high-performance), web framework for building APIs with Python.
PostgreSQL: A powerful, open-source object-relational database system.
Dockerized Setup: Easily deployable using Docker and Docker Compose.
Environment Configuration: Uses environment variables for easy configuration.

<h2>Installation and Setup</h2>
<h3>Prerequisites</h3>
Docker

Docker Compose

<h3>Steps to Set Up the Project</h3>

<h4>Clone the repository:</h4>
git clone https://github.com/your-username/fastapi-postgresql.git

cd fastapi-postgresql

<h4>Create a .env file:</h4>

Create a .env file in the root directory with the following content:

POSTGRES_USER=your_username

POSTGRES_PASSWORD=your_password

POSTGRES_DB=your_db

<h4>Build and run the containers:</h4>

Run the following command to build the Docker images and start the containers:
docker-compose up --build
This will start the FastAPI application and PostgreSQL database.

<h4>Access the application:</h4>

Open your web browser and navigate to http://localhost:8000 to access the FastAPI application.

<h4>API Documentation:</h4>

FastAPI automatically generates documentation for your API. You can access it at http://localhost:8000/docs (Swagger UI) or http://localhost:8000/redoc (ReDoc).

<h3>Usage</h3>
Interacting with the API:
You can interact with the API using tools like Postman or curl.

<h4>Example:</h4>

curl -X GET "http://localhost:8000/your-endpoint" -H "accept: application/json"

<h3>Configuration</h3>
Database Configuration:
The PostgreSQL database is configured through the .env file. 

Update the POSTGRES_USER, POSTGRES_PASSWORD, and POSTGRES_DB values as needed.

<h3>API Endpoints</h3>
Here are the default endpoints provided by the application:



GET / - Root endpoint (can be used for health checks).

POST /items/ - Example of creating an item.

GET /items/ - Retrieve items.

(Add any other relevant endpoints with descriptions.)

<h3>Contributing</h3>
Contributions are welcome! Please open an issue or submit a pull request with your changes.

<h3>License</h3>
This project is licensed under the MIT License. See the LICENSE file for details.





