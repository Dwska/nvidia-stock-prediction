# Project Setup and Usage Guide
- This project runs locally and you need Docker to run it.
- The files to initialize the container are in the docker directory

## Project Directory Structure
```sh
  ├── .github/
  │   └── workflows/
  │       └── ci.yml
  ├── docker/
  │   ├── Dockerfile.jupyter
  │   └── Dockerfile.mlflow
  ├── notebook
  │   ├── src/
  │   │   ├── data_processing.py
  │   │   ├── model_training.py
  │   │   └── utils.py
  │   ├── data_summary.ipynb
  │   └── nvidia_reg.ipynb
  ├── tests/
  │   ├── test_data_processing.py
  │   └── test_model_trainin.py
  ├── .env.example
  ├── .gitignore
  ├── docker-compose.yml
  ├── README.md
  ├── requirements-dev.txt
  └── requirements.txt
```

## Getting Started
1. **Clone the Project**

   Open your terminal and run the following command:
   ```bash
    git clone https://github.com/Dwska/nvidia-stock-prediction.git
   ```
   After successful cloning, navigate to the project directory
   ```bash
    cd nvidia-stock-prediction/
   ```
   
3. **Build and Start Containers**

   Run the following command to build and start the Docker containers (make sure your Docker is running):
   ```bash
    docker-compose up --build -d
   ```

4. **Create `.env` File**
   
   Copy this environment variables to be able to run the project (or use your own credentials if present)
   ```.env
    JUPYTER_TOKEN=mlflow
    AWS_ACCESS_KEY_ID=mlflow
    AWS_SECRET_ACCESS_KEY=password
    MLFLOW_S3_ENDPOINT_URL=http://minio:9000
    MINIO_ENDPOINT=http://minio:9000
    MINIO_ACCESS_KEY=mlflow
    MINIO_SECRET_KEY=password
    DB_DATABASE=mlflow
    DB_USERNAME=mlflow
    DB_PASSWORD=secret
    FORWARD_MINIO_PORT=9000
    FORWARD_MINIO_CONSOLE_PORT=8900
    FORWARD_DB_PORT=5432
    MLFLOW_ARTIFACT_BUCKET=mlflow
   ```

5. **Access MinIO UI**:
   - Open your web browser and navigate to [http://localhost:9000](http://localhost:9000).
   - Log in with the MinIO credentials (defined in `.env` file).
   - Create two buckets with these two specific names: ***mlflow*** and ***stocks*** (case sensitive).
   - Enable data versioning to the ***stocks*** bucket.
   - Try to upload [the dataset](https://www.kaggle.com/datasets/jvanark/nvidia-daily-stock-price-data?resource=download) in CSV format

6. **Prepare Jupyter Notebook**:
   - Access Jupyter Lab by navigating to [http://localhost:8888](http://localhost:8888) in your web browser.
   - Log in with the lab token (defined in `.env` file).
   - In Jupyter Lab, the notebooks are in the "work" folder inside the Jupyter environment.
   - To get prediction, run `nvidia_reg.ipynb`. It will download the dataset from MinIO, process the data, and deploy the model to MLflow

7. **Track Models with MLflow**:
   - Access MLflow UI by navigating to [http://localhost:5000](http://localhost:5000) in your web browser.
   - Log in with the MLflow credentials (defined in `.env` file).
   - After running your script, you can check the experiment results and model deployments in the MLflow UI.

