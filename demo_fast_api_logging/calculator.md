# Demo Calculator-Fast-API + Logging

In this demo, you will be able to deploy a simple calculator with 4 basic operations (+, -, * and /) using Fast API.

The Logging feature is also included, check the [main.py](src/main.py) module to inspect the logging code.

## Setup

* Create a virtual environment with:

    ```bash
    python3 -m venv venv
    ```

* Activate the virtual environment

    ```bash
    source venv/bin/activate
    ```

* Install the other libraries
Run the following command to install the libraries/packages.

    ```bash
    pip install -r requirements.txt
    ```

## Run FastAPI

* Change to the [demo_fast_api](.) directory
* Run next command to start calculator api locally

    ```bash
    uvicorn src.main:app --reload
    ```

## Checking endpoints

1. Access `http://127.0.0.1:8000/`, you will see a message like this `"Calculator is all ready to go!"`
2. A file called `main_fast_api.log` will be created automatically.
3. Access `http://127.0.0.1:8000/docs`, the browser will display something like this:
    ![FastAPI Docs](./imgs/fast-api-docs.png)
4. Open the [main_fast_api.log](main_fast_api.log) file and check a log saved similar to this:

    ```log
    2023-08-15 16:29:20,286:src.main:main:INFO:Healthy was checked.
    ```

5. Try running the sum endpoint by writing the values `3` and `5`, you will get the response body as follows

    **Response body**

    ```bash
    {
    "resultado": 8
    }
    ```

    ![sum](./imgs/sum.png)

6. Open the [main_fast_api.log](main_fast_api.log) file again and check another log saved similar to this:

    ```log
    2023-08-15 16:29:20,286:src.main:main:INFO:Healthy was checked.
    2023-08-15 16:31:40,162:src.main:main:DEBUG:resultado sum: 11
    ```

### Individual deployment of the API with Docker and usage

#### Build the image

* Ensure you are in the `demo_fast_api_logging` directory (root folder).
* Run the following code to build the image:

    ```bash
    docker build -t demo_fast_api-image src/
    ```

* Inspect the image created by running this command:

    ```bash
    docker images
    ```

    Output:

    ```bash
    REPOSITORY            TAG       IMAGE ID       CREATED          SIZE
    demo_fast_api-image   latest    9c2755fa5f2d   31 seconds ago   312MB
    ```

#### Run demo_fast_api REST API

1. Run the next command to start the `demo_fast_api-image` image in a container.

    ```bash
    docker run -d --rm --name demo_fast_api-c -p 8000:8000 demo_fast_api-image
    ```
    
    Output:

    ```bash
    demo_fast_api-image
    8e99c3aa80439e07832f9a480758c9d3baf631476375d7e16f7bec3cc68576b4
    ```

2. Check the container running.

    ```bash
    docker ps -a
    ```

    Output:

    ```bash
    CONTAINER ID   IMAGE               COMMAND                  CREATED          STATUS         PORTS                    NAMES
    f87bc43f127c   demo_fast_api-image   "uvicorn main:app --…"   12 seconds ago   Up 9 seconds   0.0.0.0:8000->8000/tcp   demo_fast_api-c
    ```
