fastapi-openai-sample
=====================

FastAPI sample application using OpenAI API

[![Test](https://github.com/dceoy/fastapi-openai-sample/actions/workflows/test.yml/badge.svg)](https://github.com/dceoy/fastapi-openai-sample/actions/workflows/test.yml)

Usage
-----

1.  Create `.env` file for configuration.

    ```sh
    $ cp example.env .env
    $ vi .env   # => edit
    ```

2.  Run servers using Docker Compose.

    ```sh
    $ docker-compose up -d
    ```

3.  Try the API to suggest dinner menus based on a given ingredient.

    ```sh
    $ curl -sSX POST http://127.0.0.1:8000/?ingredient=tomato
    ```
