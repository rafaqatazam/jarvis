# Django LangChain Integration
This Django application integrates LangChain functionalities, allowing you to interact with OpenAI and Anthropic models through a web interface.

## Table of Contents

- [Features](#features)
- [Prerequisites](#prerequisites)
- [Installation](#installation)
- [Configuration](#configuration)
- [Usage](#usage)
  
## Features

- Prompt classification using agents to chose the right tool to respond to the user prompt
- Integration with OpenAI and Anthropic models
- Support for various tools integrated such as Wikipedia search, DuckDuckGo search, and math calculations. Also have the diversity of integrating as many as tools we need
- A simple web interface for interacting with the AI models

## Prerequisites

- Python 3.8+
- Django 3.2+
- OpenAI API key (if using OpenAI model)
- Anthropic API key (if using Anthropic model)

## Installation

1. **Clone the repository:**

    ```sh
    git clone https://github.com/rafaqatazam/jarvis.git
    ```

2. **Create a virtual environment and activate it:**

    ```sh
    python -m venv venv
    source venv/bin/activate
    ```

3. **Install the dependencies:**

    ```sh
    pip install -r requirements.txt

    NOTE: If you encounter installing requirements and facing any error stating about package name 'six' like 'ERROR: Could not install packages due to an OSError: [Errno 2] No such file or directory'
    To fix this, open the requirements.txt file and mention six==1.15.0
    ```

4. **Run database migrations:**

    ```sh
    python manage.py migrate
    ```

5. **Create a superuser (optional):**

    ```sh
    python manage.py createsuperuser
    ```

## Configuration

1. **Set up environment variables:**

    Create a `.env` file in the project root and add the following lines:

    ```env
    ANTHROPIC_API_KEY=your-anthropic-api-key
    OPENAI_KEY=your-openai-api-key
    ```

## Usage

1. **Run the development server:**

    ```sh
    python manage.py runserver
    ```

2. **Access the application:**

    When you run the server it will provide the link to open. Usually it is `http://127.0.0.1:8000/`.

3. **Interact with the AI:**

    Use the web interface to enter prompts and receive responses from the AI.
