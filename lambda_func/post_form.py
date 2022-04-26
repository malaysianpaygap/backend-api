import base64
import json

import boto3
import psycopg2.extras
from botocore.exceptions import ClientError
from pydantic import BaseModel
from pydantic import SecretStr

SECRET_NAME = "rds-write-insert-salary-test"  # nosec


class Credentials(BaseModel):
    """
    Credentials derived from AWS Secrets Manager to establish a connection
    to the RDS postgresql database
    """

    user: SecretStr
    password: SecretStr
    host: str
    database: str
    port: int

    class Config:
        """
        Allows SecretStr to be read when converted to json
        """

        json_encoders = {SecretStr: lambda v: v.get_secret_value() if v else None}


def get_aws_secret(
    secret_name: str,
    region_name: str = "ap-southeast-1",
) -> dict:
    """
    Get the secret object from AWS Secret Manager
    Args:
        secret_name: the name of the secret to fetch
        region_name: the region the secret is located at
    """
    if not secret_name:
        raise ValueError("No secret name was passed!")

    client = boto3.client(
        service_name="secretsmanager",
        region_name=region_name,
    )

    try:
        get_secret_value_response = client.get_secret_value(SecretId=secret_name)
    except ClientError as e:
        raise e
    else:
        if "SecretString" in get_secret_value_response:
            secret = get_secret_value_response["SecretString"]

            return json.loads(secret)
        else:
            decoded_binary_secret = base64.b64decode(
                get_secret_value_response["SecretBinary"]
            )
            return json.loads(decoded_binary_secret)


def get_redshift_conn():
    """Creates a connection to Redshift based on credentials"""
    credentials = Credentials(
        **get_aws_secret(secret_name=SECRET_NAME),
    )
    # way to convert user and password of type SecretStr to str
    # refer to https://stackoverflow.com/a/65277859/13337635
    connection = psycopg2.connect(**json.loads(credentials.json()))
    connection.set_isolation_level(psycopg2.extensions.ISOLATION_LEVEL_AUTOCOMMIT)
    return connection


def handler(event, context, connection):
    if connection is None:
        try:
            connection = get_redshift_conn()
        except Exception as e:
            print(e)
            return {
                "statusCode": 500,
                "body": {
                    "message": f"Error setting up database connection:\n{e}",
                },
            }

    cursor = connection.cursor()
    query_statement = """INSERT INTO raw
    (submission_timestamp,age,race,gender,nationality,edu_qualification,job_title,years_exp,num_jobs,in_malaysia,is_remote,state,company_type,industry,industry_other,job_specialisation,job_other,avg_work_hours,avg_workdays_week,gross_monthly_salary,starting_salary,happy_rating,job_satisfaction_rating,thoughts,email,code)
    VALUES %s"""
    try:
        psycopg2.extras.execute_values(
            cursor,
            query_statement,
            [
                (
                    event["queryStringParameters"]["submission_timestamp"],
                    int(event["queryStringParameters"]["age"]),
                    event["queryStringParameters"]["race"],
                    event["queryStringParameters"]["gender"],
                    event["queryStringParameters"]["nationality"],
                    event["queryStringParameters"]["edu_qualification"],
                    event["queryStringParameters"]["job_title"],
                    event["queryStringParameters"]["years_exp"],
                    int(event["queryStringParameters"]["num_jobs"]),
                    event["queryStringParameters"]["in_malaysia"],
                    event["queryStringParameters"]["is_remote"],
                    event["queryStringParameters"]["state"],
                    event["queryStringParameters"]["company_type"],
                    event["queryStringParameters"]["industry"],
                    event["queryStringParameters"]["industry_other"],
                    event["queryStringParameters"]["job_specialisation"],
                    event["queryStringParameters"]["job_other"],
                    float(event["queryStringParameters"]["avg_work_hours"]),
                    float(event["queryStringParameters"]["avg_workdays_week"]),
                    float(event["queryStringParameters"]["gross_monthly_salary"]),
                    float(event["queryStringParameters"]["starting_salary"]),
                    int(event["queryStringParameters"]["happy_rating"]),
                    int(event["queryStringParameters"]["job_satisfaction_rating"]),
                    event["queryStringParameters"]["thoughts"],
                    event["queryStringParameters"]["email"],
                    event["queryStringParameters"]["code"],
                )
            ],
        )
        connection.commit()
        cursor.close()
        print("Successfully added new entry")
        return {
            "statusCode": 201,
            "body": {
                "message": "User successfully added!",
            },
        }
    except Exception as e:
        print(e)
        return {
            "statusCode": 500,
            "body": {
                "message": "Error inserting user into table:\n {e}",
            },
        }
    finally:
        if connection is not None:
            connection.close()
