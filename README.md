# Gemini SQL Query App

This project is a web application that converts natural language questions into SQL queries using Google Generative AI and executes them on a SQLite database. The application is built using Streamlit for the web interface.

## Features

- Convert natural language questions into SQL queries.
- Execute SQL queries on a SQLite database.
- Display query results in a user-friendly interface.

## Setup and Installation

### Prerequisites

- Python 3.7 or higher
- Google Generative AI API key
- Streamlit
- SQLite

### Installation

1. Clone the repository:

    ```bash
    git clone https://github.com/your-username/gemini-sql-query-app.git
    cd gemini-sql-query-app
    ```

2. Create a virtual environment and activate it:

    ```bash
    python -m venv venv
    source venv/bin/activate  # On Windows, use `venv\Scripts\activate`
    ```

3. Install the required packages:

    ```bash
    pip install -r requirements.txt
    ```

4. Set up your Google Generative AI API key:

    ```bash
    export GOOGLE_API_KEY='your-api-key'  # On Windows, use `set GOOGLE_API_KEY=your-api-key`
    ```

5. Run the application:

    ```bash
    streamlit run app.py
    ```

## Usage

1. Open the web application in your browser.
2. Enter a natural language question in the input field.
3. Click the "Ask the question" button.
4. The application will display the generated SQL query and the results of the query.

## Project Structure

- `app.py`: Main application file.
- `requirements.txt`: List of Python packages required to run the application.
- `data.db`: SQLite database file.
- `README.md`: Project documentation.

## Example

### Input

    How many entries of records are present?

### Generated SQL Query

    SELECT COUNT(*) FROM DATA

### Output

    (4,)
