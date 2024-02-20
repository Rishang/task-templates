
## Table of Contents

- [cloudfront:deploy](#cloudfrontdeploy)
    - [summary](#summary)
    - [required variables](#required-variables)
    - [variables](#variables)
- [ecr-build-push](#ecr-build-push)
    - [summary](#summary)
    - [required variables](#required-variables)
    - [variables](#variables)
- [ssm](#ssm)
    - [summary](#summary)
    - [required variables](#required-variables)
- [ecs-deploy](#ecs-deploy)
    - [summary](#summary)
    - [required variables](#required-variables)
    - [variables](#variables)


## cloudfront:deploy

Build the static NPM frountend projects optionally push them to CloudFront

#### Summary

Build the frontend projects and optionally push them to CloudFront
requires:
- **PATH**: The path to the project
- **CF_PUSH**: [default => false] Push to CloudFront
- **CF_DISTRIBUTION_ID**: [optional] The CloudFront distribution ID 
- **CF_S3_BUCKET**: [optional] The S3 bucket to push to
#### Required Variables

- **PATH**
#### Variables

- **BUILD_DIR**: `{{default "build" .BUILD_DIR}}`
- **CF_PUSH**: `{{default "false" .CF_PUSH}}`
- **CF_DISTRIBUTION_ID**: `{{default "" .CF_DISTRIBUTION_ID}}`
- **CF_S3_BUCKET**: `{{default "" .CF_S3_BUCKET}}`


## ecr-build-push

Build and push docker image to ECR

#### Summary

Build and push docker image to ECR
requires:
- **PATH**: The path to the Dockerfile
- **ECR_REPOSITORY**: The name of the ECR repository
#### Required Variables

- **PATH**
- **ECR_REPOSITORY**
#### Variables

- **USE_BUILDX_PUSH**: `{{default "false" .USE_BUILDX_PUSH}}`
- **IMAGE_TAG**: `{{default "latest" .IMAGE_TAG}}`


## ssm

Run a command on a remote server using SSM

#### Summary

Run a command on a remote server using SSM
requires:
- **INSTANCE_ID**: The instance ID
- **COMMAND**: The command to run
#### Required Variables

- **INSTANCE_ID**
- **COMMAND**


## ecs-deploy

Deploy a new task definition to ECS

#### Summary

Deploy a new task definition to ECS
requires:
- CLUSTER: The name of the ECS cluster
- SERVICE: The name of the ECS service
#### Required Variables

- **CLUSTER**
- **SERVICE**
#### Variables



