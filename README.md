CodeChallenge Deployment
Hello Folks!

Here's an overview of my CodeChallenge project. What seemed straightforward initially turned out to be quite engaging. It was my first experience deploying on ECS, which added a layer of complexity, but I thoroughly enjoyed the process.

This project demonstrates a modular, audit-friendly infrastructure setup using Terraform, Docker, and CI/CD pipelines. It emphasizes deployment safety, Git hygiene, and engineering practices suitable for interview scenarios.


Project Overview
Modular Terraform configuration with reusable components
CI/CD pipeline with gated apply logic for safe deployments
Dockerized demo services for local testing and ECS readiness
Structured Git workflow for clarity, traceability, and recovery
Designed primarily for testing and demonstration purposes

Repository Structure
CODE_CHALLENGE/
├── README.md
├── .gitignore
├── terraform.tfvars
├── backend.tf
├── provider.tf
├── iam.tf
├── data.tf
├── locals.tf
├── output.tf
├── main.tf
├── dev-variables.tf
├── .terraform.lock.hcl
├── .terraform/               # Terraform working directory (ignored)
├── .history/                 # Local history (ignored)
│
├── modules/                 # Reusable Terraform modules
│   ├── LoadBalancer/
│   ├── S3/
│   ├── ecs/
│   ├── testverif/
│   └── ...
│
├── docker/                  # Containerized demo app
│   ├── Dockerfile
│   └── app/
│       ├── flash.py
│       └── requirements.txt
│
├── .github/                 # GitHub-specific config
│   └── workflows/           # CI/CD pipelines
│       ├── build.yml
│       ├── terraform-plan.yml
│       ├── terraform-apply.yml
│       ├── deploy-ecr.yml
│       └── verify.yml

CI/CD Workflow
Manual Plan Trigger: Initiates Terraform plan for inspection before deployment.
Apply Step: Executes after review confirms changes are safe.
Artifact Upload: Stores the Terraform plan for auditability, traceability, and reproducibility.
This setup ensures deployment safety and clear audit trails without manual approval gates.

Docker Setup
To run the demo container locally:
docker build -t flash-container:yourimagename ./docker
docker run -d -p 8080:80 flash-container:yourimagename

Post-Deployment Verification & Monitoring
Post-Deploy Checks: After deployment, the system performs a verification test to ensure the correct image tag was deployed. This guarantees the container running in ECS matches the intended version, supporting audit transparency.

Public Access:

URL: http://flashapp.jamesitepin.com
Port: 443 (HTTP)
This verifies DNS routing, Application Load Balancer (ALB) configuration, and container health.

CloudWatch Alarm:

A manual CloudWatch alarm monitors CPU utilization:

Threshold: >80%
Action: Sends notifications via SNS email
Purpose: Detect performance issues proactively, supporting incident response and observability

ECS Deployment Details
This Flask app is containerized and deployed to Amazon ECS using Fargate. Key configurations include:

Container & Port Configuration
Application Port: 80 (Flask runs on port 80 inside the container)
ECS Task Port Mapping: Container port 80 mapped to host port 80
Health Check: ALB monitors root endpoint for a 200 OK response
Image Details
ECR Image Tag: 279c09 (passed via Terraform -var="image_tag=279c09")
