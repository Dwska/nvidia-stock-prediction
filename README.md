# Project Setup and Usage Guide
- This project run locally and you need Docker to run it.
- The files to initialize the container are in the root folder

## Project Directory Structure
```sh
  C:.
  |   docker-compose.yaml
  |   
  +---docker
  |       Dockerfile
  |       Dockerfile.jupyter
  |       
  \---notebook
```

## Getting Started
1. **Build and Start Containers**:
- Open your terminal and run the following command to build and start the Docker containers:
   ```sh
   docker-compose up -d
   ```
2. **Access MinIO UI**:
- Open your web browser and navigate to [http://localhost:9000](http://localhost:9000).
- Log in with the MinIO credentials(you can find it the Docker-Compose.YAML).
- Create two buckets: mlflow and stocks.
- Add data versioning to the stocks bucket.

3. **Prepare Jupyter Notebook**:
- The notebook directory will initially be empty.
- Access Jupyter Lab by navigating to [http://localhost:8888](http://localhost:8888) in your web browser.
- In Jupyter Lab, place your scripts in the "work" folder inside the Jupyter environment.

4. **Track Models with MLflow**:
- In your Jupyter notebook scripts, include code to track your models with MLflow.
- After running your script, you can check the experiment results in the MLflow UI by navigating to [http://localhost:5000](http://localhost:5000).

