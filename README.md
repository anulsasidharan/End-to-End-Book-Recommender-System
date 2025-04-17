# End-to-End-Book-Recommender-System

![alt text](image.png)

## project architecture diagram

![alt text](image-1.png)

## Types of recommendation systems

![alt text](<Recommendation system catJPG.jpg>)

### 📘 End-to-End Book Recommender System – Workflow Overview

![alt text](E2E_Book_Recommendation_System.jpg)


#### Data Ingestion

- Read raw datasets (e.g., books, users, ratings) from the artifacts/dataset/ directory.

- Utilize the DataIngestion component to load and preprocess data.​

#### Data Transformation

- Clean and merge datasets.

- Perform feature engineering (e.g., compute average ratings, filter popular books).

- Prepare data for recommendation algorithms.​

#### Model Training

- Implement recommendation algorithms (e.g., collaborative filtering, content-based filtering).

- Train models using the processed data.

- Save trained models to the artifacts/ directory.​

#### Model Evaluation

- Evaluate model performance using appropriate metrics (e.g., RMSE, precision, recall).

- Fine-tune models based on evaluation results.​

#### Deployment

- Develop a web application using app.py to serve recommendations.

- Containerize the application using Docker (Dockerfile provided).

- Deploy the application for end-users to interact with.​

#### User Interaction

- Users input their preferences or select books.

- The system provides personalized book recommendations based on user input


### Workflow
- config.yaml
- entity
- config/configuration.py
- components
- pipeline
- main.py
- app.py

## How to run?
### STEPS

### STEP 1. Clone the repository

Open terminal, and execute the git clone command. 

```bash 
git clone https://github.com/anulsasidharan/End-to-End-Book-Recommender-System.git
```

### STEP 2. Create a conda enveronment after opening the repository and activate it

```bash
conda create -n books python =3.12.7 -y
```

```bash
conda activate books
```

### To check the env created or not, just list the conda enveronments. 
    
```bash
conda env list
```

### STEP 3. Install the requirements

```bash
pip install -r requirements.txt
```

To run  the streamlit app
```bash
streamlit run app.py
```


# Streamlit app Docker Image Deployment

## 1. Login with your AWS console and launch an EC2 instance
## 2. Run the following commands

Note: Do the port mapping to this port:- 8501

```bash
sudo apt-get update -y

sudo apt-get upgrade

#Install Docker

curl -fsSL https://get.docker.com -o get-docker.sh

sudo sh get-docker.sh

sudo usermod -aG docker ubuntu

newgrp docker
```

```bash
git clone "your-project"
```

```bash
docker build -t anulsasidharan/bookapp:latest . 
```

```bash
docker images -a  
```

```bash
docker run -d -p 8501:8501 anulsasidharan/bookapp 
```

```bash
docker ps  
```

```bash
docker stop container_id
```

```bash
docker rm $(docker ps -a -q)
```

```bash
docker login 
```

```bash
docker push anulsasidharan/bookapp:latest 
```

```bash
docker rmi anulsasidharan/bookapp:latest
```

```bash
docker pull anulsasidharan/bookapp
```
