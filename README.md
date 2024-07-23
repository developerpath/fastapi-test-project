# Fast API Test Project

A sample project using FastAPI in Python. This project also integrates popular development tools such as Flake8, Black, and Pytest for code linting, formatting, and testing.

## Installation

1. Clone the repository:

    ```shell
    git clone https://github.com/your-username/fastapi-test-project.git
    ```

2. Navigate to the project directory:

    ```shell
    cd fastapi-test-project
    ```

3. Create a virtual environment:

    ```shell
    python -m venv .venv
    ```

4. Activate the virtual environment:

    - On Windows:

        ```shell
        .venv\Scripts\activate
        ```

    - On macOS and Linux:

        ```shell
        source .venv/bin/activate
        ```

5. Install the project dependencies:

    ```shell
    pip install -r requirements.txt
    ```

## Usage

1. Start the FastAPI dev server:

    ```shell
    fastapi dev main.py
    ```

    The server will be running at `http://localhost:8000`.

2. Open your web browser and navigate to `http://localhost:8000/docs` to access the interactive API documentation provided by FastAPI.

## Development

-   Run Flake8 for code linting:

    ```shell
    flake8
    ```

-   Run Black for code formatting:

    ```shell
    black .
    ```

-   Run Pytest for running tests:

    ```shell
    pytest -v
    ```

## Contributing

Please do not contribute any pull requests to this repository. This repository is for educational purposes only.
