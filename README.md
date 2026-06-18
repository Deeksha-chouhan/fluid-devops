# 🚀 Fluid DevOps Platform

## Project Overview

This project was developed as part of the Fluid AI DevOps Engineer Infrastructure Challenge.

The objective was to build and deploy a production-style application stack demonstrating:

- Containerization
- Kubernetes Deployment
- CI/CD Automation
- Observability
- Operational Debugging

The application consists of a Flask backend connected to Redis and deployed on a K3s Kubernetes cluster running on AWS EC2.

---

## Architecture

```text
Developer
    │
    ▼
GitHub Repository
    │
    ▼
GitHub Actions CI/CD
    │
    ▼
Docker Image Build
    │
    ▼
Docker Hub
    │
    ▼
K3s Kubernetes Cluster (AWS EC2)
    │
 ┌──┴──┐
 ▼     ▼
Flask  Redis
 App   Cache
    │
    ▼
NodePort Service
    │
    ▼
End Users
```

---

## Tech Stack

- AWS EC2
- Docker
- Kubernetes (K3s)
- GitHub Actions
- Python Flask
- Redis
- Git & GitHub
- Amazon Linux 2023

---

## Application Features

- Flask web application
- Redis-backed visit counter
- Health endpoint (`/health`)
- Dockerized deployment
- Kubernetes orchestration
- CI/CD automation using GitHub Actions
- Rolling updates
- Failure simulation and recovery

---

## Docker

Build Docker image:

```bash
docker build -t fluid-app:v1 .
```

Run locally:

```bash
docker run -p 5000:5000 fluid-app:v1
```

---

## Kubernetes Deployment

Deploy Redis:

```bash
kubectl apply -f redis-deployment.yaml
kubectl apply -f redis-service.yaml
```

Deploy Application:

```bash
kubectl apply -f app-deployment.yaml
kubectl apply -f app-service.yaml
```

Verify:

```bash
kubectl get pods
kubectl get svc
kubectl get deployments
```

---

## CI/CD Pipeline

The GitHub Actions pipeline performs:

1. Source Code Checkout
2. Docker Image Build
3. Docker Image Push
4. Kubernetes Deployment Update
5. Rolling Deployment

Pipeline Flow:

```text
Git Push
   │
   ▼
GitHub Actions
   │
   ▼
Docker Build
   │
   ▼
Docker Hub Push
   │
   ▼
Kubernetes Deploy
```

---

## Health Monitoring

Health endpoint:

```bash
/health
```

Response:

```json
{
  "status": "healthy"
}
```

Used for application monitoring and operational validation.

---

## Reliability Improvement

Implemented Health Monitoring Endpoint.

Benefits:

- Early failure detection
- Better observability
- Faster troubleshooting
- Production readiness

---

## Failure Simulation

Simulated Redis connectivity failure by modifying:

```yaml
REDIS_HOST=invalid-host
```

Observed application failure through logs and Kubernetes diagnostics.

Debugging Commands:

```bash
kubectl logs <pod-name>

kubectl describe pod <pod-name>

kubectl get svc
```

Recovery:

```bash
kubectl rollout restart deployment fluid-app
```

Application recovered successfully.

---

## DevOps Concepts Demonstrated

- Docker Containerization
- Kubernetes Deployments
- Service Discovery
- CI/CD Automation
- Rolling Updates
- Health Monitoring
- Operational Debugging
- Infrastructure Management
- High Availability

---

## Outcome

Successfully built and deployed a production-style application stack on Kubernetes with automated deployment, observability, and operational debugging workflows.

This project demonstrates practical DevOps skills in Docker, Kubernetes, CI/CD, cloud infrastructure, monitoring, and troubleshooting.

---

## Author

**Deeksha Chouhan**

GitHub: https://github.com/Deeksha-chouhan
