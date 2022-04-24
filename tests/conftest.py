import json
from pathlib import Path

import psycopg2
import pytest
from lambda_func.post_form import Credentials


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


@pytest.fixture(scope="module")
def db_connection():
    credentials = Credentials(
        user="postgres",
        password="postgres",
        host="localhost",
        port=5432,
        database="postgres",
    )
    connection = psycopg2.connect(**json.loads(credentials.json()))
    connection.set_isolation_level(psycopg2.extensions.ISOLATION_LEVEL_AUTOCOMMIT)
    return connection


@pytest.fixture(scope="module")
def lambda_post_new_salary_entry_event():
    return get_lambda_event(path="./events/post_new_salary_entry.json")
