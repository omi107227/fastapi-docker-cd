# FastAPI Docker CD

This project demonstrates how to set up a FastAPI application with Docker and GitHub Actions to automate the build and deployment process.

## Table of Contents

- [Installation](#installation)
- [Run Locally](#run-locally)
- [Build and Run Docker Image](#build-and-run-docker-image)
- [GitHub Actions Workflow](#github-actions-workflow)
- [Setup Docker Token and Secrets](#setup-docker-token-and-secrets)

## Installation

1. Clone the repository to your local machine:

    ```bash
    git clone https://github.com/your-username/fastapi-docker-cd.git
    cd fastapi-docker-cd
    ```

2. Install the required dependencies:

    ```bash
    pip install -r requirements.txt
    ```

3. Run the FastAPI app locally:

    ```bash
    uvicorn main:app --reload
    ```

    This will start the FastAPI app at `http://127.0.0.1:8000`.

4. Open the URL `http://127.0.0.1:8000/docs` in your browser to view the automatically generated documentation for your API.

---

## Run Locally

To run the FastAPI app locally without Docker:

1. Install Python and `pip` (if not already installed).
2. Install the dependencies using the following command:

    ```bash
    pip install -r requirements.txt
    ```

3. Run the FastAPI app:

    ```bash
    uvicorn main:app --reload
    ```

    The app will be available at `http://127.0.0.1:8000`.

---

## Build and Run Docker Image

### Step 1: Create a Dockerfile

Make sure your project has a `Dockerfile` at the root. Here’s an example Dockerfile:

```dockerfile
FROM python:3.9

WORKDIR /app

COPY . /app

RUN pip install --no-cache-dir -r requirements.txt

EXPOSE 8000

CMD ["uvicorn", "main:app", "--host", "0.0.0.0", "--port", "8000"]
