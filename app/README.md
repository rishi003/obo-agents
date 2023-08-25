# App

## Setting up app locally

1. Create python environment using python version *3.10*

    `conda create -n obo python=3.10`

2. Activate environment

    `conda activate obo`

3. Install required packages

    `pip install -r requirements.txt`

4. RabbitMQ is also required as message broker. You can install it via any method from here [RabbitMQ Installation](https://www.rabbitmq.com/download.html)

5. Use the following command to run the app

    `python cli.py`

    The app should be running locally http://localhost:8000. Swagger docs can be accessed at http://localhost:8000/docs.

## Setting and running app through Docker

ToDo
