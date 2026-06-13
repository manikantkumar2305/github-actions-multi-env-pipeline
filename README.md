# Multi-Environment ECS Deployment Pipeline using GitHub Actions

## Project Overview

This project demonstrates a complete CI/CD pipeline for deploying a containerized application to Amazon ECS using GitHub Actions.

The pipeline follows the **Build Once, Deploy Many** approach:

```text
Build
  ↓
Dev
  ↓
Stage
  ↓
Prod
```

A Docker image is built only once, pushed to Amazon ECR, and then promoted through Dev, Stage, and Production environments.

---

## Architecture

```text
                    GitHub Repository
                           │
                           ▼
                   GitHub Actions
                           │
                           ▼
                 Build Docker Image
                           │
                           ▼
                  Push Image to ECR
                           │
                           ▼
                 Deploy to Dev ECS
                           │
                           ▼
              Approval Gate (Stage)
                           │
                           ▼
                Deploy to Stage ECS
                           │
                           ▼
              Approval Gate (Prod)
                           │
                           ▼
                 Deploy to Prod ECS
```

### Deployment Flow

```text
Build
  ↓
Dev Deployment
  ↓
Stage Approval Gate
  ↓
Stage Deployment
  ↓
Prod Approval Gate
  ↓
Prod Deployment
```

---

## Technologies Used

* GitHub Actions
* Docker
* Amazon ECS (Fargate)
* Amazon ECR
* AWS IAM
* GitHub Environments
* Approval Gates

---

## Key Features

### Multi-Environment Deployment

The pipeline supports:

* Development Environment
* Staging Environment
* Production Environment

Each environment uses its own:

* ECS Cluster
* ECS Service
* ECS Task Definition

---

### Build Once, Deploy Many

The Docker image is built only once.

The image tag is passed between jobs using GitHub Actions outputs and deployed to all environments.

Benefits:

* Consistent deployments
* Faster pipeline execution
* Reduced build time
* Better release management

---

### GitHub Environments

GitHub Environments are used to store environment-specific variables.

Examples:

#### Dev

```text
ECS_CLUSTER=dev-cluster
ECS_SERVICE=dev-service
ECS_TASK_DEFINITION=dev-task-definition.json
```

#### Stage

```text
ECS_CLUSTER=stage-cluster
ECS_SERVICE=stage-service
ECS_TASK_DEFINITION=stage-task-definition.json
```

#### Prod

```text
ECS_CLUSTER=prod-cluster
ECS_SERVICE=prod-service
ECS_TASK_DEFINITION=prod-task-definition.json
```

---

### Approval Gates

Approval Gates are configured using GitHub Environments.

Before deployment to higher environments, manual approval is required.

Example:

```text
Build
  ↓
Dev (Auto Deploy)
  ↓
Stage (Approval Required)
  ↓
Prod (Approval Required)
```

This simulates real-world enterprise deployment workflows where releases must be approved before reaching critical environments.

---

## Workflow Explanation

### Build Job

* Checkout source code
* Configure AWS credentials
* Login to Amazon ECR
* Build Docker image
* Push image to ECR
* Store image tag as workflow output

### Dev Deployment

* Checkout repository
* Configure AWS credentials
* Login to ECR
* Update ECS task definition
* Deploy to Dev ECS Service

### Stage Deployment

* Wait for successful Dev deployment
* Wait for Stage approval
* Deploy the same image to Stage

### Prod Deployment

* Wait for successful Stage deployment
* Wait for Production approval
* Deploy the same image to Production

---

## Repository Structure

```text
.
├── .github
│   └── workflows
│       ├── deploy.yml
│       └── task-definitions
│           ├── dev-task-definition.json
│           ├── stage-task-definition.json
│           └── prod-task-definition.json
│
├── app.py
├── requirements.txt
├── Dockerfile
└── README.md
```

---

## Concepts Demonstrated

* GitHub Actions Workflows
* Job Dependencies (`needs`)
* Job Outputs
* Environment Variables
* GitHub Environments
* Approval Gates
* Docker Build & Push
* Amazon ECR
* Amazon ECS
* ECS Task Definitions
* Multi-Environment Deployments
* Build Once Deploy Many Strategy
* CI/CD Troubleshooting

---

## Challenges Solved During Development

### GitHub Output Secret Masking

Issue:

```text
Skip output 'image' since it may contain secret
```

Solution:

Passed only the image tag between jobs and reconstructed the full image URI during deployment.

---

### ECS Task Definition Validation Errors

Issue:

```text
Unexpected key 'enableFaultInjection'
```

Solution:

Removed ECS-generated metadata fields such as:

* taskDefinitionArn
* revision
* status
* requiresAttributes
* compatibilities
* registeredAt
* registeredBy
* enableFaultInjection
* tags

---

## Learning Outcomes

This project helped in understanding:

* End-to-end CI/CD pipelines
* ECS deployment automation
* GitHub Actions job outputs
* Environment-specific deployments
* Approval workflows
* AWS container deployment strategies
* Real-world DevOps troubleshooting

---

## Future Enhancements

* OIDC Authentication
* Terraform Infrastructure Provisioning
* Blue/Green Deployments
* Automated Rollbacks
* Reusable GitHub Workflows
* Security Scanning
* Slack Notifications

---

## Author

**Manikant Kumar**

DevOps | AWS | Docker | GitHub Actions | ECS | ECR
