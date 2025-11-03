                            Hello Folks! 
Let me introduce you to my CodeChallenge- it seemed basic but it was bit challenging- I did enjoy it tho!


This project demonstrates a modular, audit-friendly infrastructure setup using Terraform, Docker, and CI/CD pipelines. It’s designed to showcase deploy safety, Git hygiene, and interview-ready engineering practices.

---

## Project Overview

- Modular Terraform setup with reusable components
- CI/CD pipeline with gated apply logic.
- Dockerized demo services for local testing and ECS readiness
- Git workflow structured for clarity, traceability, and recovery
- Designed for testing purposes

##  Repo Structure
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
│   └── workflows/           # GitHub Actions CI/CD pipelines
│       ├── build.yml
│       ├── terraform-plan.yml
│       ├── terraform-apply.yml
│       └── deploy-ecr.yml
        └── verify.yml

## 🚀 CI/CD Workflow

Manual plan trigger: Terraform plan is triggered manually to inspect changes
• 	Apply step: Runs after plan is reviewed and confirmed safe
• 	Artifact upload: Stores Terraform plan for audit traceability and reproducibility
This setup supports deploy safety and audit clarity without requiring manual approval gates.

## 🐳 Docker Setup

To run the container locally:

```bash
docker build -t flash-container:yourimagename ./docker
docker run -d -p 8080:80 flash-container:yourimagename

##  Post Deploy

Post-Deploy Verification & Observability
After deployment, this project performs a verification test to confirm that the expected image tag was successfully deployed. This ensures that the container running in ECS matches the intended version and supports audit clarity.
The application resolves publicly over:

- URL:
- https://flashapp.jamesitepin.com
- http://flashapp.jamesitepin.com
- Port: 443 (HTTPS)
This confirms DNS routing, ALB listener configuration, and container health.

CloudWatch Alarm
A CloudWatch alarm was manually configured to monitor CPU utilization:
- Threshold: >80%
- Action: Sends an email notification via SNS
- Purpose: Detects performance spikes and supports proactive incident response
  This validates observability and alerting logic post-deploy.





























