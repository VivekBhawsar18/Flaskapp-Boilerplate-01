# Flask Factory Boilerplate

A basic Flask app structure to kickstart your projects.

## Structure

- `app.py`: Entry point of the application.
- `config.py`: Configuration file for the Flask app.
- `requirements.txt`: List of Python dependencies.
- `Flaskapp/`
  - `__init__.py`: Initializes the Flask app and extensions.
  - `extensions.py`: File to initialize Flask extensions.
  - `model/`: Folder for database models.
  - `templates/`: Folder for HTML templates.
  - `Test/`: Blueprint folder for testing routes.

## Getting Started

Before running the project, make sure to set the following environment variables:

1. `FLASK_APP='app'`
2. `SQLALCHEMY_DATABASE_URI='YOUR CONNECTION STRING'`
3. `SECRET_KEY='YOUR APP SECRET KEY'`

## Usage

1. Install dependencies: `pip install -r requirements.txt`
2. Set environment variables as mentioned above.
3. Run the Flask app: `flask run`

Feel free to customize and extend this boilerplate for your projects!
