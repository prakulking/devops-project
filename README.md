# Flask Visit Counter — DevOps Project

A simple Python Flask web application containerized with Docker and automated with CI/CD using GitHub Actions. Built as a hands-on DevOps learning project covering containerization, Docker Compose, and automated pipelines.

## What It Does

- Tracks and displays the number of visits to the homepage using a SQLite database
- Exposes a `/status` health-check endpoint
- Runs fully inside a Docker container — no manual Python setup needed

## Tech Stack

| Layer | Technology |
|---|---|
| App | Python, Flask |
| Database | SQLite |
| Containerization | Docker, Docker Compose |
| CI/CD | GitHub Actions |
| Cloud | AWS EC2 (deployment target) |

## Project Structure

```
devops-project/
├── app.py                  # Flask application
├── requirements.txt        # Python dependencies
├── Dockerfile              # Container build instructions
├── docker-compose.yml      # Multi-container orchestration
├── .github/
│   └── workflows/
│       └── ci.yml          # GitHub Actions CI pipeline
└── README.md
```

## Getting Started

### Prerequisites
- Docker Desktop installed
- Git

### Run with Docker Compose (Recommended)

```bash
# Clone the repo
git clone https://github.com/prakulking/devops-project.git
cd devops-project

# Build and start the container
docker-compose up --build

# Visit the app
open http://localhost:5000
```

### Run with Docker only

```bash
docker build -t flask-visit-counter .
docker run -p 5000:5000 flask-visit-counter
```

### Run locally (without Docker)

```bash
pip install -r requirements.txt
python app.py
```

## API Endpoints

| Endpoint | Method | Description |
|---|---|---|
| `/` | GET | Homepage — increments and shows visit count |
| `/status` | GET | Health check — returns `{"status": "running"}` |

## CI/CD Pipeline

Every push to `main` automatically:
1. Checks out the code
2. Builds the Docker image to verify it compiles correctly
3. (Extendable to push to AWS ECR and deploy to EC2)

## What I Learned

- Writing a `Dockerfile` and understanding image layers
- Using `docker-compose.yml` for service orchestration and volume mounting
- Setting up a GitHub Actions CI pipeline triggered on push
- Containerizing a Python Flask app with SQLite persistence
- AWS EC2 as a deployment target for containerized apps