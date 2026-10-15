# DevOps Time Service

A containerized Flask application built to demonstrate practical DevOps workflows, including automated testing, Docker, Kubernetes deployment configuration, Helm, Terraform, and GitOps preparation.

## Architecture

```text
Developer
   |
   v
GitHub Repository
   |
   v
GitHub Actions
   |-- Run application tests
   |-- Build Docker image
   |
   v
Docker Hub
   |
   v
Kubernetes (EKS)
   |
   v
Helm-managed application
   |
   v
Argo CD (GitOps integration planned)
```

## Technology Stack

- **Application:** Python, Flask
- **Testing:** pytest
- **Containerization:** Docker
- **CI:** GitHub Actions
- **Container Registry:** Docker Hub
- **Kubernetes packaging:** Helm
- **Infrastructure as Code:** Terraform
- **Cloud:** AWS EKS
- **GitOps:** Argo CD configuration prepared

## Application Endpoints

| Endpoint | Purpose |
|---|---|
| `/` | Application dashboard |
| `/health` | Health-check endpoint |
| `/api/time` | Time-service API |

## Run Locally

Clone the repository:

```bash
git clone https://github.com/Classiq04/complete-devops-project.git
cd complete-devops-project
```

Create and activate a Python virtual environment:

```bash
python3 -m venv .venv
source .venv/bin/activate
```

Install dependencies and start the application:

```bash
pip install -r requirements.txt
python app.py
```

Run the tests:

```bash
pytest -v
```

## Docker

Build the container image:

```bash
docker build -t classiq04/complete-devops-project:v1 .
```

Run the container:

```bash
docker run --rm -p 8080:8080 classiq04/complete-devops-project:v1
```

The container's application port and local run command should match the port configured by the application.

## Kubernetes and Helm

The Helm chart is located in:

`complete-devops-project-time-printer/`

It contains the Kubernetes deployment and service configuration, including the Docker Hub image reference.

Example chart validation:

```bash
helm lint ./complete-devops-project-time-printer
```

## Continuous Integration

The GitHub Actions workflow is located at:

`.github/workflows/ci.yaml`

It is configured to run application tests and build the Docker image. Publishing images automatically from the workflow is not currently configured.

## Infrastructure as Code

Terraform configurations are maintained in `terraform-configs/` for the AWS infrastructure used by this project.

Review Terraform configuration and costs carefully before creating cloud resources. Destroy resources when they are no longer needed.

## GitOps Roadmap

The repository includes an Argo CD Application manifest (`argocd-app.yaml`) and Terraform configuration under `argocd-configs/`.

The next step is to deploy Argo CD to the Kubernetes cluster, apply the Application manifest, and verify that Argo CD can synchronize the application from Git. This integration is not yet verified as operational.

## Project Status

- [x] Flask application and health/API endpoints
- [x] Docker image built and published to Docker Hub
- [x] Helm chart created
- [x] Terraform configuration committed
- [x] GitHub Actions workflow committed
- [x] Project pushed to GitHub
- [ ] Verify GitHub Actions run succeeds
- [ ] Deploy Argo CD and verify GitOps synchronization
- [ ] Capture deployment evidence and clean up AWS resources

## Repository

https://github.com/Classiq04/complete-devops-project
