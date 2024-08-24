### 🐺 Durov

A test task from Hipasus LTD

A core logic is located [here](src/durov/infra/adapters/repos/user.py)

To address the issue of multiple concurrent requests to the /users/{username} endpoint, we implemented a solution using
a dictionary of Future objects. This approach ensures that when multiple requests are made for the same user, they all
share the result of a single database query, rather than issuing separate queries.

### Installation guide

Make sure you have docker installed

### Clone repository

```commandline
git clone https://github.com/ilyas-kalandar/Durov
cd Durov
```

### Create .env file

```commandline
touch .env
```

Example of .env file

```env
DB_URL = "mysql+aiomysql://root:password@db/durov"

LOGGING_LVL = "INFO"
LOGGING_FORMAT = "[%(asctime)s] - |%(levelname)s| - %(message)s"

SERVING_HOST = "0.0.0.0"
SERVING_PORT = 8000
```

### 🚀 Starting project

```commandline
docker-compose up --build db web 
```

### 🧪 Running tests

```commandline
docker-compose up --build tests
```