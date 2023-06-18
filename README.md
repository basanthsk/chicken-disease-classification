# Chicken Disease Image Classification
This is end-to-end AI/ML project for detection of  chicken diseases using images of poultry fecal as the basis for its detection. In order to diagnose poultry diseases for small- to medium-scale poultry farmers, images of poultry fecal are used. The images are classified as "Coccidiosis", "Healthy", "New Castle Disease", and "Salmonella".

The Python code is developed in a modular design based on the OOPS principle, and DVC is used for model and data monitoring, as well as versioning. The project has been containerized and deployed to AWS and Azure.

To Clone this repository 

```bash
https://github.com/basanthsk/chicken-disease-classification.git
```
To create virtual environment using conda

```bash
cond create -n <name of the venv> python=3.8 -y
```

To install requirements
```bash
pip install -r requirements.txt
```

To lanuch the local api based on flask

```bash 
python app.py
```

### DVC cmd
1. dvc init # initialization of the dvc 
2. dvc repro # to run the pipeline

## AWS CICD Deplyement with github actions
 1. Login to AWS console
 2. create IAM user for deployment
  ```bash
  

1. EC2 access : It is virtual machine

2. ECR: Elastic Container registry to save your docker image in aws
```

Description: About the deployment

```bash
1. Build docker image of the source code

2. Push your docker image to ECR

3. Launch Your EC2 

4. Pull Your image from ECR in EC2

5. Lauch your docker image in EC2
```

Policy:
```bash

1. AmazonEC2ContainerRegistryFullAccess

2. AmazonEC2FullAccess
```
## Create a ECR repo to store/save docker image

```bash
Save the URI: <uri of elastic container registry >
```

## Create EC2 machine (Ubuntu)
To install docker in EC2 Machine
``` bash
#optinal

sudo apt-get update -y

sudo apt-get upgrade

#required

curl -fsSL https://get.docker.com -o get-docker.sh

sudo sh get-docker.sh

sudo usermod -aG docker ubuntu

newgrp docker
```

## To Configure EC2 as self-hosted runner
from the gitbub setting of the repo
```bash
setting > ctions > runner > new self hosted runner > choose os > then run command one by one
```
## Add AWS credential into github secrets

AWS_ACCESS_KEY_ID=

AWS_SECRET_ACCESS_KEY=

AWS_REGION = us-east-1

AWS_ECR_LOGIN_URI = demo>>  <ecr uri>

ECR_REPOSITORY_NAME = simple-app

