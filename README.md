---

# Multi-Tier Docker Setup

## Overview
This project demonstrates a multi-tier architecture using Docker:
- **App Image**: Runs a Flask application.
- **Database Image**: Runs a MySQL database.

## Prerequisites
- Docker installed on your system.

## Build Docker Images
1. Create a directory for your project.
2. Place `app.py` and `Dockerfile` in that directory.
3. In the same directory, build the app image:
   ```bash
   docker build -t myapp:latest .  # Creates the app image
   ```
4. Pull the MySQL image from Docker Hub:
   ```bash
   docker pull mysql:latest  # Downloads the MySQL image
   ```
5. Use the following command to verify that both images are available locally:
   ```bash
   docker images  # List all available Docker images
   ```

## Run the Containers

### 1. **Run the MySQL container**
   Run the MySQL container with the necessary environment variables:
   ```bash
   docker run --name mydb -e MYSQL_ROOT_PASSWORD=rootpassword -e MYSQL_DATABASE=awdb -e MYSQL_USER=ashik -e MYSQL_PASSWORD=redhat -d mysql:latest
   ```

### 2. **Access the MySQL container**
   Enter the MySQL container to manage the database:
   ```bash
   docker exec -it mydb bash  # Access the MySQL container
   ```

### 3. **Login to MySQL**
   Log into MySQL using the user credentials:
   ```bash
   mysql -u ashik -p  # Login with user 'ashik' and password 'redhat'
   ```

### 4. **Create Database and Table**
   Once logged in to MySQL, run the following commands to create the database, table, and insert data:
   ```sql
   CREATE DATABASE awdb;
   USE awdb;
   CREATE TABLE students (id INT AUTO_INCREMENT PRIMARY KEY, name VARCHAR(255));
   INSERT INTO students (name) VALUES ('ashik'), ('jhon');
   ```

### 5. **Exit MySQL**
   After creating the table and inserting data, exit MySQL:
   ```bash
   exit
   ```

### 6. **Get MySQL Container's IP Address**
   Use the following command to get the IP address of the MySQL container:
   ```bash
   docker inspect mydb | grep "IPAddress"  # Get the container's IP address
   ```
   **Note**: The IP address may change each time the container is restarted. Update the IP address in your `app.py` if needed.

### 7. **Run the App container**
   Run the Flask app container:
   ```bash
   docker run --name myapp -it myapp:latest
   ```

### 8. **Run the Flask App**
   In the app container, start the Flask application:
   ```bash
   python3 app.py  # Start the Flask app
   ```

## Access the Application
1. Open your browser and go to: 
   - [http://localhost:5000/data](http://localhost:5000/data) 
   - Or, use the IP address of your app container if running on a different network.

2. You should see the content from the `students` table in the database.

---

### Final Notes:
- **Database IP Address**: Every time you restart your MySQL container, the IP address may change. Make sure to update the IP address in the `app.py` file if necessary.
- **Docker Compose**: If you prefer to simplify running both containers, consider using `docker-compose` for managing both the app and database containers together.

---
