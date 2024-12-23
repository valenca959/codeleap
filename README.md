### Person Registration API - Documentation

#### About the Project 🌐
Designed with a RESTful interface, it allows users to register, update, query, and delete personal and career-related information efficiently. 🚀

Key features include:
1. **Person Registration**: Register and manage career details.
2. **Hosts File Modification**: Simplifies local development with domain redirection.
3. **Dockerization**: Streamlines development with containerization.
4. **Automated Testing**: Ensures reliability through rigorous testing.

---

### Features 🔗
- **Registration API**: Add, retrieve, update, and delete career details.
- **Local Development Tools**: Scripts for modifying the hosts file to enable domain redirection.
- **Docker Support**: Easy setup and deployment in isolated environments.
- **Secure HTTPS Access**: Access via custom domain `https://dev.codeleap.co.uk/`.
- **Fallback Access**: Option to access directly via `http://127.0.0.1:8000/`.

---

### Getting Started

#### Prerequisites 🔧
- **Python**: Version 3.6 or higher
- **Docker & Docker Compose**: For containerized environments
- **Git**: To clone the repository
- **Admin Permissions**: Required for modifying the hosts file

#### Installation Steps

1. **Clone the Repository**:
   ```bash
   git clone https://github.com/valenca959/codeleap.git
   cd codelap
   ```

2. **Install Dependencies**:
   ```bash
   pip install -r requirements.txt
   ```

3. **Database Configuration**:
   ```bash
   python manage.py migrate
   ```
   Adjust database settings in `settings.py` if using an external database.

4. **Update Hosts File for Local Development**:
   - On Linux:
     ```bash
     sudo python3 update_host.py dev.codeleap.co.uk 172.19.0.10
     ```
   - On Windows:
     ```bash
     python3 update_hosts_windows.py dev.codeleap.co.uk 172.19.0.10
     ```
     *(Run as Administrator)*

   **Note**: This step enables access via `https://dev.codeleap.co.uk/`. Alternatively, skip this step and use `http://127.0.0.1:8000/`.

5. **Start the Application**:
   ```bash
   docker-compose up --build
   ```

---

### Accessing the API 🌐
- **HTTPS**: https://dev.codeleap.co.uk/careers
- **Fallback**: http://127.0.0.1:8000/careers

---

### API Endpoints 🌍

- **POST /careers**: Register a new person with their career details.
- **GET /careers**: Retrieve a list of all registered people.
- **GET /careers/{id}**: Retrieve details of a person by ID.
- **DELETE /careers/{id}**: Remove a person by ID.

---

### Development ⚖️

#### Running the Project with Docker
1. **Build Docker Image**:
   ```bash
   docker-compose build
   ```

2. **Start Docker Container**:
   ```bash
   docker-compose up
   ```

3. **Stop Containers**:
   ```bash
   docker-compose down
   ```

### Automated Testing 🧬

- **Run Tests**:
  ```bash
    ./manage.py test
  ```
  Ensures the reliability of CRUD operations and other features.

---

### Dockerfile 🛠️

The `Dockerfile` sets up the API with:
- **Python 3.11**
- Dependency installation from `requirements.txt`
- Execution of the Django server

---

### Notes 📑
- Ensure the hosts file resolves `dev.codeleap.co.uk` to `127.0.0.1` or the appropriate container IP.
- Admin/root permissions are essential for modifying system files during setup.


