![Test Status](https://github.com/gmunumel/track-list-extractor/actions/workflows/python-tests.yml/badge.svg)

# track-list-extractor

This is a small project to extract track information from https://www.1001tracklists.com/. You only need to provide the url.

## Install Dependencies

Create a virtual environment to store project-related libraries. Run the following command in root folder:

    mkdir .venv

Then run the virtual environment library script with:

    python3 -m venv .venv

Activate the virtual environment:

If you are in Windows:

    .\.venv\Scripts\activate

If you are in Linux:

    source .venv/bin/activate

Then install the libraries:

    pip install -r requirements.txt

## Using Docker

### Build the application (_remove cache_)

```bash
docker build --pull --no-cache -t track-list-extractor .
```

Or with cache:

```bash
docker build -t track-list-extractor .
```

Or using `buildx`:

```bash
docker buildx create --use
docker buildx build --pull --no-cache --load -t track-list-extractor .
```

Using cached build version:

```bash
docker buildx build --load -t track-list-extractor .
```

### Run the application

```bash
docker run --name track-list-extractor -p 5000:5000 track-list-extractor
```

### Remove and run the application

```bash
docker rm track-list-extractor && docker run --name track-list-extractor -p 5000:5000 track-list-extractor
```

### Build and run - one step

```bash
docker build --pull --no-cache -t track-list-extractor . && docker rm track-list-extractor && docker run --name track-list-extractor -p 5000:5000 track-list-extractor
```

### Open container file system

```bash
docker exec -it track-list-extractor /bin/bash
```

### Use the application

```bash
curl -H "Content-Type: application/json" -XPOST "http://localhost:5000/api/v1/tracklist" -d '{"url": "https://www.1001tracklists.com/tracklist/1f00ch3k/sebastien-leger-the-moment-presents-exceptional-trips-gocek-turkey-mixmag-2021-07-04.html"}'

```

## Deploy to AWS ECR

### Authenticate Docker to Amazon ECR repository:

```bash
aws ecr get-login-password --region eu-central-1 | docker login --username AWS --password-stdin 177539010329.dkr.ecr.eu-central-1.amazonaws.com/gminc/track-list-extractor
```

### Build Docker image:

```bash
docker build -t track-list-extractor .
```

### Tag Docker image:

```bash
docker tag track-list-extractor:latest 177539010329.dkr.ecr.eu-central-1.amazonaws.com/gminc/track-list-extractor:latest
```

### Push Docker image to Amazon ECR:

```bash
docker push 177539010329.dkr.ecr.eu-central-1.amazonaws.com/gminc/track-list-extractor:latest
```

## Deploy to Amazon ECS with Fargate

### Obtain your VPC ID:

```bash
aws ec2 describe-vpcs --query 'Vpcs[*].{ID:VpcId,Name:Tags[?Key==`Name`].Value|[0]}' --output table
```

### Obtain your Security Group:

```bash
aws ec2 describe-security-groups --query 'SecurityGroups[*].{ID:GroupId,Name:GroupName}' --output table
```

### Obtain your Subnet ID:

```bash
aws ec2 describe-subnets --query 'Subnets[*].{ID:SubnetId,Name:Tags[?Key==`Name`].Value|[0],VPC:VpcId}' --output table
```

### Create an ECS Cluster

```bash
aws ecs create-cluster --cluster-name track-list-extractor-cluster
```

### Register the Task Definition

Configuration in [task-definition.json](task-definition.json)

```bash
aws ecs register-task-definition --cli-input-json file://task-definition.json
```

### Create a Security Group

Create a security group that allows inbound traffic on port 5000:

```bash
aws ec2 create-security-group --group-name track-list-extractor-sg --description "Security group for track-list-extractor" --vpc-id vpc-0d7eec66411ad376a --query 'GroupId' --output text
```

Authorize the security group:

```bash
aws ec2 authorize-security-group-ingress --group-id sg-068343f9f8caebbf6 --protocol tcp --port 5000 --cidr 0.0.0.0/0
```

### Create a Fargate Service

Configuration in [service-definition.json](service-definition.json)

```bash
aws ecs create-service --cli-input-json file://service-definition.json
```

## Access Flask Application

Once the service is running, you can access your Flask application using the public IP address of the Fargate task. You can find the public IP address in the ECS console under the "Tasks" section of your cluster.

Update the ip with the one used by your task:

```bash
curl -H "Content-Type: application/json" -XPOST "http://52.59.51.162:5000/api/v1/tracklist" -d '{"url": "https://www.1001tracklists.com/tracklist/1f00ch3k/sebastien-leger-the-moment-presents-exceptional-trips-gocek-turkey-mixmag-2021-07-04.html"}'

```

## Redeploy image

```bash
# Authenticate Docker to ECR
aws ecr get-login-password --region eu-central-1 | docker login --username AWS --password-stdin 177539010329.dkr.ecr.eu-central-1.amazonaws.com

# Build, tag, and push the updated Docker image
docker build -t track-list-extractor .
docker tag track-list-extractor:latest 177539010329.dkr.ecr.eu-central-1.amazonaws.com/gminc/track-list-extractor:latest
docker push 177539010329.dkr.ecr.eu-central-1.amazonaws.com/gminc/track-list-extractor:latest

# Register the new task definition revision
aws ecs register-task-definition --cli-input-json file://task-definition.json

# Update the ECS service to use the new task definition revision
aws ecs update-service --cluster track-list-extractor-cluster --service track-list-extractor-service --task-definition track-list-extractor-task

```

## Clean up

### Delete the service

```bash
aws ecs delete-service --cluster track-list-extractor-cluster --service track-list-extractor-service --force

```

### Delete the cluster

```bash
aws ecs delete-cluster --cluster track-list-extractor-cluster

```

## Run the application locally

Running the app:

```bash
python src/run.py
```

Produces the output similar to this:

```
{
        "name": "Sébastien Léger @ The Moment Presents: Exceptional Trips, Göcek, Turkey (Mixmag) 2021-07-04",
        "pretty_print": "Sébastien Léger @ The Moment Presents: Exceptional Trips, Göcek, Turkey (Mixmag) 2021-07-04\n===========================================================================================\n01. Budakid - Astray In Woodland\n02. [00:05:00] Sébastien Léger - Son Of Sun [ALL DAY I DREAM]\n03. [00:11:45] Shai T - One Night In Paris [LOST MIRACLE]\n04. [00:17:30] Simone Vitullo & Tanit - Priroda (Greg Ochman Remix) [GO DEEVA]\n05. [00:23:00] Sébastien Léger - Regina Blue [ALL DAY I DREAM]\n06. [00:29:00] Sébastien Léger - Lava [ALL DAY I DREAM]\n07. [00:35:00] Sébastien Léger - Feel [ALL DAY I DREAM]\n08. [00:42:00] Eli Nissan - Lyla [LOST MIRACLE]\n09. [00:48:00] Raw Main - Sacré Coeur [LOST MIRACLE]\n10. [00:54:00] Cypherpunx ft. Sian Evans - Alien (Sébastien Léger Remix) [RENAISSANCE]\n11. [01:02:00] Eli Nissan - Casablanca [LOST MIRACLE]\n12. [01:08:00] Roy Rosenfeld - Force Major [LOST & FOUND]\n13. [01:14:00] Roy Rosenfeld - Tuti [LOST MIRACLE]\n14. [01:19:30] Ólafur Arnalds - Saman (Sébastien Léger Remix)\n\n Source: https://www.1001tracklists.com/tracklist/1f00ch3k/sebastien-leger-the-moment-presents-exceptional-trips-gocek-turkey-mixmag-2021-07-04.html",
        "source": "https://www.1001tracklists.com/tracklist/1f00ch3k/sebastien-leger-the-moment-presents-exceptional-trips-gocek-turkey-mixmag-2021-07-04.html",
        "total_tracks": "14",
        "tracks": [
            {
                "id": "tlp0_labeldata",
                "name": "Budakid - Astray In Woodland",
                "number": "01",
            },
            {
                "id": "tlp1_labeldata",
                "label": "ALL DAY I DREAM",
                "name": "Sébastien Léger - Son Of Sun",
                "number": "02",
                "time": "[00:05:00]",
            },
            {
                "id": "tlp2_labeldata",
                "label": "LOST MIRACLE",
                "name": "Shai T - One Night In Paris",
                "number": "03",
                "time": "[00:11:45]",
            },
            {
                "id": "tlp3_labeldata",
                "label": "GO DEEVA",
                "name": "Simone Vitullo & Tanit - Priroda (Greg Ochman Remix)",
                "number": "04",
                "time": "[00:17:30]",
            },
            {
                "id": "tlp4_labeldata",
                "label": "ALL DAY I DREAM",
                "name": "Sébastien Léger - Regina Blue",
                "number": "05",
                "time": "[00:23:00]",
            },
            {
                "id": "tlp5_labeldata",
                "label": "ALL DAY I DREAM",
                "name": "Sébastien Léger - Lava",
                "number": "06",
                "time": "[00:29:00]",
            },
            {
                "id": "tlp6_labeldata",
                "label": "ALL DAY I DREAM",
                "name": "Sébastien Léger - Feel",
                "number": "07",
                "time": "[00:35:00]",
            },
            {
                "id": "tlp7_labeldata",
                "label": "LOST MIRACLE",
                "name": "Eli Nissan - Lyla",
                "number": "08",
                "time": "[00:42:00]",
            },
            {
                "id": "tlp8_labeldata",
                "label": "LOST MIRACLE",
                "name": "Raw Main - Sacré Coeur",
                "number": "09",
                "time": "[00:48:00]",
            },
            {
                "id": "tlp9_labeldata",
                "label": "RENAISSANCE",
                "name": "Cypherpunx ft. Sian Evans - Alien (Sébastien Léger Remix)",
                "number": "10",
                "time": "[00:54:00]",
            },
            {
                "id": "tlp10_labeldata",
                "label": "LOST MIRACLE",
                "name": "Eli Nissan - Casablanca",
                "number": "11",
                "time": "[01:02:00]",
            },
            {
                "id": "tlp11_labeldata",
                "label": "LOST & FOUND",
                "name": "Roy Rosenfeld - Force Major",
                "number": "12",
                "time": "[01:08:00]",
            },
            {
                "id": "tlp12_labeldata",
                "label": "LOST MIRACLE",
                "name": "Roy Rosenfeld - Tuti",
                "number": "13",
                "time": "[01:14:00]",
            },
            {
                "id": "tlp13_labeldata",
                "name": "Ólafur Arnalds - Saman (Sébastien Léger Remix)",
                "number": "14",
                "time": "[01:19:30]",
            },
        ],
    }
```

## Test

To run all tests

```
pytest -v
```
