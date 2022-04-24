import pytest
from pathlib import Path
import json
import psycopg2


def get_lambda_event(path: str) -> dict:
    """
    Returns the Lambda event used for testing from the generated events within /events
    Args:
        path: path to the event json file to be used
    """
    event_path = Path(path)
    try:
        with open(event_path) as f:
            event = json.load(f)
        return event
    except Exception as e:
        raise e


def get_db_credentials() -> dict:
    """
    Creates the credentials needed to connect to the local postgres db for
    testing purposes
    """
    return dict(
        user="postgres",
        host="localhost",
        database="postgres",
        password="postgres",
        port=5432,
    )


@pytest.fixture(scope="module")
def db_connection():
    credentials = get_db_credentials()
    connection = psycopg2.connect(**credentials)
    connection.set_isolation_level(psycopg2.extensions.ISOLATION_LEVEL_AUTOCOMMIT)
    return connection


@pytest.fixture(scope="module")
def lambda_post_new_salary_entry_event():
    return get_lambda_event(path="./events/post_new_salary_entry.json")
